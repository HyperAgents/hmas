from glob import glob
from json import dumps

from corese import (
    query_graph, 
    safe_load,
    prefix_manager,
    owl_profile,
    check_OWL_constraints
)
from constants import (
    GET_BY_MODULE,
    NOT_REFERENCED,
    SRC_PATH,
    ONTOLOGY_SEPARATOR,
    DOMAIN_OUT_Of_VOCABULARY,
    RANGE_OUT_OF_VOCABULARY,
    GET_TERM_PAIRS,
    TERM_DISTANCE_THRESHOLD
)

def group_terms_by_module(modelet):
    """Get all the triples that has a subject included in the ontology.
    Group all of these triples by module (using rdfs:isDefinedBy property)

    :param modelet: Corese graph containing the modelet
    :returns: A dictionary of n3 for each module to be merged with the given n3
    """
    tsv = query_graph(modelet, GET_BY_MODULE)

    grouped_triples = {}

    for line in tsv:
        cut_line = line.split('\t')
        module = cut_line[0][1:-1].split(ONTOLOGY_SEPARATOR)[-1]
        triple = []

        for element in cut_line[1:]:
            uri = ""
            # Resolve the URI if the element is prefixed
            if not element[0] in ['<', '"', "'"]:
                prefix = element.split(":")[0]
                base_url = prefix_manager.getNamespace(prefix)
                uri = f"<{base_url}{element[len(prefix)+1:]}>"
            else:
                uri = element
            triple.append(uri)

        triple = " ".join(triple) + " ."

        if not module in grouped_triples:
            grouped_triples[module] = triple
        else:
            grouped_triples[module] += "\n" + triple

    return grouped_triples

def profile_check(ontology, extras=""):
    """Returns a report about whether an ontology is compatible with each profile and if not, why

    :param ontology: Corese graph containing the modelet
    :param extra: string in n3 notation, additional triples to add to the graph
    :returns: A dictionary with a key for each profile containing itself another dictionary
    with a key "is_reached" mapping a boolean indicating a compatibility, and a "message" justifying the result
    """

    if isinstance(ontology, str):
        ontology = safe_load(ontology, extras)

    if isinstance(ontology, dict):
        return ontology

    decidability_range = ["OWL_TC", "OWL_RL", "OWL_QL", "OWL_EL"]
    engine = owl_profile(ontology)

    report = {}

    for decidability_level in decidability_range:
        # Keeping 2 arrays containing almost the same thing was not necessary, so getattr
        profile = getattr(owl_profile, decidability_level)
        is_reached, message = engine.process(profile), engine.getMessage()
        engine.setMessage("")
        report[decidability_level] = {
            "is_reached": is_reached,
            "message": message.strip()
        }

    # Check for respect for OWL constraints
    OWL_constraints_errors = check_OWL_constraints(ontology)

    report["test_run"] = len(OWL_constraints_errors) == 0
    report["syntax_errors"] = []
    report["constraint_errors"] = OWL_constraints_errors

    return report

def health_check(graph):
    """Proceed to make a profile check of a given graph while checking the termes not referencing a modelet

    :param graph: The graph
    :returns: An error report
    """
    report = profile_check(graph)
    report["warnings"] = []
    
    # Check for terms not linked to an ontology
    unlinked_subjects = query_graph(graph, NOT_REFERENCED)
    unlinked_subjects = [
        f"Warning: Subject {item} not linked to a module by an rdfs:isDefinedBy property"
        for item in unlinked_subjects
    ]

    report["warnings"] += unlinked_subjects
    return report

def modules_tests(glob_path):
    """Returns a report about of a profile check of a set of ontologies

    :param glob_path: A glob-format path string
    :returns: A dictionary of reports, the keys are the file paths
    """

    modules = glob(glob_path) if isinstance(glob_path, str) else glob_path
    report = {}

    for module in modules:
        module_graph = safe_load(module)

        if isinstance(module_graph, dict):
            report[module] = module_graph
            continue

        report[module] = health_check(module_graph)

    return report, [key for key in report.keys() if report[key]["test_run"]]

def modelets_tests(glob_path):
    """Test of the modelets
    Test them individually, and then checks how each module behave
    when merged with their related terms in the modelets

    :param glob_path: A glob-format path string
    :returns: A dictionary of reports
    """

    modelets = glob(glob_path) if isinstance(glob_path, str) else glob_path
    report = {}

    for modelet in modelets:
        if "template" in modelet:
            continue

        graph = safe_load(modelet, import_from_src=True)

        if isinstance(graph, dict):
            report[modelet] = graph
            continue
        
        # Indivual profile check
        report[modelet] = {}
        report[modelet]["standalone"] = health_check(graph)   
        
        # Add each triple of the modelet to their related ontology, then proceed to profile checks
        moduled_triples = group_terms_by_module(graph)
        report[modelet]["merged"] = {}

        for module in moduled_triples.keys():         
            merged_graph = safe_load(
                f"{SRC_PATH}{module}.ttl",
                extras=moduled_triples[module]
            )
            report[modelet]["merged"][module] = health_check(merged_graph)

        report[modelet]["file"] = modelet
        report[modelet]["test_run"] = True
        report[modelet]["syntax_errors"] = ""
        report[modelet]["message"] = ""

    return report, [
        modelet for modelet in report.keys() 
        if "standalone" in report[modelet] and report[modelet]["standalone"]["test_run"]
    ]

def levenshtein(s1, s2):
    """Returns the levenshtein distance between two trings
    Algorithm borrowed from https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Levenshtein_distance#Python

    :param s1: The first string
    :param s2: The second string
    :returns: The levenshtein distance
    """
    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1       # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]

def best_practices_test(ontology):
    """Test the best practices mistakes that do not break the RDF syntax neither the OWL reasoning,
    but that should still not happen

    :param ontology: The ontology to test
    :returns: An report dictionary
    """
    if isinstance(ontology, str):
        ontology = safe_load(ontology, import_from_src=True)

    # This should not happen since it was checked before
    if isinstance(ontology, dict):
        return ontology
    
    report = {"warnings": []}
    
    # Checking for domain property out of the vocabulary
    domain_out_of_vocabulary = query_graph(ontology, DOMAIN_OUT_Of_VOCABULARY)
    domain_out_of_vocabulary = [line.split("\t") for line in domain_out_of_vocabulary]
    domain_out_of_vocabulary = [
        f"The property {item[0][1:-1]} has a domain out of the ontology: {item[1]}"
        for item in domain_out_of_vocabulary
    ]
    report["warnings"] += domain_out_of_vocabulary

    # Checking for range property out of the vocabulary
    range_out_of_vocabulary = query_graph(ontology, RANGE_OUT_OF_VOCABULARY)
    range_out_of_vocabulary = [line.split("\t") for line in range_out_of_vocabulary]
    range_out_of_vocabulary = [
        f"The property {item[0][1:-1]} has a range out of the ontology: {item[1]}"
        for item in range_out_of_vocabulary
    ]
    report["warnings"] += range_out_of_vocabulary

    # Checking for too close terms
    term_pairs = query_graph(ontology, GET_TERM_PAIRS)
    term_pairs = [
        [item.strip()[1:-1] for item in line.split("\t")]
        for line in term_pairs
    ]
    too_close_terms = [
        f"The following terms are too similar: {line[0]} and {line[1]}"
        for line in term_pairs
        if levenshtein(line[0], line[1]) < TERM_DISTANCE_THRESHOLD
    ]
    report["warnings"] += too_close_terms

    return report

def best_practices_tests(modules, modelets):
    """Launch a bunch of best pratices tests on modules and modelets

    :param modules: The modules paths to test
    :param modelets: The modelets paths to test
    :returns: An report dictionary
    """

    report = {"modules": {}, "modelets": {}}

    # Best practices on modules
    for module in modules:
        report["modules"][module] = best_practices_test(module)

    # Best practices on modules
    for modelet in modelets:
        if "template" in modelet:
            continue

        graph = safe_load(modelet, import_from_src=True)

        # This is not supposed to happen, we have filtered the cursed ones
        if isinstance(graph, dict):
            report["modelets"][modelet] = graph
            continue 

        # Tests on best practices on standalone modelets
        report["modelets"][modelet] = {"merged": {}}
        report["modelets"][modelet]["standalone"] = best_practices_test(graph)
        
        # Add each triple of the modelet to their related ontology, then proceed to best_practices_test
        moduled_triples = group_terms_by_module(graph)

        for module in moduled_triples.keys():         
            merged_graph = safe_load(
                f"{SRC_PATH}{module}.ttl",
                extras=moduled_triples[module]
            )
            report["modelets"][modelet]["merged"][module] = best_practices_test(merged_graph)
    
    # Test all modules and modelets together
    all_graphs = modules + modelets
    global_graph = safe_load(all_graphs, import_from_src=True)
    report["global"] = best_practices_test(global_graph)

    return report
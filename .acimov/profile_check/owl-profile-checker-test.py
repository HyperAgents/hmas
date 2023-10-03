from glob import glob
from json import dumps

from corese import (
    query_graph, 
    safe_load,
    prefix_manager,
    owl_profile,
    print_title,
    check_OWL_constraints
)
from constants import (
    GET_BY_MODULE,
    NOT_REFERENCED,
    SRC_PATH,
    ONTOLOGY_SEPARATOR,
    DOMAIN_OUT_Of_VOCABULARY,
    RANGE_OUT_OF_VOCABULARY,
    SRC_TTL_GLOB,
    DOMAINS_TTL_GLOB
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

def best_practices_test(ontology):
    graph = safe_load(ontology, import_from_src=True)

    # This should not happen since it was checked before
    if isinstance(graph, dict):
        return graph
    
    report = {"warnings": []}
    
    # Checking for domain property out of the vocabulary
    domain_out_of_vocabulary = query_graph(graph, DOMAIN_OUT_Of_VOCABULARY)
    domain_out_of_vocabulary = [
        f"The following property has a domain out of the ontology: {item}"
        for item in domain_out_of_vocabulary
    ]
    report["warnings"] += domain_out_of_vocabulary

    # Checking for range property out of the vocabulary
    range_out_of_vocabulary = query_graph(graph, RANGE_OUT_OF_VOCABULARY)
    range_out_of_vocabulary = [
        f"The following property has a range out of the ontology: {item}"
        for item in range_out_of_vocabulary
    ]
    report["warnings"] += range_out_of_vocabulary

    return report

def best_practices_tests(modules, modelets):
    report = {}

    # Best practices on modules
    for module in modules:
        report[module] = best_practices_test(module)

    # TODO Best practices on modelets

    return report

###
# Test OWL_RL
###

safe_modules = glob(SRC_TTL_GLOB)
print_title("Profile check")
print_title("Checking existing modules")
base_modules_report, safe_modules = modules_tests(safe_modules)

print_title("Checking modelets")
safe_modelets = glob(DOMAINS_TTL_GLOB)
modelets_report, safe_modelets = modelets_tests(safe_modelets)

print_title("Checking best practices")
best_practices_reports = best_practices_tests(safe_modules, safe_modelets)
report = {
    "base_modules": base_modules_report,
    "modelets": modelets_report, 
    "best_practices": best_practices_reports
}

with open("report.json", 'w') as f:
    f.write(dumps(report,sort_keys=True, indent=4))
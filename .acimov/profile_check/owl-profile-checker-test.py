from glob import glob
from json import dumps

from corese import (
    query_graph, 
    safe_load,
    prefix_manager,
    OWLProfile,
    printTitle
)
from constants import (
    GET_BY_MODULE,
    NOT_REFERENCED,
    SRC_PATH,
    DOMAINS_PATH,
    ONTOLOGY_SEPARATOR
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
            grouped_triples[module] = "\n" + triple

    return grouped_triples

def profile_check(ontology, extras=""):
    """Returns a report about whether an ontology is compatible with each profile and if not, why

    :param ontology: Corese graph containing the modelet
    :param extra: string in n3 notation, additional triples to add to the graph
    :returns: A dictionary with a key for each profile containing itself another dictionary
    with a key "is_reached" mapping a boolean indicating a compatibility, and a "message" justifying the result
    """
    syntax_errors = ""

    if isinstance(ontology, str):
        ontology = safe_load(ontology, extras)

    if isinstance(ontology, dict):
        return ontology

    decidability_range = ["OWL_TC", "OWL_RL", "OWL_QL", "OWL_EL"]
    engine = OWLProfile(ontology)

    report = {}

    for decidability_level in decidability_range:
        # Keeping 2 arrays containing almost the same thing was not necessary, so getattr
        profile = getattr(OWLProfile, decidability_level)
        is_reached, message = engine.process(profile), engine.getMessage()
        engine.setMessage("")
        report[decidability_level] = {
            "is_reached": is_reached,
            "message": message.strip()
        }

    report["test_run"] = True
    report["syntax_errors"] = syntax_errors

    return report

def modules_tests(glob_path):
    """Returns a report about of a profile check of a set of ontologies

    :param glob_path: A glob-format path string
    :returns: A dictionary of reports, the keys are the file paths
    """
    modules = glob(glob_path)

    report = {}

    for module in modules:
        report[module] = profile_check(module)

    return report

def modelets_tests(glob_path):
    """Test of the modelets
    Test them individually, and then checks how each module behave
    when merged with their related terms in the modelets

    :param glob_path: A glob-format path string
    :returns: A dictionary of reports
    """
    modelets = glob(glob_path)
    modelets_report = {}

    for modelet in modelets:
        if "template" in modelet:
            continue

        graph = safe_load(modelet)

        if isinstance(graph, dict):
            modelets_report[modelet] = graph
            continue
        
        # Indivual profile check
        modelets_report[modelet] = {}
        modelets_report[modelet]['standalone'] = profile_check(graph)

        # Check for terms not linked to an ontology
        unlinked_subjects = query_graph(graph, NOT_REFERENCED)
        unlinked_subjects = [
            f"Warning: Subject {item} not linked to a module by an rdfs:isDefinedBy property"
            for item in unlinked_subjects
        ]
        unlinked_subjects = "\n".join(unlinked_subjects)

        # Add each triple of the modelet to their related ontology, then proceed to profile checks
        moduled_triples = group_terms_by_module(graph)

        modelets_report[modelet]["merged"] = {}

        for module in moduled_triples.keys():         
            merged_graph = safe_load(f"{SRC_PATH}{module}.ttl", extras=moduled_triples[module])
            modelets_report[modelet]["merged"][module] = profile_check(merged_graph)

        modelets_report["file"] = modelet
        modelets_report["test_run"] = True
        modelets_report["syntax_errors"] = ""
        modelets_report["message"] = ""

    return modelets_report

###
# Test OWL_RL
###

printTitle("Profile check")
printTitle("Checking existing modules")
base_modules_report = modules_tests(f"{SRC_PATH}*.ttl")
printTitle("Checking modelets")
modelets_report = modelets_tests(f"{DOMAINS_PATH}*/*/onto.ttl")
report = {**base_modules_report , **modelets_report}

with open("report.json", 'w') as f:
    f.write(dumps(report,sort_keys=True, indent=4))
from glob import glob
from os.path import sep, relpath

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
    ONTOLOGY_SEPARATOR,
    DOMAIN_OUT_Of_VOCABULARY,
    RANGE_OUT_OF_VOCABULARY,
    GET_TERM_PAIRS,
    TERM_DISTANCE_THRESHOLD,
    DECIDABILITY_RANGE,
    PROFILE_ERROR_FORMAT,
    ONTOLOGY_URL,
    PWD_TO_ROOT_FOLDER
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

def profile_errors(message):
    lines =  message.split('\n')
    matches = [PROFILE_ERROR_FORMAT.match(item) for item in lines]
    matches = [i for i in range(len(matches)) if not matches[i] is None]

    messages = [lines[i] for i in matches]
    messages = ["".join(line.split('.')[1:]).strip() for line in messages]

    intervals = [range(matches[i] + 1, matches[i + 1]) for i in range(len(matches))[:-1]]
    intervals = intervals + [range(matches[-1] + 1, len(lines))]
    statements = [" ".join([lines[i] for i in item]).strip() for item in intervals]

    return [{"message": messages[i], "pointer": [statements[i]]} for i in range(len(messages)) if len(messages[i]) > 0]

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

    engine = owl_profile(ontology)

    report = {
        "profile-test": {},
        "syntax-test": {},
        "owl-rl-constraint-test": {}
    }

    for decidability_level in DECIDABILITY_RANGE:
        # Keeping 2 arrays containing almost the same thing was not necessary, so getattr
        profile = getattr(owl_profile, decidability_level)
        is_compatible, message = engine.process(profile), engine.getMessage()
        message = profile_errors(message)
        engine.setMessage("")
        error_name = f"{decidability_level.lower().replace('_', '-')}-profile-error"
        report["profile-test"][error_name] = message if not is_compatible else []

    # Check for respect for OWL constraints
    OWL_constraints_errors = [{"message": message} for message in check_OWL_constraints(ontology)]

    report["syntax-test"]["syntax-error"] = []
    report["owl-rl-constraint-test"]["owl-rl-constraint-violation"] = OWL_constraints_errors
    return report

def fragment_check(fragments, extras="", skip=[]):
    fragment_graph_no_import = safe_load(fragments, extras, disable_import=True)
    no_import_load_error = isinstance(fragment_graph_no_import, dict)

    if no_import_load_error:
        return fragment_graph_no_import, True
    
    fragment_graph_with_import = safe_load(fragments, extras)
    with_import_load_error = isinstance(fragment_graph_with_import, dict)

    # TODO implement the earl:NotTested for the tests that can not be run due to an unsafe import for instance

    profile_test = profile_check(fragment_graph_no_import)

    if with_import_load_error:
        return profile_test

    best_practices = best_practices_test(
        fragment_graph_with_import,
        fragment_graph_no_import,
        skip
    )
    
    return {**profile_test, **best_practices}, False

def modules_tests(glob_path):
    """Returns a report about of a profile check of a set of ontologies

    :param glob_path: A glob-format path string
    :returns: A dictionary of reports, the keys are the file paths
    """
    modules = glob(glob_path) if isinstance(glob_path, str) else glob_path
    report = []
    unsafe_modules = []

    for module in modules:
        module_key = relpath(module, PWD_TO_ROOT_FOLDER).replace(sep, "/")

        subject = {"heart": [module_key]}

        fragment_report, load_error = fragment_check(module)

        if load_error:
            unsafe_modules.append(module)

        report.append({
            "subject": subject,
            "report": fragment_report
        })

    return report, unsafe_modules

def modelets_tests(glob_path, skip_merge_test=False):
    """Test of the modelets
    Test them individually, and then checks how each module behave
    when merged with their related terms in the modelets

    :param glob_path: A glob-format path string
    :returns: A dictionary of reports
    """

    modelets = glob(glob_path) if isinstance(glob_path, str) else glob_path
    report = []
    unsafe_modelets = []

    for modelet in modelets:
        if "template" in modelet:
            continue

        modelet_key = relpath(modelet, PWD_TO_ROOT_FOLDER).replace(sep, "/")

        standalone_subject = {
            "heart": [modelet_key]
        }

        standalone_report, load_error = fragment_check(
            modelet,
            skip=["domain-and-range-referencing-test"]
        )

        report.append({
            "subject": standalone_subject,
            "report": standalone_report
        })

        if load_error:
            unsafe_modelets.append(modelet)
            continue

        if skip_merge_test:
            continue
        
        # Add each triple of the modelet to their related ontology, then proceed to profile checks
        alone_no_owl = safe_load(
            modelet,
            disable_owl=True
        )
        moduled_triples = group_terms_by_module(alone_no_owl)

        for module in moduled_triples.keys():         
            merged_subject = {
                "heart": [f"src/{module}.ttl"],
                "appendix": [modelet_key]
            }

            report.append({
                "subject": merged_subject,
                "report": fragment_check(
                    merged_subject["heart"],
                    moduled_triples[module]
                )[0]
            })

    return report, unsafe_modelets

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

def best_practices_test(
        fragment_wih_import,
        fragment_no_import,
        skip=[]):
    """Test the best practices mistakes that do not break the RDF syntax neither the OWL reasoning,
    but that should still not happen

    :param ontology: The ontology to test
    :returns: An report dictionary
    """
    
    report = {}

    # Check for terms not linked to an ontology
    if not "term-referencing-test" in skip:
        unlinked_subjects = query_graph(fragment_no_import, NOT_REFERENCED)
        unlinked_subjects = [
            {
                "message": f"Subject {item} not linked to a module by a rdfs:isDefinedBy property",
                "pointer": [item]
            }
            for item in unlinked_subjects
        ]
        report["term-referencing-test"] = {}
        report["term-referencing-test"]["no-reference-module"] = unlinked_subjects
    
    if not "domain-and-range-referencing-test" in skip:
        # Checking for domain property out of the vocabulary
        domain_out_of_vocabulary = query_graph(fragment_wih_import, DOMAIN_OUT_Of_VOCABULARY)
        domain_out_of_vocabulary = [line.split("\t") for line in domain_out_of_vocabulary]
        domain_out_of_vocabulary = [
            {
                "message": f"The property {item[0][1:-1]} has a domain out of the ontology: {item[1]}",
                "pointer": [f"<{ONTOLOGY_URL}{item[0][1:-1]}>", item[1]]
            }
            for item in domain_out_of_vocabulary
        ]

        # Checking for range property out of the vocabulary
        range_out_of_vocabulary = query_graph(fragment_wih_import, RANGE_OUT_OF_VOCABULARY)
        range_out_of_vocabulary = [line.split("\t") for line in range_out_of_vocabulary]
        range_out_of_vocabulary = [
            {
                "message": f"The property {item[0][1:-1]} has a range out of the ontology: {item[1]}",
                "pointer": [f"<{ONTOLOGY_URL}{item[0][1:-1]}>", item[1]]
            }
            for item in range_out_of_vocabulary
        ]
        report["domain-and-range-referencing-test"] = {}
        report["domain-and-range-referencing-test"]["domain-out-of-vocabulary"] = domain_out_of_vocabulary
        report["domain-and-range-referencing-test"]["range-out-of-vocabulary"] = range_out_of_vocabulary

    # Checking for too close terms
    if not "terms-differenciation-test" in skip:
        term_pairs = query_graph(fragment_no_import, GET_TERM_PAIRS)
        term_pairs = [
            [item.strip()[1:-1] for item in line.split("\t")]
            for line in term_pairs
        ]
        too_close_terms = [
            {
                "message": f"The following terms are too similar: :{line[0]} and :{line[1]}",
                "pointer": [f"<{ONTOLOGY_URL}{item}>" for item in line]
            }
            for line in term_pairs
            if levenshtein(line[0], line[1]) < TERM_DISTANCE_THRESHOLD
        ]
        report["terms-differenciation-test"] = {}
        report["terms-differenciation-test"]["too-close-terms"] = too_close_terms

    return report

def merged_fragment_set_test(fragments_to_merge, heart_name):
    fragments_keys = [
        relpath(fragment, PWD_TO_ROOT_FOLDER).replace(sep, "/")
        for fragment in fragments_to_merge
    ]

    subject = {
        "heart": fragments_keys,
        "name": heart_name
    }

    merged_fragments_report, _ = fragment_check(fragments_to_merge)

    return [{
        "subject": subject,
        "report": merged_fragments_report
    }]

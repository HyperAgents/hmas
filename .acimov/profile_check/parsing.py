# We don't need reasoning, profile checking etc
from rdflib import (
    Graph,
    BNode,
    Literal,
    URIRef,
    Namespace
)

from rdflib.namespace import (
    RDF,
    RDFS,
    FOAF,
    DCTERMS,
    SDO
)

from constants import (
    DEV_USERNAME,
    PROFILE_CHECK_URI,
    DEV_PROFILE,
    DOMAINS_URL,
    PROFILE_CHECK_URI,
    EARL_NAMESPACE,
    SRC_NAMESPACE,
    TEST_NAMESPACE,
    ACIMOV_MODEL_NAMESPACE,
    ONTOLOGY_NAMESPACE,
    TEST_RESOURCES,
    BRANCH
)

# TODO a faire pour plus tard
def parse_turtle_to_html(turtle):
    raise NotImplementedError()

def statement(self, subject, *po):
    for item in po:
        self.add((subject, item[0], item[1]))

def assertGroup(g, mode):
    assertorId = f"{DEV_USERNAME}-{mode}"
    title = f"{DEV_USERNAME} using {mode} script"
    description = f"Represents the user @{DEV_USERNAME} launching the {mode} test script"
    scriptURI = f"{PROFILE_CHECK_URI}manual-test"
    
    # Define the developper and the assertor
    assert_group = BNode(assertorId)
    developper = BNode(DEV_USERNAME)

    # Define the developper
    g.statement(
        developper,
        (RDF.type, FOAF.Person),
        (SDO.mainEntityOfPage, URIRef(DEV_PROFILE))
    )

    # Define the developper using the software
    g.statement(
        assert_group,
        (RDF.type, FOAF.OnlineAccount),
        (DCTERMS.title, Literal(title, lang="en")),
        (DCTERMS.description, Literal(description, lang="en")),
        (EARL_NAMESPACE.mainAssertor, developper),
        (FOAF.member, URIRef(scriptURI))
    )

    return assert_group

def get_subject_id_part(fragment_list):
    modules = [item for item in fragment_list if item.startswith("src/")]
    modules = ['.'.join(item[4:].split('.')[:-1]) for item in modules]
    modules.sort()
    modelets = [item for item in fragment_list if item.startswith("domains/")]
    modelets = ['-'.join(item.split('/')[1:-1]) for item in modelets]
    modelets.sort()

    subject_id_part = '-'.join(modules + modelets)
    return subject_id_part

def get_subject_id(subject):
    heart_id = get_subject_id_part(subject["heart"])
    result = [heart_id]

    if "appendix" in subject and len(subject["appendix"]):
        appendix_id = get_subject_id_part(subject["appendix"])
        result.append(appendix_id)

    subject_id = "-".join(result)
    return subject_id

def testSubject(
        g,
        json_subject
):
    heart = json_subject['heart']
    appendix = [] if not "appendix" in json_subject else json_subject["appendix"] 
    subject_id = get_subject_id(json_subject) if not "name" in json_subject else json_subject["name"]

    heart_type = "Set of fragments" if len(heart) > 1 else \
                f"{'Standalone' if len(appendix) == 0 else 'Merged'} {'module' if heart[0].startswith('src/') else 'modelet'}"
    
    title = f"{heart_type} {', '.join(heart)} from branch {BRANCH}"

    if len(appendix) > 0:
        title = f"{title} with related terms from the fragments {', '.join(appendix)}"
    
    module_fragments = [item for item in heart + appendix if item.startswith('src/')]
    module_fragments = [
        SRC_NAMESPACE['.'.join(item.split('/')[-1].split('.')[:-1])]
        for item in module_fragments
    ]
    
    modelets_fragment = [item for item in heart + appendix if item.startswith('domains/')]
    modelets_fragment = [
        URIRef(DOMAINS_URL + item.split("domains/")[-1])
        for item in modelets_fragment
    ]

    test_subject = BNode(subject_id)
    statements = [
        (DCTERMS.hasPart, part)
        for part in module_fragments + modelets_fragment
    ]

    statements = [
        (RDF.type, EARL_NAMESPACE.TestSubject),
        (DCTERMS.title, Literal(title, lang="en"))
    ] + statements
    g.statement(test_subject, *statements)

    return test_subject

def testCriterion(
        g,
        title,
        description,
        testURI
):
    test_criterion = BNode()
    g.statement(
        test_criterion,
        (RDF.type, EARL_NAMESPACE.TestCriterion),
        (DCTERMS.title, Literal(title, lang="en")),
        (DCTERMS.description, Literal(description, lang="en")),
        (RDFS.seeAlso, testURI)
    )
    return test_criterion

def testResult(
        g,
        json_result,
        test_resource,
        skip_pass=False
    ):
    rdf_result = BNode()
    g.add((rdf_result, RDF.type, EARL_NAMESPACE.TestResult))    
    errors_summaries = []

    for error_id in json_result.keys():
        error_list = json_result[error_id]

        if len(error_list) == 0:
            if skip_pass:
                continue
            errors_summaries.append([
                (RDF.type, EARL_NAMESPACE.Pass),
                (
                    DCTERMS.title,
                    Literal(test_resource["errors"][error_id]["pass_title"], lang="en")
                ),
                (
                    DCTERMS.description,
                    Literal(test_resource["errors"][error_id]["pass_description"], lang="en")
                )
            ])
        
        for error in error_list:
            error_summary = [
                (
                    RDF.type,
                    EARL_NAMESPACE.Fail if test_resource["errors"][error_id]["is_blocking"]
                    else EARL_NAMESPACE.CantTell
                ),
                (
                    DCTERMS.title,
                    Literal(test_resource["errors"][error_id]["fail_title"], lang="en")
                ),
                (
                    DCTERMS.description,
                    Literal(error["message"], lang="en")
                )
            ]
            if "pointer" in error:
                for pointer_string in error["pointer"]:
                    if len(pointer_string) == 0:
                        continue
                    
                    statement_subject = pointer_string.split(" ")[0]

                    if statement_subject[0] == "<":
                        pointer = URIRef(statement_subject[1:-1])
                    elif statement_subject[0] != "[":
                        normalizedUri = Namespace(
                            [
                                namespace for prefix, namespace in g.namespaces()
                                if prefix == pointer_string.split(":")[0]
                            ][0]
                        )[pointer_string.split(":")[1]]
                        pointer = URIRef(normalizedUri)
                    else:
                        pointer = Literal(pointer_string)

                    # TODO deal with the anonymous statements a better way
                    error_summary.append((RDFS.seeAlso, pointer))

            errors_summaries.append(error_summary)
    
    for summary in errors_summaries:
        test_outcome = BNode()
        g.statement(test_outcome, *summary)
        g.add((rdf_result, EARL_NAMESPACE.outcome, test_outcome))

    return rdf_result

def parse_subject_report(
        json_subject,
        subject_report,
        assert_group,
        g,
        skip_pass=False
):
    rdf_subject = None
    
    for criterion in subject_report.keys():
        # Early stop on skip_pass if the criterion has no error
        error_lists = subject_report[criterion].values()
        error_list_lengths = [
            len(error_list) for error_list in error_lists
            if len(error_list) > 0
        ]
        if skip_pass and len(error_list_lengths) == 0:
            continue

        rdf_subject = rdf_subject if not rdf_subject is None else testSubject(g, json_subject)
        test_result = testResult(
            g,
            subject_report[criterion],
            TEST_RESOURCES[criterion],
            skip_pass=skip_pass
        )
        assertion = BNode()
        g.statement(
            assertion,
            (RDF.type, EARL_NAMESPACE.Assertion),
            (EARL_NAMESPACE.assertedBy, assert_group),
            (EARL_NAMESPACE.subject, rdf_subject),
            (EARL_NAMESPACE.test, ACIMOV_MODEL_NAMESPACE[criterion]),
            (EARL_NAMESPACE.result, test_result)
        )

def parse_report_to_turtle(json_report, script_name, skip_pass=False) :
    g = Graph()
    g.statement = statement.__get__(g)

    g.bind("earl", EARL_NAMESPACE)
    g.bind("", ONTOLOGY_NAMESPACE)
    g.bind("src", SRC_NAMESPACE)
    g.bind("profile-test", TEST_NAMESPACE)
    g.bind("acimov-model-test", ACIMOV_MODEL_NAMESPACE)

    assert_group = assertGroup(g, script_name)

    # Reports of each assertion
    for json_assertion in json_report:
        parse_subject_report(
            json_assertion["subject"],
            json_assertion["report"],
            assert_group,
            g,
            skip_pass=skip_pass
        )

    return g.serialize(format="ttl")

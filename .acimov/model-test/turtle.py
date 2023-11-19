from datetime import datetime

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
    SDO,
    XSD
)

from constants import (
    DEV_USERNAME,
    DEV_PROFILE,
    DOMAINS_URL,
    EARL_NAMESPACE,
    SRC_NAMESPACE,
    TEST_NAMESPACE,
    ACIMOV_MODEL_NAMESPACE,
    ONTOLOGY_NAMESPACE,
    TEST_RESOURCES,
    BRANCH,
    MODULE_URL_FORMAT,
    MODELET_URL_FORMAT,
    PWD_TO_ROOT_FOLDER
)

def statement(self, subject, *po):
    for item in po:
        self.add((subject, item[0], item[1]))

def prepare_graph():
    graph = Graph()
    graph.statement = statement.__get__(graph)

    graph.bind("earl", EARL_NAMESPACE)
    graph.bind("", ONTOLOGY_NAMESPACE)
    graph.bind("src", SRC_NAMESPACE)
    graph.bind("profile-test", TEST_NAMESPACE)
    graph.bind("acimov-model-test", ACIMOV_MODEL_NAMESPACE)

    return graph

def make_assertor(report, mode, script_uri):
    assertorId = f"{DEV_USERNAME}-{mode}"
    title = f"{DEV_USERNAME} using {mode} script"
    description = f"Test triggered by @{DEV_USERNAME} by {mode} trigger"
    
    # Define the developper and the assertor
    assert_group = BNode(assertorId)
    developper = BNode(DEV_USERNAME)

    # Define the developper
    report.statement(
        developper,
        (RDF.type, FOAF.Person),
        (SDO.mainEntityOfPage, URIRef(DEV_PROFILE))
    )

    # Define the developper using the software
    report.statement(
        assert_group,
        (RDF.type, FOAF.OnlineAccount),
        (DCTERMS.title, Literal(title, lang="en")),
        (DCTERMS.description, Literal(description, lang="en")),
        (EARL_NAMESPACE.mainAssertor, developper),
        (FOAF.member, URIRef(script_uri)),
        (DCTERMS.date, Literal(datetime.now(), datatype=XSD.dateTime))
    )

    return assert_group

def make_subject_id_part(fragment_list):
    modules = [item for item in fragment_list if item.startswith("src/")]
    modules = ['.'.join(item[4:].split('.')[:-1]) for item in modules]
    modules.sort()
    modelets = [item for item in fragment_list if item.startswith("domains/")]
    modelets = ['-'.join(item.split('/')[1:-1]) for item in modelets]
    modelets.sort()

    subject_id_part = '-'.join(modules + modelets)
    return subject_id_part

def make_subject_id(heart, appendix=[]):
    result = [make_subject_id_part(heart)]

    if len(appendix):
        appendix_id = make_subject_id_part(appendix)
        result.append(appendix_id)

    subject_id = "-".join(result)
    return subject_id

def make_subject(
        report,
        heart,
        appendix=[],
        name="",
        custom_title=""
):
    subject_id = make_subject_id(heart, appendix=appendix) if name == "" else name

    heart_type = "Set of fragments" if len(heart) > 1 else \
                f"{'Standalone' if len(appendix) == 0 else 'Merged'} {'module' if heart[0].startswith('src/') else 'modelet'}"
    
    title = f"{heart_type} {', '.join(heart)} from branch {BRANCH}"

    if len(appendix) > 0:
        title = f"{title} with related terms from the fragments {', '.join(appendix)}"

    title = title if len(custom_title) == 0 else custom_title
    
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

    test_subject = BNode(subject_id, subject_id)
    statements = [
        (DCTERMS.hasPart, part)
        for part in module_fragments + modelets_fragment
    ]

    statements = [
        (RDF.type, EARL_NAMESPACE.TestSubject),
        (DCTERMS.title, Literal(title, lang="en")),
        (DCTERMS.identifier, Literal(subject_id))
    ] + statements
    report.statement(test_subject, *statements)

    return test_subject

def short_subject_part(part):
    module_search = MODULE_URL_FORMAT.findall(part)
    if len(module_search) > 0:
        return f"{PWD_TO_ROOT_FOLDER}{module_search[0]}.ttl"
    
    modelet_search = MODELET_URL_FORMAT.findall(part)
    if len(modelet_search) > 0:
        return f"{PWD_TO_ROOT_FOLDER}{modelet_search[0]}"
    
    return part

def extract_statement(report, subject, pointer):
    isolated_graph = Graph()

    for part in report.objects(subject, DCTERMS.hasPart):
        part_path = short_subject_part(str(part))
        isolated_graph.parse(part_path)
        
    isolated = isolated_graph.query(f"SELECT ?p ?o WHERE {{{pointer} ?p ?o}}")
    isolated = [line for line in isolated]

    if len(isolated) == 0:
        return URIRef(pointer[1:-1])
    
    isolated = [[f"<{str(item)}>" if isinstance(item, URIRef) else f'"{str(item)}"' for item in line] for line in isolated]
    isolated = [f"{pointer} {line[0]} {line[1]} ." for line in isolated]
    isolated = "\n".join(isolated)
    
    statement = Graph()

    for prefix, namespace in isolated_graph.namespaces():
        statement.bind(prefix, namespace)

    statement.parse(data=isolated, format="ttl")
    statement.bind("", ONTOLOGY_NAMESPACE)
    
    statement = statement.serialize(format="ttl", encoding="utf-8").decode(encoding="utf-8")
    statement = [line.strip().replace("<", "&#60;") for line in statement.split("\n") if len(line.strip()) > 0]
    
    for i in range(len(statement)):
        if not statement[i].startswith("@"):
            statement = "\n".join(statement[i:])
            break
    
    return Literal(statement)

def make_pointer(report, subject, pointer_string):
    statement_subject = pointer_string.split(" ")[0]
    is_statement = " " in pointer_string

    if statement_subject[0] == "<" and not is_statement and \
        pointer_string[1:].startswith(str(ONTOLOGY_NAMESPACE)):
        
        pointer = extract_statement(report, subject, statement_subject)
    elif statement_subject[0] != "[" and not is_statement:
        normalizedUri = Namespace(
            [
                namespace for prefix, namespace in report.namespaces()
                if prefix == pointer_string.split(":")[0]
            ][0]
        )[pointer_string.split(":")[1]]
        pointer = URIRef(normalizedUri)
    else:
        pointer = Literal(pointer_string.replace("<", "&#60;")) #.replace(">", "&#62;")
    
    return pointer

def make_outcome(
    report,
    subject,
    criterion,
    error,
    outcome_type,
    description="",
    pointers=[]
):
    outcome_ressources = TEST_RESOURCES[criterion]["errors"][error][outcome_type]
    outcome_title = outcome_ressources["title"]
    outcome_description = description if len(description) > 0 else outcome_ressources["description"]
    parsed_pointers = [make_pointer(report, subject, pointer) for pointer in pointers if len(pointer) > 0]
    outcome_statement = [
        (RDF.type, EARL_NAMESPACE[outcome_type]),
        (DCTERMS.title, Literal(outcome_title, lang="en")),
        (DCTERMS.description, Literal(outcome_description, lang="en"))
    ]
    outcome_statement += [(RDFS.seeAlso, pointer) for pointer in parsed_pointers]

    outcome = BNode()
    report.statement(outcome, *outcome_statement)

    return outcome

def make_outcomes(
    report,
    subject,
    criterion,
    error,
    messages,
    pointers=[],
    skip_pass=False
):
    if len(pointers) > 0 and not len(pointers) == len(messages):
        pointers = []
    
    outcomes = []
    outcome_ressources = TEST_RESOURCES[criterion]["errors"][error]
    if len(messages) == 0:
        if skip_pass:
            return []
        outcomes = [
            make_outcome(
                report,
                subject,
                criterion,
                error,
                "Pass",
                description=outcome_ressources["Pass"]["description"]
            )
        ]
    else:
        outcomes = [
            make_outcome(
                report,
                subject,
                criterion,
                error,
                "Fail" if outcome_ressources["blocking"] else "CannotTell",
                messages[i],
                pointers[i] if i < len(pointers) else []
            )
            for i in range(len(messages))
        ]

    return outcomes

def make_result(report, outcomes, skip_pass=False, not_tested=False):
    result_statement = [
        (RDF.type, EARL_NAMESPACE.TestResult)
    ] + [
        (EARL_NAMESPACE.outcome, outcome)
        for outcome in outcomes
        if not (make_outcome_type(report, outcome) == "Pass" and skip_pass) and
           not (make_outcome_type(report, outcome) == "NotTested" and not_tested)
    ]

    result = BNode()
    report.statement(result, *result_statement)

    return result

def make_outcome_type(report, result):
    outcome = report.value(result, EARL_NAMESPACE.outcome)
    outcomeType = report.value(outcome, RDF.type)
    earl_separator = str(EARL_NAMESPACE)[-1]
    return str(outcomeType).split(earl_separator)[-1]

def assemble_assertion(
    report,
    assertor,
    subject,
    criterion,
    result,
    skip_pass=False,
    tested_only=False
):
    statement = [
        (RDF.type, EARL_NAMESPACE.Assertion),
        (EARL_NAMESPACE.assertedBy, assertor),
        (EARL_NAMESPACE.subject, subject),
        (EARL_NAMESPACE.test, ACIMOV_MODEL_NAMESPACE[criterion]),
        (EARL_NAMESPACE.result, result),
    ]

    assertion = BNode()
    report.statement(assertion, *statement)

def make_assertion(
    report,
    assertor,
    subject,
    criterion,
    error,
    messages,
    pointers=[],
    skip_pass=False,
    tested_only=False
):
    assemble_assertion(
        report,
        assertor,
        subject,
        criterion,
        make_result(report,
            make_outcomes(
                report,
                subject,
                criterion,
                error,
                messages,
                pointers,
                skip_pass=skip_pass
            )
        ),
        skip_pass=skip_pass,
        tested_only=tested_only
    )

def make_not_tested(
    report,
    assertor,
    subject,
    criterion,
    tested_only=False
):
    if tested_only:
        return
    
    outcomes = TEST_RESOURCES[criterion]["errors"].keys()

    for outcome in outcomes:
        assemble_assertion(
            report,
            assertor,
            subject,
            criterion,
            make_result(
                report,
                [
                    make_outcome(
                        report,
                        None,
                        criterion,
                        outcome,
                        "NotTested"
                    )
                ],
                not_tested=tested_only
            )
            
        )

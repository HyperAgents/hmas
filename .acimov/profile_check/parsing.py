from os.path import sep

# We don't need reasoning, profile checking etc
from rdflib import (
    Graph,
    Namespace,
    BNode,
    Literal,
    URIRef
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
    SRC_URL,
    PROFILE_CHECK_URI,
    EARL_URL
)

def parse_turtle_to_html(turtle):
    raise NotImplementedError()

def statement(self, subject, *po):
    for item in po:
        self.add((subject, item[0], item[1]))

def parse_report_to_turtle(report) :
    g = Graph()
    g.statement = statement.__get__(g)
    
    EARL = Namespace(EARL_URL)
    SRC = Namespace(SRC_URL)
    TEST = Namespace(PROFILE_CHECK_URI)

    g.bind("earl", EARL)
    g.bind("src", SRC)
    g.bind("profile-test", TEST)

    # Define the developper and the assertor
    assert_group = BNode()
    developper = BNode()

    # Define the 
    g.statement(
        developper,
        (RDF.type, FOAF.Person),
        (SDO.mainEntityOfPage, URIRef(DEV_PROFILE))
    )

    # Define the developper using the software
    g.statement(
        assert_group,
        (RDF.type, FOAF.Group),
        (
            DCTERMS.title,
            Literal(
                f"{DEV_USERNAME} using Manual script",
                lang="en")
        ),
        (
            DCTERMS.description,
            Literal(
                f"Represents the user @{DEV_USERNAME} launching the manual test script",
                lang="en"
            )
        ),
        (EARL.mainAssertor, developper),
        (FOAF.member, URIRef(f"{PROFILE_CHECK_URI}manual-test.py"))
    )

    # Reports on the base modules
    base_modules = report["base_modules"]

    for module in base_modules.keys():
        # Define the test subject
        test_subject = BNode()
        g.statement(
            test_subject,
            (RDF.type, EARL.TestSubject),
            (
                DCTERMS.title,
                Literal("An isolated module", lang="en")
            ),
            (DCTERMS.hasPart, SRC[module.split(sep)[-1]])
        )

        # Define the test criterion
        syntax_test = BNode()
        g.statement(
            syntax_test,
            (RDF.type, EARL.TestSubject),
            (DCTERMS.title, Literal("Syntax test", lang="en")),
            (
                DCTERMS.description,
                Literal(
                    "A test meant to check wether the test subject is syntaxically correct or not.",
                    lang="en"
                )
            ),
            (RDFS.seeAlso, TEST["syntax-test"])
        )

        # Check of syntax errors
        # Define the test result
        syntax_result = BNode()
        syntax_outcome = BNode()
        g.statement(
            syntax_result,
            (RDF.type, EARL.TestResult),
            (EARL.outcome, syntax_outcome)
        )

        if len(base_modules[module]["syntax_errors"]) == 0:
            g.statement(
                syntax_outcome,
                (RDF.type, EARL.Pass),
                (
                    DCTERMS.title,
                    Literal("Test subject has a correct syntax", lang="en")
                ),
                (
                    DCTERMS.description,
                    Literal("Test subject has no syntax error", lang="en")
                )
            )
        else:
            g.statement(
                syntax_outcome,
                (RDF.type, EARL.Fail),
                (
                    DCTERMS.title,
                    Literal("Test subject has an incorrect syntax", lang="en")
                ),
                (
                    DCTERMS.description,
                    Literal("\n".join(base_modules[module]["syntax_errors"]), lang="en")
                ),
                (RDFS.seeAlso, TEST["syntax-error"])
            )
        
        # Define the assertion
        assertion = BNode()

        g.statement(
            assertion,
            (RDF.type, EARL.Assertion),
            (EARL.assertedBy, assert_group),
            (EARL.subject, test_subject),
            (EARL.test, syntax_test),
            (EARL.result, syntax_result)
        )

    return g.serialize(format="ttl")
from regex import compile as regex_compile
from subprocess import check_output
from rdflib import Namespace
from os import getcwd, environ
from os.path import sep, relpath, abspath

##############
# Parameters #
##############

# The ontology base URL
ONTOLOGY_URL = "https://purl.org/hmas/"
# The URL of the Corese python library to fetch
CORESE_PYTHON_URL = "https://files.inria.fr/corese/distrib/corese-library-python-4.4.1.jar"
# The desired levenshtein threshold to accept terms as different enough
TERM_DISTANCE_THRESHOLD = 3
# The EARL ontology prefix
EARL_PREFIX="http://www.w3.org/ns/earl#"

############################################
# Constants calculated from the parameters #
############################################

ROOT_FOLDER = abspath(
  f"{sep.join(abspath(__file__).split(sep)[:-1])}{sep}..{sep}.."
)

PWD_TO_ROOT_FOLDER = f"{relpath(ROOT_FOLDER, getcwd())}{sep}"
PWD_TO_MODEL_OUTPUT_FOLDER = f"{PWD_TO_ROOT_FOLDER}.acimov{sep}profile_check{sep}output{sep}"
PWD_TO_PROFILE_CHECK = f"{PWD_TO_ROOT_FOLDER}.acimov{sep}profile_check{sep}"

# The character separating the ontology base URL from the suffix
ONTOLOGY_SEPARATOR = ONTOLOGY_URL[-1]
# The corese python executable name
CORESE_JAR_NAME = CORESE_PYTHON_URL.split('/')[-1]

CORESE_LOCAL_PATH = abspath(f"{PWD_TO_PROFILE_CHECK}{CORESE_JAR_NAME}")

IS_GITHUB_ACTIONS = not environ.get("github.server_url") is None

# The reository URI

REPO_URI = check_output(
  "git config --get remote.origin.url".split(" ")
  )\
  .decode('utf-8')\
  .strip() if not IS_GITHUB_ACTIONS else \
  f"{environ.get('github.server_url')}/{environ.get('github.repository')}"

# Base reporitory platform URL
PLATFORM_URL = "/".join(REPO_URI.split("/")[:-2])

# The current branch
BRANCH = check_output(
  "git rev-parse --abbrev-ref HEAD".split(" ")
  )\
  .decode('utf-8')\
  .strip() if not IS_GITHUB_ACTIONS else \
  environ.get("github.ref_name")

# The relative path from root to the profile_test folder
PATH_TO_PROFILE_FOLDER = relpath(".", ROOT_FOLDER)

# The path to the profile check README.md
PROFILE_CHECK_URI = f"{REPO_URI}tree/{BRANCH}/{PATH_TO_PROFILE_FOLDER}"
  # TODO: Should be manual/precommit/actions compatible
  # git config --get remote.origin.url for precommit/manual
  # $GITHUB_SERVER_URL + '/' + $GITHUB_REPOSITORY for action

ACIMOV_MODEL_TEST_URI = f"{PROFILE_CHECK_URI}/model-test-onto.ttl"

DEV_USERNAME = ""
try:
  DEV_USERNAME = check_output("git config --global user.name".split(" "))\
  .decode('utf-8')\
  .strip()
except:
  DEV_USERNAME = "GithubActions"

# Format of a syntax error in the console
AST_ERROR_FORMAT = regex_compile("ERROR fr\\.inria\\.corese\\.sparql\\.triple\\.parser\\.ASTQuery")
PROFILE_ERROR_FORMAT = regex_compile("^[0-9]+\\. [^\\n]+|$")

# Glob path to modules
MODULES_TTL_GLOB_PATH = f"{PWD_TO_ROOT_FOLDER}src{sep}*.ttl"
# Glob path to modelets
MODELETS_TTL_GLOB_PATH = f"{PWD_TO_ROOT_FOLDER}domains{sep}*{sep}*{sep}onto.ttl"

# URL prefix for the files in the current branch in src
SRC_URL = f"{REPO_URI}blob/{BRANCH}/src/"
DOMAINS_URL = SRC_URL.replace("src", "domains")

DEV_PROFILE = f"{PLATFORM_URL}/{DEV_USERNAME}"

EARL_URL = "https://www.w3.org/ns/earl#"

ONTOLOGY_NAMESPACE = Namespace(ONTOLOGY_URL)
EARL_NAMESPACE = Namespace(EARL_URL)
SRC_NAMESPACE = Namespace(SRC_URL)
TEST_NAMESPACE = Namespace(PROFILE_CHECK_URI)
ACIMOV_MODEL_NAMESPACE = Namespace(f"{ACIMOV_MODEL_TEST_URI}#")

# The different levels of OWL profile decidability available un CORESE
DECIDABILITY_RANGE = ["OWL_TC", "OWL_RL", "OWL_QL", "OWL_EL"]

# SparQL request listing all the ontology terms not linked to a moduled by a rdfs:isDefinedBy property
NOT_REFERENCED = """
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

SELECT DISTINCT ?s where {
  ?s ?p ?o .
  FILTER(strstarts(str(?s), "ONTOLOGY_URL"))
  FILTER NOT EXISTS { ?s rdfs:isDefinedBy [] . }
  FILTER NOT EXISTS { ?s rdf:type owl:Ontology . }
  FILTER NOT EXISTS { ?s rdf:type skos:Concept . }
  FILTER NOT EXISTS { FILTER ( str(?s) =  "ONTOLOGY_URL" ) }
}
""".replace("ONTOLOGY_URL", ONTOLOGY_URL)

# SparQL request to get all the triples with their related modules, using the rdfs:isDefinedBy property 
GET_BY_MODULE = """
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

SELECT ?m ?s ?p ?o where {
  ?s ?p ?o .
  ?s rdfs:isDefinedBy ?m .
  FILTER(strstarts(str(?s), "ONTOLOGY_URL"))
}
ORDER BY ?m
""".replace("ONTOLOGY_URL", ONTOLOGY_URL)

# SparQL request to get all the properties with a domain linking to a term not defined in the ontology
DOMAIN_OUT_Of_VOCABULARY = """
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

SELECT DISTINCT ?suffix ?domain WHERE {
  # Get all the properties with a defined domain
  ?property rdf:type owl:ObjectProperty .
  ?property rdfs:domain ?domain .

  # Get only the most specialized domains for each property
  FILTER NOT EXISTS {
    ?property rdfs:domain ?domain2 .
    ?domain2 owl:subClassOf ?domain .
  }

  # Ignore the owl:Thing domains
  FILTER NOT EXISTS {
    FILTER (?domain = owl:Thing)
  }
  
  # Ignore the domains in the ontology
  FILTER NOT EXISTS {
    ?domain rdf:type ?o .
    FILTER(strstarts(str(?domain), "ONTOLOGY_URL"))
  }
  
  # Ignore the properties out of the ontology
  FILTER(strstarts(str(?property), "ONTOLOGY_URL"))

  # Format the result
  BIND (SUBSTR(str(?property), STRLEN("ONTOLOGY_URL") + 1) as ?suffix)
}
""".replace("ONTOLOGY_URL", ONTOLOGY_URL)

# SparQL request to get all the properties with a range linking to a term not defined in the ontology
RANGE_OUT_OF_VOCABULARY = DOMAIN_OUT_Of_VOCABULARY.replace("domain", "range")

# Gets all the imports in a graph
GET_IMPORTS = """
SELECT DISTINCT ?i WHERE {
  ?s rdf:type owl:Ontology ;
  owl:imports ?i .
}
"""

# Not used for now... a LDScript implementation of the Levenshtein distance
# Works on Corese command but not on GUI
LEVENSHTEIN_FUNCTION = """
function fun:levenshtein(x, y) {
  if (strlen(x) = 0) {
    return (strlen(y))
  }
  else {
    if (strlen(y) = 0) {
      return (strlen(x))
    }
    else {
      let (
        x0 = substr(x, 1, 1),
        y0 = substr(y, 1, 1),
        indicator = if(x0 = y0, 0, 1),
        subx = substr(x, 2),
        suby = substr(y, 2)
      ) {
        return (
          fun:min(
            xt:list (
              fun:levenshtein(subx, y) + 1,
              fun:levenshtein(suby, x) + 1,
              fun:levenshtein(subx, suby) + indicator
            ),
            0,
            0
          )
        )
      }
    }
  }
}

function fun:min(list, i, currentMin) {
  if (i = 0) {
    return (
      fun:min(list, i + 1, xt:get(list, 0))
    )
  }
  else {
    if (i >= xt:size(list)) {
      return (currentMin)
    }
    else {
      let (currentElement = xt:get(list, i)) {
        if (currentElement < currentMin) {
          return (fun:min(list, i + 1, currentElement))
        }
        else {
          return (fun:min(list, i + 1, currentMin))
        }
      }
    }
  }
}
"""

# SparQL request getting all the pairs of suffixes from the ontology in a given graph
# Gets rid of the duplicates (ab and ba) and the auto pairs (aa)
GET_TERM_PAIRS = """
SELECT DISTINCT ?suffix1 ?suffix2 WHERE {
  ?s1 ?p1 [] .
  ?s2 ?p2 [] .
  FILTER(strstarts(str(?s1), "ONTOLOGY_URL"))
  FILTER(strstarts(str(?s2), "ONTOLOGY_URL"))
  FILTER(str(?s1) > str(?s2))
  BIND (SUBSTR(str(?s1), STRLEN("ONTOLOGY_URL") + 1) as ?suffix1)
  BIND (SUBSTR(str(?s2), STRLEN("ONTOLOGY_URL") + 1) as ?suffix2)
} ORDER BY ?suffix1
""".replace("ONTOLOGY_URL", ONTOLOGY_URL)

# Not used for now
# Gets the pairs of suffixes in the given graph and gives all the pairs of terms that are too similar
GET_TOO_CLOSED_PAIRS = """
SELECT ?suffix1 ?suffix2 ?distance WHERE {
  {
    GET_TERM_PAIRS
  }
  BIND(fun:levenshtein(?suffix1, ?suffix2) AS ?distance)
  FILTER(?distance > TERM_DISTANCE_THRESHOLD)
}

""".replace(
    "GET_TERM_PAIRS",
    GET_TERM_PAIRS
  ).replace(
      "TERM_DISTANCE_THRESHOLD",
      str(TERM_DISTANCE_THRESHOLD)
) + LEVENSHTEIN_FUNCTION

BLOCKINGS_ERRORS = """
select ?n ?c ?t ?d where {
  ?a a earl:Assertion ;
  earl:subject ?s ;
  earl:test ?c ;
  earl:result ?r .

  ?s dcterms:title ?n .

  ?r a earl:TestResult ;
  earl:outcome ?o .

  ?o a earl:Fail ;
  dcterms:title ?t ;
  dcterms:description ?d .
}
"""

# TODO make a resource script providing the messages
TEST_RESOURCES = {
    "term-referencing-test": {
        "title": "Term referencing test",
        "description": "Test checking if each term is linked to a module through a rdfs:isDefineBy property",
        "errors": {
            "no-reference-module": {
              "pass_title": "Any term is referenced",
              "pass_description": "Each term of the test subject is linked to a module by a rdfs:isDefinedBy property",
              "fail_title": "Term not referenced to a module",
              "is_blocking": False
            }
        }
    },
    "domain-and-range-referencing-test": {
        "title": "Domain or range out of vocabulary",
        "description": "Test checking if each range of domain of any property is defined within the fragment",
        "errors": {
            "domain-out-of-vocabulary": {
              "pass_title": "Domains properly defined",
              "pass_description": "Each rdfs:domain is defined within the fragment",
              "fail_title": "Domain out of vocabulary",
              "is_blocking": False
            },
            "range-out-of-vocabulary": {
              "pass_title": "Ranges properly defined",
              "pass_description": "Each rdfs:range is defined within the fragment",
              "fail_title": "Range out of vocabulary",
              "is_blocking": False
            }
        }
    },
    "terms-differenciation-test": {
        "title": "Test of terms differenciation",
        "description": "Test checking if each term of the subject have a Levenshtein distance high enough from each other",
        "errors": {
          "too-close-terms": {
            "pass_title": "Terms differenciated enough",
            "pass_description": "All the terms have have a satisfying Levenshtein distance from each other term.",
            "fail_title": "Too close terms",
            "is_blocking": False
          }
        }
    },
    "syntax-test": {
        "title": "Syntax test",
        "description": "A test meant to check wether the test subject is syntaxically correct or not.",
        "errors": {
            "syntax-error": {
              "pass_title": "Correct syntax",
              "pass_description": "Test subject has a correct syntax",
              "fail_title": "Test subject has syntax errors",
              "is_blocking": True
            }
        }
    },
    "owl-rl-constraint-test": {
        "title": "OWL RL Constraint violation test",
        "description": "A test meant to check if a OWL RL constraint is violated",
        "errors": {
            "owl-rl-constraint-violation": {
              "pass_title": "OWL RL consistent",
              "pass_description": "The provided graph is consistent for any OWL RL constraint",
              "fail_title": "OWL RL Constraint violation",
              "is_blocking": True
            }
        }
    },
    "profile-test": {
      "title": "OWL Profile Compatibility Test",
      "description": "Test for the compatibility of the subject for the OWL Profile",
      "errors": {}
    }
}

for profile in DECIDABILITY_RANGE:
  profile_id = profile.lower().replace('_', '-')
  spaced_name = profile.replace('_', ' ')
  TEST_RESOURCES["profile-test"]["errors"][f"{profile_id}-profile-error"] = {
    "pass_title": f"{spaced_name} Profile compatible",
    "pass_description": f"The subject is included in the {spaced_name} sublanguage",
    "fail_title": f"{spaced_name} Profile incompatible",
    "is_blocking": False
  }

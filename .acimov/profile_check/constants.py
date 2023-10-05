import regex as re

##############
# Parameters #
##############

# The ontology base URL
ONTOLOGY_URL = "https://purl.org/hmas/"
# The relative path to the src folder
SRC_PATH = "../../src/"
# The relative path to the domains folder
DOMAINS_PATH = "../../domains/"
# The URL of the Corese python library to fetch
CORESE_PYTHON_URL = "https://files.inria.fr/corese/distrib/corese-library-python-4.4.1.jar"
# The desired levenshtein threshold to accept terms as different enough
TERM_DISTANCE_THRESHOLD = 3

############################################
# Constants calculated from the parameters #
############################################

# The character separating the ontology base URL from the suffix
ONTOLOGY_SEPARATOR = ONTOLOGY_URL[-1]
# The corese python executable name
CORESE_JAR_NAME = CORESE_PYTHON_URL.split('/')[-1]

# Format of a syntax error in the console
AST_ERROR_FORMAT = re.compile("ERROR fr\\.inria\\.corese\\.sparql\\.triple\\.parser\\.ASTQuery")

# Glob path to modules
MODULES_TTL_GLOB_PATH = f"{SRC_PATH}*.ttl"
# Glob path to modelets
MODELETS_TTL_GLOB_PATH = f"{DOMAINS_PATH}*/*/onto.ttl"

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

SELECT DISTINCT ?property WHERE {
  ?property rdf:type owl:ObjectProperty .
  ?property rdfs:domain ?domain .
   
   FILTER NOT EXISTS {
    ?domain rdf:type ?o .
    FILTER(strstarts(str(?domain), "ONTOLOGY_URL"))
  }
  FILTER(strstarts(str(?property), "ONTOLOGY_URL"))
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
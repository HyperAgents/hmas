import regex as re

ONTOLOGY_URL = "https://purl.org/hmas/"
SRC_PATH = "../../src/"
DOMAINS_PATH = "../../domains/"
CORESE_PYTHON_URL = "https://files.inria.fr/corese/distrib/corese-library-python-4.4.1.jar"

ONTOLOGY_SEPARATOR = ONTOLOGY_URL[-1]
CORESE_JAR_NAME = CORESE_PYTHON_URL.split('/')[-1]

AST_ERROR_FORMAT = re.compile("ERROR fr\\.inria\\.corese\\.sparql\\.triple\\.parser\\.ASTQuery")

SRC_TTL_GLOB = f"{SRC_PATH}*.ttl"
DOMAINS_TTL_GLOB = f"{DOMAINS_PATH}*/*/onto.ttl"

NOT_REFERENCED = """
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

SELECT DISTINCT ?s where {
  ?s ?p ?o .
  FILTER(strstarts(str(?s), "ONTOLOGY_URL"))
  FILTER NOT EXISTS { ?s rdfs:isDefinedBy [] . }
  FILTER NOT EXISTS { ?s rdf:type owl:Ontology . }
  FILTER NOT EXISTS { ?s rdf:type skos:Concept . }
}
""".replace("ONTOLOGY_URL", ONTOLOGY_URL)

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

DOMAIN_OUT_Of_VOCABULARY = """
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

SELECT DISTINCT ?property WHERE {
  ?property rdf:type owl:ObjectProperty .
  ?property rdfs:domain ?domain .
   
   FILTER NOT EXISTS {
    ?domain rdf:type ?o .
  }
  FILTER(strstarts(str(?property), "ONTOLOGY_URL"))
}
""".replace("ONTOLOGY_URL", ONTOLOGY_URL)

RANGE_OUT_OF_VOCABULARY = DOMAIN_OUT_Of_VOCABULARY.replace("rdfs:domain", "rdfs:range")

GET_IMPORTS = """
SELECT DISTINCT ?i WHERE {
  ?s rdf:type owl:Ontology ;
  owl:imports ?i .
}
"""

"""
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

SELECT DISTINCT ?property WHERE {
  {
    ?property rdf:type owl:ObjectProperty .
    ?property rdfs:domain ?domain .
    FILTER(strstarts(str(?property), "ONTOLOGY_URL"))
  }
  UNION
  {
  
  }
}
"""
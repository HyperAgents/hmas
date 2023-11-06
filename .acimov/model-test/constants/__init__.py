from json import load
from os.path import sep

from .parameters import *
from .paths import *

from .corese_info import *
from .git_info import *
from .sparql import *

from .rdflib_info import *

__all__ = ["parameters", "paths", "corese_info", "git_info", "sparql", "rdflib_info"]

from .parameters import ONTOLOGY_URL, BLOCKING_ERRORS
from .paths import PWD_TO_MODEL_TEST

# The character separating the ontology base URL from the suffix
ONTOLOGY_SEPARATOR = ONTOLOGY_URL[-1]

TEST_RESOURCES = None
with open(f"{PWD_TO_MODEL_TEST}constants{sep}tests-resources.json", "r") as f:
  TEST_RESOURCES = load(f)

for criterion in TEST_RESOURCES.keys():
  criterion_resource = TEST_RESOURCES[criterion]
  for error in criterion_resource["errors"].keys():
    error_resource = criterion_resource["errors"][error]
    error_resource["blocking"] = error in BLOCKING_ERRORS

CRITERIONS_NEEDING_SYNTAX = [
  criterion for criterion in TEST_RESOURCES.keys()
  if not criterion == "syntax-test"
]

BEST_PRACTICES_TESTS = [
  criterion for criterion in CRITERIONS_NEEDING_SYNTAX
  if not criterion in ["syntax-test", "owl-rl-constraint-test", "profile-test"]
]
from subprocess import check_output
from os.path import relpath

from .paths import ROOT_FOLDER

# The reository URI
REPO_URI = check_output(
  "git config --get remote.origin.url".split(" ")
  )\
  .decode('utf-8')\
  .strip()

# Base reporitory platform URL
PLATFORM_URL = "/".join(REPO_URI.split("/")[:-2])

# The current branch
BRANCH = check_output(
  "git rev-parse --abbrev-ref HEAD".split(" ")
  )\
  .decode('utf-8')\
  .strip()

# The relative path from root to the profile_test folder
PATH_TO_PROFILE_FOLDER = relpath(".", ROOT_FOLDER)

# The path to the profile check README.md
PROFILE_CHECK_URI = f"{REPO_URI}tree/{BRANCH}/{PATH_TO_PROFILE_FOLDER}"
  # TODO: Should be manual/precommit/actions compatible
  # git config --get remote.origin.url for precommit/manual
  # $GITHUB_SERVER_URL + '/' + $GITHUB_REPOSITORY for action

DEV_USERNAME = check_output(
  "git config --global user.name".split(" ")
  )\
  .decode('utf-8')\
  .strip()

ACIMOV_MODEL_TEST_URI = f"{PROFILE_CHECK_URI}/model-test-onto.ttl"
# URL prefix for the files in the current branch in src
SRC_URL = f"{REPO_URI}blob/{BRANCH}/src/"
DOMAINS_URL = SRC_URL.replace("src", "domains")
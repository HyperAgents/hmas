from subprocess import check_output
from os.path import relpath, sep

from .paths import ROOT_FOLDER

from sys import argv

# The repository URI
arg_repo = [item.split("=")[1] for item in argv if item.startswith("--REPO_URI=")]
REPO_URI = arg_repo[0] if len(arg_repo) > 0 else check_output(
  "git config --get remote.origin.url".split(" ")
)\
.decode('utf-8')\
.strip()

if REPO_URI.endswith("/"):
  REPO_URI = REPO_URI[:-1]

# Base reporitory platform URL
PLATFORM_URL = "/".join(REPO_URI.split("/")[:-2])

# The current branch
arg_branch = [item.split("=")[1] for item in argv if item.startswith("--BRANCH=")]
BRANCH = arg_branch[0] if len(arg_branch) > 0 else check_output(
  "git rev-parse --abbrev-ref HEAD".split(" ")
)\
.decode('utf-8')\
.strip()

# The relative path from root to the profile_test folder
PATH_TO_PROFILE_FOLDER = relpath(".", ROOT_FOLDER)

IS_PROFILE_FOLDER_PWD = PATH_TO_PROFILE_FOLDER == "." or PATH_TO_PROFILE_FOLDER == f".{sep}"

# The path to the profile check README.md
PROFILE_CHECK_URI = f"{REPO_URI}/blob/{BRANCH}/{'' if IS_PROFILE_FOLDER_PWD else PATH_TO_PROFILE_FOLDER}"

arg_dev_username = [item.split("=")[1] for item in argv if item.startswith("--DEV_USERNAME=")]
DEV_USERNAME = arg_dev_username[0] if len(arg_dev_username) > 0 else check_output(
  "git config --global user.name".split(" ")
)\
.decode('utf-8')\
.strip()


ACIMOV_MODEL_TEST_URI = f"{PROFILE_CHECK_URI}.acimov/model-test/model-test-onto.ttl"
# URL prefix for the files in the current branch in src
SRC_URL = f"{REPO_URI}blob/{BRANCH}/src/"
DOMAINS_URL = SRC_URL.replace("src", "domains")

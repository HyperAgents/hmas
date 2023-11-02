from json import dumps
from glob import glob
from datetime import datetime
from os import makedirs
from os.path import sep, exists
from sys import argv

from constants import (
    MODULES_TTL_GLOB_PATH,
    MODELETS_TTL_GLOB_PATH,
    DEV_USERNAME,
    PWD_TO_PROFILE_CHECK,
    PWD_TO_MODEL_OUTPUT_FOLDER
)

from corese import print_title # TODO Need later for a utils.py?

from testing import (
    modules_tests,
    modelets_tests,
    merged_fragment_set_test,
)

from parsing import parse_report_to_turtle

###
# Test OWL_RL
###
_, *args = argv

modes = [
    item.split('=')[1]
    for item in args
    if item.startswith("--name=")
]

mode = modes[0] if len(modes) > 0 else "manual"

print_title("Checking existing modules")
modules = glob(MODULES_TTL_GLOB_PATH)
modules_report, unsafe_modules = modules_tests(modules)

print_title("Checking modelets")
modelets = glob(MODELETS_TTL_GLOB_PATH)
modelets_report, unsafe_modelets = modelets_tests(modelets)

print_title("Checking the merge of safe modules")
safe_modules = [
    module for module in modules
    if not module in unsafe_modules
]
safe_modules_report = merged_fragment_set_test(safe_modules, "all-modules")

print_title("Checking the merge of safe fragments")
fragments = modules + modelets
unsafe_fragments = unsafe_modules + unsafe_modelets

safe_fragment = [
    fragment for fragment in fragments
    if not fragment in unsafe_fragments
]
safe_fragments_report = merged_fragment_set_test(safe_fragment, "all-fragments")

report = modules_report + modelets_report + safe_modules_report + safe_fragments_report

file_name = ""
if mode == "manual":
    now = ".".join(
            datetime\
            .now()\
            .isoformat()\
            .split(".")[:-1]
        ).replace(":", "-")
    file_name = f"{mode}-{DEV_USERNAME}-{now}"
else:
    file_name = mode

if not exists(PWD_TO_MODEL_OUTPUT_FOLDER):
    makedirs(PWD_TO_MODEL_OUTPUT_FOLDER)

with open(f"{PWD_TO_MODEL_OUTPUT_FOLDER}{file_name}.json", 'w') as f:
    f.write(dumps(report, indent=4))

turtle = parse_report_to_turtle(
    report,
    mode,
    skip_pass="--skip-pass" in args
)

with open(f"{PWD_TO_MODEL_OUTPUT_FOLDER}{file_name}.ttl", "w") as f:
    f.write(turtle)
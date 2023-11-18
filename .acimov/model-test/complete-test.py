from glob import glob
from datetime import datetime
from os import makedirs
from os.path import exists
from sys import argv

from constants import (
    MODULES_TTL_GLOB_PATH,
    MODELETS_TTL_GLOB_PATH,
    DEV_USERNAME,
    PWD_TO_MODEL_OUTPUT_FOLDER,
    PROFILE_CHECK_URI,
    BRANCH
)

from corese import print_title # TODO Need later for a utils.py?

from testing import (
    modules_tests,
    modelets_tests,
    merged_fragment_set_test,
)

from turtle import (
    prepare_graph,
    make_assertor
)

from markdown import (
    make_turtle_page
)

def datetime_id():
    return ".".join(
            datetime\
            .now()\
            .isoformat()\
            .split(".")[:-1]
        ).replace(":", "-")

###
# Test OWL_RL
###
_, *args = argv

modes = [
    item.split('=')[1]
    for item in args
    if item.startswith("--mode=")
]

names = [
    item.split('=')[1]
    for item in args
    if item.startswith("--dev=")
]

skip_pass = "--skip-pass" in args
tested_only = "--tested-only" in args

dev = names[0] if len(names) > 0 else DEV_USERNAME
mode = modes[0] if len(modes) > 0 else "manual"

report = prepare_graph()
test_assertor = make_assertor(
    report,
    mode,
    f"{PROFILE_CHECK_URI}.acimov/model-test/complete-test.py",
    dev=dev
)

print_title("Checking existing modules")
modules = glob(MODULES_TTL_GLOB_PATH)
unsafe_modules = modules_tests(modules, report, test_assertor, skip_pass=skip_pass, tested_only=tested_only)

print_title("Checking modelets")
modelets = glob(MODELETS_TTL_GLOB_PATH)
unsafe_modelets = modelets_tests(modelets, report, test_assertor, skip_pass=skip_pass, tested_only=tested_only)

print_title("Checking the merge of safe modules")
safe_modules = [
    module for module in modules
    if not module in unsafe_modules
]
merged_fragment_set_test(
    report,
    test_assertor,
    safe_modules,
    "all-modules",
    skip_pass=skip_pass,
    tested_only=tested_only,
    custom_title=f"All the modules from branch {BRANCH} that are syntaxically correct as well as their recursive imports"    
)

print_title("Checking the merge of safe fragments")
fragments = modules + modelets
unsafe_fragments = unsafe_modules + unsafe_modelets

safe_fragment = [
    fragment for fragment in fragments
    if not fragment in unsafe_fragments
]
merged_fragment_set_test(
    report,
    test_assertor,
    safe_fragment,
    "all-fragments",
    skip_pass=skip_pass,
    tested_only=tested_only,
    custom_title=f"All the fragments from branch {BRANCH} that are syntaxically correct as well as their recursive imports"  
)

file_name = mode if not mode == "manual" else f"{mode}-{dev}-{datetime_id()}"
file_base = f"{PWD_TO_MODEL_OUTPUT_FOLDER}{file_name}"

print_title("Exporting results")

if not exists(PWD_TO_MODEL_OUTPUT_FOLDER):
    makedirs(PWD_TO_MODEL_OUTPUT_FOLDER)

with open(f"{file_base}.ttl", "w") as f:
    f.write(report.serialize(format="ttl"))

with open(f"{file_base}.md", "w") as f:
    f.write(make_turtle_page(report, file_name))
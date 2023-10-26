from json import dumps
from glob import glob
from datetime import datetime
from os.path import sep

from constants import (
    MODULES_TTL_GLOB_PATH,
    MODELETS_TTL_GLOB_PATH,
    DEV_USERNAME,
    PWD_TO_PROFILE_CHECK
)

from corese import print_title # TODO Need later for a utils.py?

from testing import (
    modules_tests,
    modelets_tests,
    global_test
)

from parsing import parse_report_to_turtle

###
# Test OWL_RL
###

safe_modules = glob(MODULES_TTL_GLOB_PATH)
print_title("Profile check")
print_title("Checking existing modules")
modules_report, safe_modules = modules_tests(safe_modules)

print_title("Checking modelets")
safe_modelets = glob(MODELETS_TTL_GLOB_PATH)
modelets_report, safe_modelets = modelets_tests(safe_modelets)

safe_graphs = safe_modules + safe_modelets
print_title("Checking the all the modules and modelets together")
global_report = global_test(safe_graphs)


report = modules_report + modelets_report + global_report

now = '.'.join(datetime.now().isoformat().split('.')[:-1]).replace(':', '-')

file_name = f"manual-{DEV_USERNAME}-{now}"

with open(f"{PWD_TO_PROFILE_CHECK}{sep}output/{file_name}.json", 'w') as f:
    f.write(dumps(report, indent=4))


turtle = parse_report_to_turtle(report)

with open(f"{PWD_TO_PROFILE_CHECK}{sep}output/{file_name}.ttl", "w") as f:
    f.write(turtle)

from json import dumps
from glob import glob

from constants import (
    MODULES_TTL_GLOB_PATH,
    MODELETS_TTL_GLOB_PATH
)

from corese import print_title # TODO Need later for a utils.py?

from testing import (
    modules_tests,
    modelets_tests,
    best_practices_tests,
)

from parsing import parse_report_to_turtle

###
# Test OWL_RL
###

safe_modules = glob(MODULES_TTL_GLOB_PATH)
print_title("Profile check")
print_title("Checking existing modules")
base_modules_report, safe_modules = modules_tests(safe_modules)

print_title("Checking modelets")
safe_modelets = glob(MODELETS_TTL_GLOB_PATH)
modelets_report, safe_modelets = modelets_tests(safe_modelets)

print_title("Checking best practices")
best_practices_reports = best_practices_tests(safe_modules, safe_modelets)
report = {
    "base_modules": base_modules_report,
    "modelets": modelets_report, 
    "best_practices": best_practices_reports
}

turtle = parse_report_to_turtle(report)

with open("report.json", 'w') as f:
    f.write(dumps(report, indent=4))

with open("turtle_report.ttl", "w") as f:
    f.write(turtle)
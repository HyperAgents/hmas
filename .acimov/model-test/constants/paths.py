from os import getcwd
from os.path import sep, relpath, abspath

##################
# Relative paths #
##################

ROOT_FOLDER = abspath(
  f"{sep.join(abspath(__file__).split(sep)[:-1])}{sep}..{sep}..{sep}..{sep}"
)

PWD_TO_ROOT_FOLDER = f"{relpath(ROOT_FOLDER, getcwd())}{sep}"
PWD_TO_MODEL_OUTPUT_FOLDER = f"{PWD_TO_ROOT_FOLDER}.acimov{sep}output{sep}"
PWD_TO_MODEL_TEST = f"{PWD_TO_ROOT_FOLDER}.acimov{sep}model-test{sep}"
MODULES_TTL_GLOB_PATH = f"{PWD_TO_ROOT_FOLDER}src{sep}*.ttl"
MODELETS_TTL_GLOB_PATH = f"{PWD_TO_ROOT_FOLDER}domains{sep}*{sep}*{sep}onto.ttl"
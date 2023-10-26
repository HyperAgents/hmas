from os import system
from os.path import sep, abspath

from pre_commit import output

script_folder_path = sep.join(abspath(__file__).split(sep)[:-1])


with open(f"{script_folder_path}{sep}requirements.txt", "r") as requirements:
    dependencies = requirements.readlines()
    dependencies = [item.strip() for item in dependencies]

    for dependency in dependencies:
        system(f"python -m pip install -q {dependency}")

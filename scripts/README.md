# Scripts folder

This folder contains scripts that are used to check the quality of the ontology, generate the html documentation, and ultimately build the `public` folder that contains the documentation website of the ontologies.

## Get started

To execute the scripts, you need python 3, and the requirements in `scripts/requirements.txt`.
Best is to create a virtual environment 

```
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r scripts/requirements.txt
```

## Run the script

Don't forget to activate the virtual environment for each session.

```
source .venv/bin/activate
```

Then call the script:

```
scripts/process_core.py
```


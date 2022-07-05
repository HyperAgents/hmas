#!/usr/bin/env python3
import os
import mistune

############################################################ assertions to check

def test_scenario_title(m):
    assert "name" in m, ("must", "The scenario has a title")

def test_scenario_desc(m):
    assert "description" in m, ("must", "The scenario has a description")

def test_scenario_cq(m):
    assert len(m["questions"]) > 0, ("must", "The scenario addresses at least one competency question")

def test_scenario_term(m):
    # TODO add check that the term is in onto.ttl
    assert len(m["terms"]) > 0, ("must", "The scenario introduces at least one term")

def test_scenario_tbox(m):
    p = m["path"]
    assert os.path.exists(f"{p}/onto.ttl"), ("must", "The scenario has ontological definitions")

def test_scenario_abox(m):
    p = m["path"]
    assert os.path.exists(f"{p}/dataset.ttl"), ("must", "The scenario has an example dataset")

def test_q_sparql(m, q):
    p = m["path"]
    assert os.path.exists(f"test/{p}/{q}.rq"), ("must", "The competency question is formalized as a SPARQL query")

def test_scenario_eval(m):
    # TODO rdflib call
    assert True, ("must", "The SPARQL query evaluates to 'true' for the scenario's dataset")

def test_scenario_cqs(m):
    assert len(m["questions"]) > 1, ("should", "The feature addresses more than one competecy question")

def test_scenario_terms(m):
    assert len(m["terms"]) > 1, ("should", "The feature introduces more than one term")

def test_term_scenarios(t):
    # TODO
    assert True, ("should", "The ontology term is defined in only one scenario")

def test_term_scenario(t):
    # TODO
    assert True, ("must", "The ontology term is referenced in at least one scenario")

test_scenario = [
    test_scenario_title,
    test_scenario_desc,
    test_scenario_cq,
    test_scenario_term,
    test_scenario_tbox,
    test_scenario_abox,
    test_scenario_eval,
    test_scenario_cqs
]

test_q = [
    test_q_sparql
]

test_dom = [
    # TODO if domain has name and desc
    # TODO test if domain has at least one motivating scenario (feature)
]

test_term = [
    test_term_scenario,
    test_term_scenarios
]

############################################################# checking procedure

# TODO as HTML instead?
def get_text(ast):
    if "children" not in ast:
        # text or codespan
        return ast["text"]
    else:
        text = ""
        for child in ast["children"]:
            text += get_text(child)
        return text

def find_section(ast, title, level=2):
    for (i, item) in enumerate(ast):
        if item["type"] == "heading" \
        and item["level"] == level \
        and item["children"][0]["text"] == title \
        and len(ast) > i+1:
            return ast[i+1]
    return None

def parse_domain(dom):
    # TODO
    return NotImplemented

def parse_scenario(sc):
    m = {
        "id": sc.name,
        "path": sc.path,
        "name": None,
        "description": None,
        "questions": [],
        "terms": []
    }

    f = f"{sc.path}/README.md"

    if not os.path.exists(f):
        return m

    get_ast = mistune.create_markdown(renderer='ast', plugins=['table'])
    md = open(f, "r").read()
    ast = get_ast(md)

    # first element is the name of the feature
    if ast[0]["type"] == "heading" and ast[0]["level"] == 1:
        m["name"] = get_text(ast[0])

    # second element is the description of the feature
    descItem = find_section(ast, "Description")
    if descItem is not None and descItem["type"] == "paragraph":
        m["description"] = get_text(descItem)

    # next elements are competency questions
    qItem = find_section(ast, "Competency Questions")
    if qItem is not None and qItem["type"] == "table":
        for (i, item) in enumerate(qItem["children"][1]["children"]):
            if len(item["children"]) == 2:
                id = get_text(item["children"][0])
                m["questions"].append(id)
            else:
                m["questions"].append(None)

    # next element is the glossary
    glossaryItem = find_section(ast, "Glossary")
    if glossaryItem is not None and glossaryItem["type"] == "list":
        for item in glossaryItem["children"]:
            t = {}
            if len(item["children"]) == 1 and item["children"][0]["type"] == "block_text":
                t["label"] = get_text(item["children"][0]["children"][0])
            if len(item["children"][0]["children"]) > 0 and item["children"][0]["children"][0]["type"] == "link":
                t["ref"] = item["children"][0]["children"][0]["link"]
            m["terms"].append(t)

    return m

report = []

def is_dir(f): return f.is_dir()

for dom in filter(is_dir, os.scandir("domains")):
    for sc in filter(is_dir, os.scandir(dom.path)) :
        modelet = parse_scenario(sc)

        for test in test_scenario:
            try:
                test(modelet)
            except AssertionError as a:
                report.append((sc.name, a))

for error in report:
    print(error)

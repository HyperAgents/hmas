#!/usr/bin/env python3
import os
import mistune

############################################################ assertions to check

def test_feat_name(m):
    assert "name" in m, ("must", "The feature has a name")

def test_feat_desc(m):
    assert "description" in m, ("must", "The feature has a description")

def test_feat_dom(m):
    assert len(m["domains"]) > 0, ("must", "The feature references at least one domain")

def test_feat_cq(m):
    assert len(m["questions"]) > 0, ("must", "The feature addresses at least one competency question")

def test_feat_term(m):
    # TODO add check that the term is referenced
    assert len(m["terms"]) > 0, ("must", "The feature introduces at least one term")

def test_feat_cbox(m):
    id = m["id"]
    assert os.path.exists(f"test/{id}/abox.ttl") and os.path.exists(f"test/{id}/tbox.ttl"), ("must", "The feature has a TBox and an example ABox")

def test_q_sparql(m, q):
    id = m["id"]
    assert os.path.exists(f"test/{id}/{q}.rq"), ("must", "The competency question is formalized as a SPARQL query")

def test_feat_eval(m):
    # TODO rdflib call
    assert True, ("must", "The SPARQL query evaluates to the expected answer for the feature's TBox and ABox")

def test_feat_doms(m):
    assert len(m["domains"]) > 1, ("should", "The feature references more than one domains")

def test_feat_cqs(m):
    assert len(m["questions"]) > 1, ("should", "The feature addresses more than one competecy question")

def test_feat_terms(m):
    assert len(m["terms"]) > 1, ("should", "The feature introduces more than one term")

def test_term_feats(t):
    # TODO
    assert True, ("should", "The term is defined in only one feature")

def test_term_feat(t):
    # TODO
    assert True, ("must", "The term is referenced in at least one feature")

def test_dom_feat_ref(dom, m):
    # TODO
    assert True, ("must", "The domain has at least one motivating scenario for the ontology feature")

test_feat = [
    test_feat_name,
    test_feat_desc,
    test_feat_dom,
    test_feat_cq,
    test_feat_term,
    test_feat_cbox,
    test_feat_eval,
    test_feat_doms,
    test_feat_cqs
]

test_q = [
    test_q_sparql
]

test_dom = [
    # TODO if domain has name and desc
    # TODO test if domain has at least one motivating scenario (feature)
]

test_term = [
    test_term_feat,
    test_term_feats
]

test_dom_feat = [
    test_dom_feat_ref
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

def parse_modelet(feat):
    m = {
        "id": feat,
        "name": None,
        "description": None,
        "domains": [],
        "questions": [],
        "terms": []
    }

    f = f"test/{feat}/modelet.md"

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

    # next elements are references to domain
    exItem = find_section(ast, "Examples")
    if exItem is not None and exItem["type"] == "list":
        for (i, item) in enumerate(exItem["children"]):
            ex = {}
            if len(item["children"]) == 1 and item["children"][0]["type"] == "block_text":
                ex["label"] = get_text(item["children"][0]["children"][0])
            if len(item["children"][0]["children"]) == 1 and item["children"][0]["children"][0]["type"] == "link":
                ex["ref"] = item["children"][0]["children"][0]["link"]
            m["domains"].append(ex)

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

for feat in os.listdir("test"):
    m = parse_modelet(feat)

    for test in test_feat:
        try:
            test(m)
        except AssertionError as a:
            report.append((feat, a))

for error in report:
    print(error)

# TODO tests in /scenarios and /src directory
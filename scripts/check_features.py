#!/usr/bin/env python3
import os
import traceback
import mistune

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

# TODO pre-process AST to create sections?
# TODO more generic function that takes an AST template?
def find_section(ast, title):
    for (i, item) in enumerate(ast):
        if item["type"] == "heading" \
        and item["level"] == 2 \
        and item["children"][0]["text"] == title \
        and len(ast) > i+1:
            return ast[i+1]
    raise ValueError

def build_modelet(feat):
    get_ast = mistune.create_markdown(renderer='ast', plugins=['table'])
    md = open(f"test/{feat}/modelet.md", "r").read()
    ast = get_ast(md)

    m = {}
    m["errors"] = []

    # TODO generic function to manage errors

    # first element is the name of the feature
    try:
        assert ast[0]["type"] == "heading" and ast[0]["level"] == 1
        m["name"] = get_text(ast[0])
    except AssertionError:
        m["errors"].append({ "element": "title", "cause": "ill-formed" })

    # second element is the description of the feature
    try:
        descItem = find_section(ast, "Description")
        assert descItem["type"] == "paragraph"
        m["description"] = get_text(descItem)
    except ValueError:
        m["errors"].append({ "element": "description", "cause": "missing" })
    except AssertionError:
        m["errors"].append({ "element": "description", "cause": "ill-formed" })

    # next elements are references to domain
    try:
        exItem = find_section(ast, "Examples")
        assert exItem["type"] == "list"
        m["domains"] = []
        for (i, item) in enumerate(exItem["children"]):
            try:
                assert len(item["children"]) == 1 and item["children"][0]["type"] == "block_text"
                assert len(item["children"][0]["children"]) == 1 and item["children"][0]["children"][0]["type"] == "link"
                ref = item["children"][0]["children"][0]["link"]
                label = get_text(item["children"][0]["children"][0])
                m["domains"].append({ "ref": ref, "label": label })
            except AssertionError:
                m["errors"].append({ "element": f"example {i}", "cause": "ill-formed" })
    except ValueError:
        m["errors"].append({ "element": "examples", "cause": "missing" })
    except AssertionError:
        m["errors"].append({ "element": "examples", "cause": "ill-formed" })

    # next elements are competency questions
    try:
        qItem = find_section(ast, "Competency Questions")
        assert qItem["type"] == "table"
        m["questions"] = []
        for (i, item) in enumerate(qItem["children"][1]["children"]):
            try:
                assert len(item["children"]) == 2
                id = get_text(item["children"][0])
                m["questions"].append(id)
            except AssertionError:
                m["errors"].append({ "element": f"competency question {i}", "cause": "ill-formed" })
    except ValueError:
        m["errors"].append({ "element": "competency questions", "cause": "missing" })
    except AssertionError:
        m["errors"].append({ "element": "competency questions", "cause": "ill-formed" })

    # next element is the glossary
    try:
        glossaryItem = find_section(ast, "Glossary")
        assert glossaryItem["type"] == "list"
        m["terms"] = []
        for item in glossaryItem["children"]:
            try:
                assert len(item["children"]) == 1 and item["children"][0]["type"] == "block_text"
                assert len(item["children"][0]["children"]) > 0 and item["children"][0]["children"][0]["type"] == "link"
                ref = item["children"][0]["children"][0]["link"]
                label = get_text(item["children"][0]["children"][0])
                m["terms"].append({ "ref": ref, "label": label })
            except AssertionError:
                m["errors"].append({ "element": f"term {i}", "cause": "ill-formed" })
    except ValueError:
        m["errors"].append({ "element": "terms", "cause": "missing" })
    except AssertionError:
        m["errors"].append({ "element": "terms", "cause": "ill-formed" })

    return m

for feat in os.listdir("test"):
    dir = f"test/{feat}/"

    # # every feature should be described in a modelet
    # assert os.path.exists(dir + "modelet.md")
    # # every feature should be associated with an ABox and a TBox
    # assert os.path.exists(dir + "abox.ttl")
    # assert os.path.exists(dir + "tbox.ttl")
    # # every feature should be associated with a query
    # # TODO don't hardcode 'q1'
    # assert os.path.exists(dir + "q1.rq")

    try:
        m = build_modelet(feat)
        print(feat)
        print(m)
        print("\n")
    except Exception as e:
        print(feat + " is invalid")
        traceback.print_exc()

# every domain must have one motivating scenario for some feature
# every motivating scenario must be associated with a modelet
# every modelet must reference one or more scenarios
# every modelet must include one or more competency questions (with query and answer set)
# every modelet must include a TBox and an ABox
# every query evaluation must equal the expected answer against the TBox and ABox
# every modelet must reference one or more terms in a vocabulary included in the repository [to relax?]
# every term must be referenced by one or more modelets

# every modelet should refer to more than one scenario
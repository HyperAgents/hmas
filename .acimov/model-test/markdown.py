from rdflib import Graph, Literal
from datetime import datetime
from constants import (
    SEVERITY_RANGE,
    COLOR_BOX_TEMPLATE,
    ERROR_TABLE_HEADER,
    GET_ASSERTOR_DETAILS,
    PWD_TO_MODEL_TEST_ONTO,
    GET_CRITERION_DATA,
    GET_DETAILED_ASSERTIONS,
    GET_ASSERTION_PARTS,
    GET_ASSERTION_POINTERS,
    MODULE_URL_FORMAT,
    MODELET_URL_FORMAT
)

def parse_assertions(report):
    assertions = [assertion for assertion in report.query(GET_DETAILED_ASSERTIONS)]
    severities = set([str(severity[0]) for severity in SEVERITY_RANGE])
    assertions = {
        severity: [
            assertion
            for assertion in assertions
            if str(assertion[4]).split("#")[-1] == severity
        ]
        for severity in severities
    }

    all_parts = report.query(GET_ASSERTION_PARTS)
    subjectIds = set([str(line[0]) for line in all_parts])
    partsDict = {
        subjectId: [
            str(line[1]) for line in all_parts
            if str(line[0]) == subjectId
        ]
        for subjectId in subjectIds
    }

    all_pointers = report.query(GET_ASSERTION_POINTERS)
    outcomeIds = set([str(line[0]) for line in all_pointers])
    pointersDict = {
        outcomeId: [
            line[1] for line in all_pointers
            if str(line[0]) == outcomeId
        ]
        for outcomeId in outcomeIds
    }
    return assertions, partsDict, pointersDict

def parseCriterions():
    criterions = Graph()
    criterions.parse(PWD_TO_MODEL_TEST_ONTO)
    criterions = criterions.query(GET_CRITERION_DATA)
    criterions = {
        str(criterion[0]): {
            "title": str(criterion[1]),
            "description": str(criterion[2])
        }
        for criterion in criterions
    }
    return criterions

def title_to_id(title):
    start = 0
    while(title[start] == "#"): start += 1
    while(title[start] == " "): start += 1
    return f"#{title[start:].lower().replace(' ', '-')}"

def make_assertor_chapter(report):
    result = []

    result.append("# Test Context")
    result.append("")
    result.append("Here is some context about under which context this test was made")
    result.append("")

    assertor_info = report.query(GET_ASSERTOR_DETAILS)
    assertor_info = [x for x in assertor_info][0]

    title, description, date, script, page = assertor_info

    date = datetime.fromisoformat(str(date)).strftime("%Y-%m-%d %H:%M:%S")
    dev = page.split('/')[-1]

    description = description.replace(f"@{dev}", f"[@{dev}]({page})")
    script_name = script.split("/")[-1]

    result.append(f"|Assertor|[{dev}]({page})|")
    result.append("|----|-----|")
    result.append(f"|Title|{title}|")
    result.append(f"|Description|{description}|")
    result.append(f"|Script|[{script_name}]({script})")
    result.append(f"|Date|{date}|")

    result.append("")
    result.append("***")
    result.append("")

    return result

def get_criterions_data(criterions, id):
    data = criterions.query(GET_CRITERION_DATA.replace("ID", id))
    title, description = [x for x in data][0]
    return title, description

def subject_part_to_markdown(part):
    module_search = MODULE_URL_FORMAT.findall(part)
    if len(module_search) > 0:
        return f"[Module {module_search[0][4:]}]({part})"
    
    modelet_search = MODELET_URL_FORMAT.findall(part)
    if len(modelet_search) > 0:
        return f"[Modelet {modelet_search[0][8:]}]({part})"
    
    return part

def make_details_table(
    chapter,
    assertionInfo,
    partsDict,
    pointersDict,
    severity,
    assertion_counter,
    emoji,
    criterions
):
    _, _, _, outcome, _, subjectId, subjectTitle, criterionUri, outcomeTitle, outcomeDescription = assertionInfo
    subjectId = str(subjectId)
    outcome = str(outcome)

    parts = [part for part in partsDict.get(subjectId, [])]
    parts = [part + ("" if part.endswith(".ttl") else ".ttl") for part in parts]
    parts = [subject_part_to_markdown(part) for part in parts]
    parts = "<br/>".join([f"- {part}" for part in parts])

    criterionId = criterionUri.split('#')[-1]
    criterionTitle = criterions[criterionId]["title"]
    criterionDescription = criterions[criterionId]["description"]

    chapter += [
        f"### {severity} Assertion number {assertion_counter}",
        "",
        f"[Jump to {severity} assertions summary](#{severity.lower()}-assertions)",
        "",
        f"New {emoji}{severity} assertion"
        "",
        "#### Subject detail",
        f"|Name|{subjectId}|",
        "|----|----|",
        f"|Title|{subjectTitle}|",
        f"|Composition|{parts}|",
        "",
        "#### Criterion detail",
        f"|Identifier|[{criterionId}]({criterionUri})|",
        "|----|----|",
        f"|Title|{criterionTitle}|",
        f"|Description|{criterionDescription}|",
        "",
        "#### Outcome Detail",
        f"|Type|{emoji}{severity}|",
        "|----|----|",
        f"|Title|{outcomeTitle}|",
        f"|Description|{outcomeDescription}|"
    ]

    for rdfPointer in pointersDict.get(outcome, []):
        mdPointer = str(rdfPointer).replace("\n", "<br>")
        beforePointer = '<pre lang="rdf" style="overflow-wrap: break-word;">' if isinstance(rdfPointer, Literal) else ""
        afterPointer = "<br/></pre>" if isinstance(rdfPointer, Literal) else ""
        chapter.append(f"|Pointer|{beforePointer}{mdPointer}{afterPointer}|")

    chapter.append("")
    chapter.append("***")

def make_details_chapter(criterions, assertions, partsDict, pointersDict):
    chapter = [
        "",
        "# Assertion Details",
        "",
        "[Jump to the previous chapter](#model-test-report-review)"
        "",
        "In this chapter we will go further into each assertion",
        ""
    ]

    for severity, emoji, _ in SEVERITY_RANGE:
        severity_assertions = assertions[severity]

        if len(severity_assertions) == 0:
            continue

        chapter.append(f"## {emoji}{severity} Assertion Details")
        chapter.append("")

        for i, assertionInfo in enumerate(severity_assertions):
            make_details_table(
                chapter,
                assertionInfo,
                partsDict,
                pointersDict,
                severity,
                i + 1,
                emoji,
                criterions
            )
    
    return chapter

def make_summary_chapter(assertions):
    chapter_title = "# Model test report review"

    table_lines = []
    count_line = []

    for severity, emoji, _ in SEVERITY_RANGE:

        severity_assertions = assertions[severity]
        table_length = len(severity_assertions)
        title = f"## {severity} assertions"
        id = title_to_id(title)

        severity_lines = [
            title,
            "",
            f"[Jump to chapter start](#model-test-report-review)"
            "",
            "",
            f"{str(len(severity_assertions))} {severity} assertions",
            ""
            ] + ERROR_TABLE_HEADER + [
            "|".join([
                '',
                f"[Table top]({id})",
                f"{str(i+1)}/{str(table_length)}",
                COLOR_BOX_TEMPLATE
                    .replace('EMOJI', emoji)
                    .replace('TEXT', severity),
                f"`{str(subjectId)}`",
                f"[{criterionId.split('#')[-1]}]({criterionId})",
                str(errorTitle),
                f"[Jump](#{severity.lower()}-assertion-number-{str(i+1)})",
                ''
            ])
            for i, (_, _, _, _, _, subjectId, _, criterionId, errorTitle, _) in enumerate(severity_assertions)
        ]
        table_lines += severity_lines
        count_line.append(f"{emoji}{str(table_length)} [{severity}]({id})")

    assertions_stats = [len(assertions[key]) for key, _, _ in SEVERITY_RANGE]
    nb_assertions = sum(assertions_stats)

    severity_rates = [max(1, int(nb/nb_assertions * 100)) for nb in assertions_stats]
    severity_rates[-1] = 100 - sum(severity_rates[:-1])

    bar = '<div  style="border-radius: 12px; height: 25px; overflow: hidden">'
    for i in range(len(SEVERITY_RANGE)):
        color = SEVERITY_RANGE[i][2]
        style = f""
        if i == 0:
            style += f'border-radius: 12px 0px 0px 12px'
        if i == len(SEVERITY_RANGE) - 1:
            style += 'border-radius: 0px 12px 12px 0px'
        bar += f'<img src="https://placehold.co/15x15/{color}/{color}.png" width="{severity_rates[i]}%" height="25px" style="{style}"/>'
    bar +='</div>'

    result = [
        chapter_title,
        "",
        "[Jump to the next chapter](#assertion-details)",
        "",
        "Here is the human readable preview for the model test report",
        "",
        f"{str(nb_assertions)} Assertions"
        "",
        "",
        ", ".join(count_line),
        "",
        bar,
        "",
        ] + table_lines + ["", "***"]
    return result

def make_turtle_page(report, file_name) -> str:

    md = []

    assertions, partsDict, pointersDict = parse_assertions(report)
    criterions = parseCriterions()

    md += [
        "# Test Report Markdown export",
        "",
        "This file is an export of the RDF test report made out of [EARL vocabulary](https://www.w3.org/TR/EARL10/)",
        "",
        f"The original test report is available in turtle syntax [here](./{file_name}.ttl).",
        ""
    ]
    md += make_assertor_chapter(report)
    md += make_summary_chapter(assertions)
    md += make_details_chapter(criterions, assertions, partsDict, pointersDict)

    md = "\n".join(md)
    return md
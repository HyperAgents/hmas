#!/usr/bin/env python

import precommit_imports

from typing import Sequence
from sys import argv

from testing import modules_tests
from parsing import parse_report_to_turtle
from constants import EARL_NAMESPACE, BLOCKINGS_ERRORS
from rdflib import Graph
from rdflib.namespace import DCTERMS
from pre_commit import output

# TODO remove this
from json import dumps

def main(files: Sequence[str] | None = None):

    output.write_line(" ")
    output.write_line(f"Files staged: {' '.join(files)}")
    output.write_line(" ")

    if files is None:
        return 0

    report, _ = modules_tests(files)
    turtle = parse_report_to_turtle(report)

    graph = Graph()
    graph.bind("earl", EARL_NAMESPACE)
    graph.bind("dcterms", DCTERMS)
    graph.parse(data=turtle, format="ttl")

    blocking_errors_iterator = graph.query(BLOCKINGS_ERRORS)
    blocking_errors = [item for item in blocking_errors_iterator]

    if len(blocking_errors) == 0:
        return 0
    
    for blocking_error in blocking_errors:
        output.write_line("Blocking error")
        output.write_line(f"\tSubject: {blocking_error.n}")
        output.write_line(f"\tCriterion: {blocking_error.c.split('#')[-1]}")
        output.write_line(f"\tError name: {blocking_error.t}")
        output.write_line(f"\tError description: {blocking_error.d}")

    return 1

if __name__ == '__main__':
    _, *args = argv
    raise SystemExit(main(args))

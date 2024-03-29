#!/usr/bin/env python3
import os
import sys
import logging
import shutil
import subprocess
import rdflib
from rdflib import Graph, URIRef, Literal, BNode
from rdflib.namespace import RDF, RDFS, OWL, DCTERMS, XSD
import pylode

from pathlib import Path

logging.basicConfig(level=logging.DEBUG)

base = "https://purl.org/hmas/"

os.makedirs("public", exist_ok=True)
shutil.copytree("resources", "public", dirs_exist_ok=True)

for input_file_path in [ "src/core.ttl", "src/interaction.ttl" , "src/regulation.ttl", "src/meta.ttl", "src/fipa.ttl"]:
    input_file_path_head = input_file_path[:-4] + ".head"
    input_file_path_tail = input_file_path[:-4] + ".tail"
    dest_path = input_file_path.replace("src/" , "public/")[0:-4]

    # parse and check ttl syntax
    g = Graph()
    try:
        g.parse(input_file_path)
    except rdflib.plugins.parsers.notation3.BadSyntax as err:
        err_string = str(err).replace('\n', '\n  ')
        logging.error(f"File {dest_path} {err_string}")
        pass
#        sys.exit(1) # exit with error code if there is a parsing error

    if len(list(g.subjects(RDF.type, OWL.Ontology))) != 1: # check there is one ontology declaration
        logging.error("There MUST be exactly one triple: `?ontology rdf:type owl:Ontology`")
        pass
#        sys.exit(1) # exit with error code if there is a parsing error

    for ontology in g.subjects(RDF.type, OWL.Ontology):
        logging.debug(f"The ontology is {ontology.n3()}")
        break;

    # find when the file was first added to the git repository, and set dct:created ? 

    git_dct_created = subprocess.check_output(["git", "log", "--diff-filter=A", "--format='%ad'", "--date=short", "--", input_file_path]).decode('ascii')[1:-2]

    for dct_created in g.objects(ontology, DCTERMS.created):
        break

    try:
        dct_created
    except NameError:
        logging.debug(f"No dct:created attribute. Adding the date when {input_file_path} was first commited: {git_dct_created}")
        g.add((ontology, DCTERMS.created, Literal(git_dct_created,datatype=XSD.date)))
    else:
        if dct_created.lstrip() != git_dct_created:
            logging.debug(f"dct:created value {dct_created.n3()} is different from the date when {input_file_path} was first commited: {git_dct_created}")


    # find when the file was last changed in the git repository, and set dct:modified.

    # find when the set dct:modified automatically ?
    git_dct_modified = subprocess.check_output(["git", "log", "-1", "--format='%ad'", "--date=short", "--", input_file_path]).decode('ascii')[1:-2]
    dct_modified = Literal(git_dct_modified,datatype=XSD.date)
    if (ontology, DCTERMS.modified, dct_modified) not in g:
        g.add((ontology, DCTERMS.modified, dct_modified))
        logging.debug(f"adding last git commit date as dct:modified value: {git_dct_modified.lstrip()}")

    # generate html documentation and rdf variants
    od = pylode.OntDoc(ontology=input_file_path,language="en", icon16="hyperagent16.ico", icon32="hyperagent32.ico", css="style.css", head=input_file_path_head + ".en" + ".html", tail=input_file_path_tail + ".en" + ".html", only_defined=True)
    of = Path(dest_path+ ".en.html")
    od.make_html(of, include_css=False)

    od = pylode.OntDoc(ontology=input_file_path,language="fr", icon16="hyperagent16.ico", icon32="hyperagent32.ico", css="style.css", head=input_file_path_head + ".fr" + ".html", tail=input_file_path_tail + ".fr" + ".html", only_defined=True)
    of = Path(dest_path+ ".fr.html")
    od.make_html(of, include_css=False)
    
    shutil.copy(input_file_path, dest_path+ ".ttl")
    
    with open(dest_path+ ".rdf", "wb") as output:
        output.write(g.serialize(format='pretty-xml', encoding='utf-8'))
    with open(dest_path+ ".json-ld", "wb") as output:
        output.write(g.serialize(format='json-ld', indent=4, encoding='utf-8'))
    with open(dest_path+ ".n3", "wb") as output:
        output.write(g.serialize(format='n3', encoding='utf-8'))
    with open(dest_path+ ".nt", "wb") as output:
        output.write(g.serialize(format='nt', encoding='utf-8'))


    # append term redirections to the htaccess

    with open("public/.htaccess", "a") as f:
        definedTerms = []
        for definedTerm in g.subjects(RDFS.isDefinedBy, ontology):
            localName = str(definedTerm)[len(base):]
            if localName == '':
                continue
            definedTerms.append(localName)
        if len(definedTerms) != 0:
            f.write(f"""
RewriteCond %{{REQUEST_URI}} ^/hmas/({"|".join(definedTerms)})$
RewriteRule ^(.*)$ /hmas/{dest_path[7:]}#$1 [R=303,NE]
            """)

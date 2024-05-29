# Project Workflows

Two workflows are implemented for now:

* A deployment workflow
* A model test workflow

 Let's have more details about both of these

 ## Deployment workflow

 The deployment workflow aims to publish the ontology in various formats and provides a HTML documentation using a [modified version of PyLODE](https://github.com/HyperAgents/pyLODE)
 This workflow creates a `public` folder and does the following process for each turtle file found in `src` folder:
 * check if syntax is valid
 * check if there is one and only one ontology declaration
 * check if there is a dct:created property
     * if not, add the git creation date into the graph
 * check if there is a dct:modified property
     * if not, add thegit last modification date into the graph
 * uses the html heads and tails on top of the ontology to generate html documentation
     * this work is done in French and in English
 * the original RDF files from `src` folder are  copied into the `public` folder into all of the following formats:
     * rdf/xml
     * turtle
     * json-ls
     * n3
     * nt
 * updates a .htaccess to add the following redirection for each term `term` of the current RDF `file`:
     * `^/prefix/term` redirected to
     * `^/prefix/file#term` target URL

The `public` folder is then pushed to the target deployment server ar the url `/var/www/hmas/html`

## Model test workflow

A test is process on each of these resources:

* each of the modules found in the `src` folder
* each of the modelets found in the `domains/*/*` folders
* each module with related terms from the modelets
* all the modules merged all together
* all the modelets merged all together

The following tests are made on each of these resources:
* check of syntax
* check of owl constraint violation
* check if each rdfs:domain and rdfs:range that is written is set to a term defined in the ontology
* check if each term of the resource is different enough from each other in a spelling point of view (use of Levenshtein distance)
* check if each term has a rdfs:label property in English
* check if each termm is related to a module by a rdfs:isDefinedBy property
* check if each fragment is compatible with different OWL profiles?
    * OWL EL
    * OWL QL
    * OWL TC (not standard)
 
The result of this test is then written in two formats:
* turtle format (using [EARL](https://www.w3.org/TR/EARL10/) ontology (machine readable) in the `.acimov/output` folder
* markdown format (human readable) in the `.acimov/output` folder
* some badges are then published in the main README providing
    * Some metrics about the tests
    * The different compatibilities of the ontology

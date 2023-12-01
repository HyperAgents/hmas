<< badges ! @nico >>

# The Hypermedia Multi-Agent Systems (hMAS) Ontology 

<< Motivation: overview of the Hypermedia MAS >>

Our vision is ...  the deployment of world-wide hybrid communities of people and artificial agents on the Web. For this purpose, we are defining a new class of multi-agent systems (MAS) that are: 

1) aligned with the Web architecture to inherit the properties of the Web as a world-wide, open, and long-lived system ; 
2) transparent and accountable to support acceptance by people. 

Our systems use semantic hypermedia to enable uniform interaction among heterogeneous entities in MAS: people, artificial agents, devices, digital services, knowledge repositories, etc. We refer to this new class of Web-based MAS as Hypermedia MAS.
To undertake this investigation, HyperAgents brings together internationally recognized researchers actively contributing to research on autonomous agents and MAS, the Web architecture and the Web of Things, Semantic Web and Linked Data, and to the standardization of the Web.


## Getting started

<< overview of the ontology and definitions of the most stable important terms ?  + todo: update the figure >> 

* link to the documentation online https://purl.org/hmas/
* link to the primer

![view of the ontology](https://github.com/HyperAgents/ns.hyperagents.org/blob/master/resources/hmas-webvowl-v2.jpg)

<<overview of the modularization >>
Main modules: 
- [core](): 
- [interaction](): 
- [regulation](): 

for bugs and feature requests, please [raise an issue](issues/new) and follow the templates there


### Contributing 

### Contribute to the ontology


<< check the content of the linked file ! >>
The file [current ontology](https://github.com/HyperAgents/ns.hyperagents.org/blob/master/MODELING-ONTOLOGIES.md) describes :
* the different features of the project

If you want to contribute, please follow the [contributing file](https://github.com/HyperAgents/ns.hyperagents.org/blob/master/CONTRIBUTING.md).

## About this repository

This git repository contains the methodology and results of the ontology modelling activity of the [HyperAgent project](https://www.hyperagents.org/).
The root of the repository contains three introductory files respectively describing the code of conduct, the process for contributing and the method followed for designing this ontology.

<<overview of the repository structure: how  >>
Main modules: 
- [core](): 
- [interaction](): 
- [regulation](): 


### Top-level directory 
The repository folders both core ontology and domain-specific ontologies (blabla and blabla). Each ontology is defined in modular fashion. The overall structure is as follows.

```
📂 hmas
│
├─ 📁 core
│   ├── 📁 blabla
│   ├── 📁 ........
│   ├── 📁 blabla
│   ├── 📁 blabla
│   └── 📄 README.md
│
├─ 📁 domains
│   ├── 📁 blabla
│   ├── 📁 blabla
│   └── 📄 README.md
│
├─ 📁 .acimov ---> ideally, this folder should be deleted
│   ├── 📁 DOGenerator
│   ├── 📁 KGGenerator
│   ├── 📁 docs
│   ├── 📁 tests
│   └── 📄 README.md
│
├─ 📁 src
│
├─ 📄 README.md
│
└──🔑 LICENSE
```
### 📁 Core directory

The core directory contains the core ontology definition organized in modules. Each module folder contains: 
```
 .
 ├── 📄 onto.ttl               /* T-box
 ├── 📄 dataset.ttl            /* A-box
 ├── 🖼️ diagram.<imgFormat>    /* eg. CHOWLK diagram
 ├── ❓ cq-Q.rq                /* A set of Competency questions translated as Sparql query.
 └── 📄 readme.md
```

### 📁 Domain directory

For each application domain (bklabla/blabla), the domain folder contains the motivating scenarios (modules) illustrating the ontology use. Module folders are organized as for core ontology folder modules, with additional domain-specific definitions.

### 📁 ACIMOV scripts directory

The `.acimov` folder contains necessary [**scripts**](./.acimov/README.md) for automating ontology building: automatic integration, testing, documentation publishing,....


### Participate to the community group

blabla

## Licence

This ontology is licensed under the [CC BY 4.0 DEED license](LICENSE.md)
<< check the license metadata in the ontology corresponds to the LICENSE.md file >>

## How to Cite

Zenodo ? DOI ? github file for canonical citation CITATION.cff 

## Acknowledgments

This project was initially funded by the [HyperAgents](https://www.hyperagents.org/) project, an ANR/SNF project 

<< mention Community Group ? >>

We thank INRIA/UNISG/EMSE for supporting and hosting this project.

funding agencies 

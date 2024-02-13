# Alignment with the W3C WoT Thing Description Model

# Abstract

This document presents the correspondance between the hMAS vocabulary and the W3C Web of Things (WoT) Thing Description vocabulary [WOT-TD]. 

# Table of contents

1. [Introduction](./README.md#1-introduction)
2. [hMAS Core and WoT TD Alignment](./README.md#2-hmas-core-and-wot-td-alignment)<br/>
    2.1. [Artifacts and Things](./README.md#21-artifacts-and-things)<br/>
    2.2. [Resource Profiles and Thing Descriptions](./README.md#22-resource-profiles-and-thing-descriptions)<br/>
3. [hMAS Interaction and WoT TD Alignment](./README.md#3-hmas-interaction-and-wot-td-alignment)<br/>
    3.1. [Signifiers and Interaction Affordances](./README.md#31-signifiers-and-interaction-affordances)<br/>
       &emsp; 3.3.1. [Signified Interaction Affordances](./README.md#31-signifiers-and-interaction-affordances)<br/>
       &emsp; 3.3.2. [SHACL Action Specifications and Interaction Affordances](./README.md#31-signifiers-and-interaction-affordances)<br/>
    3.2  [Security Definitions](./README.md#32-security-definitions)<br/>
6. [SHACL and JSON Data Schema Alignment](./README.md#3-shacl-and-json-data-schema-alignment)<br/>
7. [Summary](./README.md#5-summary)
8. [Acknowledgements](./README.md#6-acknowledgements)
9. [References](./README.md#7-references)



# 1. Introduction

# 2. hMAS Core and WoT TD Alignment
## 2.1 Artifacts and Things
A WoT Thing is a subclass of hmas:Artifact
(insert RDF of subclassing)

## 2.2 Resource Profiles and Thing Descriptions
A WoT Thing is a subclass of hMAS Artifact whose hMAS Resource Profile is a WoT Thing Description. We can therefore represent:
(insert RDF of hmas:Resource profile that is profile of a td:Thing, e.g. from issue https://github.com/HyperAgents/hmas/issues/187)
```rdf
@prefix hmas: <https://purl.org/hmas/> .
@prefix onto: <https://ci.mines-stetienne.fr/kg/ontology#> .
@prefix hctl: <https://www.w3.org/2019/wot/hypermedia#> .
@prefix pto:   <http://www.productontology.org/id/> .
@prefix htv: <http://www.w3.org/2011/http#> .
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix xs: <https://www.w3.org/2001/XMLSchema#> .
@prefix ex: <http://example.org/> .

ex:ur5Profile a hmas:ResourceProfile;
   hmas:isProfileOf ex:ur5.

ex:ur5 a td:Thing, pto:Robotic_arm ;
   td:title "UR5 Robotic Arm" ;
   td:hasSecurityConfiguration [ a wotsec:NoSecurityScheme ].
```

(Optional TODO: explain how td:baseURI is used in hmas:ResourceProfile)
# 3. hMAS Interaction and WoT TD Alignment

## 3.1 Signifiers and Interaction Affordances

### 3.1.1 Signified Interaction Affordances


# 4. SHACL and JSON Data Schema Alignment

# 5. Summary

# 6. Acknowledgements

This document was produced by the HyperAgents research team, spread over the laboratories of INRIA Nice Sophia (Fabien Gandon, Christopher Leturc, Olivier Corby, Franck Michel, Andrea Tettamanzi, Serena Villata, Nicolas Robert), École des Mines de Saint-Étienne (Antoine Zimmermann, Maxime Lefrançois, Victor Charpenay, Luis Gustavo Nardin, Olivier Boissier, Gauthier Picard) and the University of Saint Gallen (Andrei Ciortea, Danai Vachtsevanou, Simon Mayer).

# 6. References

[WOT-THING-DESCRIPTION]

Web of Things (WoT) Thing Description 1.1. Sebastian Käbisch; Michael McCool; Ege Korkan. W3C. 5 December 2023. W3C Recommendation. URL: https://www.w3.org/TR/wot-thing-description/ 



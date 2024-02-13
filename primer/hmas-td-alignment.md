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

```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix td: <https://www.w3.org/2019/wot/td#> .
@prefix hmas: <https://purl.org/hmas/> .

td:Thing rdfs:subClassOf hmas:Artifact .
```

## 2.2 Resource Profiles and Thing Descriptions
A WoT Thing is a subclass of hMAS Artifact whose hMAS Resource Profile is a WoT Thing Description. We can therefore represent:

```rdf
@prefix hmas: <https://purl.org/hmas/> .
@prefix pto:   <http://www.productontology.org/id/> .
@prefix ex: <http://example.org/> .
@prefix td: <https://www.w3.org/2019/wot/td#> .
@prefix wotsec: <https://www.w3.org/2019/wot/security#> .

ex:ur5Profile a hmas:ResourceProfile;
   hmas:isProfileOf ex:ur5.

ex:ur5 a td:Thing, pto:Robotic_arm ;
   td:title "UR5 Robotic Arm" ;
   td:hasSecurityConfiguration [ a wotsec:NoSecurityScheme ] .
```

Constraints can be added on a hmas:ResourceProfile that will concern any request trying to reach a hmas:Signifier of that artifact.

These constraints allows to check the td:baseURI property on the incoming data.

```turtle
@prefix hmas: <https://purl.org/hmas/> .
@prefix pto:   <http://www.productontology.org/id/> .
@prefix ex: <http://example.org/> .
@prefix td: <https://www.w3.org/2019/wot/td#> .
@prefix wotsec: <https://www.w3.org/2019/wot/security#> .
@prefix sh: <http://www.w3.org/ns/shacl#> .

ex:ur5Profile a hmas:ResourceProfile;
   hmas:isProfileOf ex:ur5 ;
   hmas:globalSpecification [
        sh:class hmas:ActionExecution ;
        sh:property [
            sh:path hmas:PathToBaseURI ;
            sh:minCount 1 ;
            sh:maxCount 1 ;
            sh:hasValue <http://link.to/my/artifact/base-uri>
        ]
    ] .

ex:ur5 a td:Thing, pto:Robotic_arm ;
   td:title "UR5 Robotic Arm" ;
   td:hasSecurityConfiguration [ a wotsec:NoSecurityScheme ] .
```
# 3. hMAS Interaction and WoT TD Alignment

## 3.1 Signifiers and Interaction Affordances

### 3.1.1 Signified Interaction Affordances

A td:InteractionAffordance can be used as specification for a hmas:Signifier using the property hmas:signifies

```
@prefix hmas: <https://purl.org/hmas/> .
@prefix td: <https://www.w3.org/2019/wot/td#> .
@prefix pto:   <http://www.productontology.org/id/> .
@prefix wotsec: <https://www.w3.org/2019/wot/security#> .
@prefix hctl: <https://www.w3.org/2019/wot/hypermedia#> .
@prefix js: <https://www.w3.org/2019/wot/json-schema#> .
@prefix ex: <https://www.example.org/> .

ex:ur5Profile a hmas:ResourceProfile;
   hmas:exposesSignifier [ a hmas:Signifier ; hmas:signifies ex:affordance ];
   hmas:isProfileOf ex:ur5.

ex:ur5 a td:Thing, pto:Robotic_arm ;
   td:title "UR5 Robotic Arm" ;
   td:hasSecurityConfiguration [ a wotsec:NoSecurityScheme ];
   td:hasInteractionAffordance ex:affordance .

ex:affordance a td:PropertyAffordance, js:IntegerSchema ;
    td:name "example affordance";
	td:hasForm ex:form .

ex:form a hctl:Form;
    hctl:hasOperationType td:readProperty, td:writeProperty ;
    hctl:hasTarget <https://api.interactions.ics.unisg.ch/example> .
```

### 3.1.2 SHACL Action Specifications and Interaction Affordances

A ShaCL constraint can be provided to describe the Affordances.

This constraint can embed a td:OperationType shape to force semantics to the ActionExecution.

For the PropertyAffordances td:OperationType MUST be one of readproperty, writeproperty, observeproperty, unobserveproperty

```turtle@prefix hmas: <https://purl.org/hmas/> .
@prefix hmas: <https://purl.org/hmas/> .
@prefix hmas-dev: <https://purl.org/hmas/dev#> .
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix hctl: <https://www.w3.org/2019/wot/hypermedia#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix ex: <https://www.example.org/> .

# Example of readproperty Action Specification
ex:TruckReadableBatterySpecification a sh:NodeShape ;
    sh:class hmas:ActionExecution ;
    sh:property [
        sh:path prov:used ;
        sh:minQualifiedShape 1 ;
        sh:maxQualifiedShape 1 ;
        sh:qualifiedValueShape [
            sh:class hctl:Form ;
            sh:property hmas-dev:ReadProperty, hmas-dev:GetMethod, hmas-dev:forApplicatonJson, [
                sh:path hctl:hasTarget ;
                sh:minCount 1 ;
                sh:maxCount 1 ;
                sh:hasValue "/properties/batteryvoltage"
            ]
        ]
    ] , [
        sh:path hmas:hasOutput ;
        sh:minQualifiedShape 1 ;
        sh:maxQualifiedShape 1 ;
        sh:qualifiedValueShape ex:TruckBatteryBody
    ] .

# Example of writeproperty Action Specification
ex:TruckSettableWheels a sh:NodeShape ;
    sh:class hmas:ActionExecution ;
    sh:property [
        sh:path prov:used ;
        sh:minQualifiedShape 1 ;
        sh:maxQualifiedShape 1 ;
        sh:qualifiedValueShape [
            sh:class hctl:Form ;
            sh:property hmas-dev:WriteProperty, hmas-dev:PostMethod, hmas-dev:forApplicatonJson, [
                sh:path hctl:hasTarget ;
                sh:minCount 1 ;
                sh:maxCount 1 ;
                sh:hasValue "/actions/wheelControl"
            ]
        ]
    ] , [
        sh:path hmas:hasInput ;
        sh:minQualifiedShape 1 ;
        sh:maxQualifiedShape 1 ;
        sh:qualifiedValueShape ex:JsonControlWheelBody
    ] .


# Example of observeproperty Action Specification
ex:CherrybotObservableGripper a sh:NodeShape ;
    sh:class hmas:ActionExecution ;
    sh:property [
        sh:path prov:used ;
        sh:minQualifiedShape 1 ;
        sh:maxQualifiedShape 1 ;
        sh:qualifiedValueShape [
            sh:class hctl:Form ;
            sh:property hmas-dev:ObserveProperty, hmas-dev:PostMethod, hmas-dev:forApplicatonJson, [
                sh:path hctl:hasTarget ;
                sh:minCount 1 ;
                sh:maxCount 1 ;
                sh:hasValue "/gripper/observe"
            ]
        ]
    ] , [
        sh:path hmas:hasInput ;
        sh:minQualifiedShape 1 ;
        sh:maxQualifiedShape 1 ;
        sh:qualifiedValueShape ex:CallbackURIBody
    ] , [
        sh:path hmas:hasInput ;
        sh:minQualifiedShape 1 ;
        sh:maxQualifiedShape 1 ;
        sh:qualifiedValueShape ex:NotificationSpecification
    ] .

# Example of unobserveproperty Action Specification
ex:CherrybotUnobservableGripper a sh:NodeShape ;
    sh:class hmas:ActionExecution ;
    sh:property [
        sh:path prov:used ;
        sh:minQualifiedShape 1 ;
        sh:maxQualifiedShape 1 ;
        sh:qualifiedValueShape [
            sh:class hctl:Form ;
            sh:property hmas-dev:UnobserveProperty, hmas-dev:GetMethod, hmas-dev:forApplicatonJson, [
                sh:path hctl:hasTarget ;
                sh:minCount 1 ;
                sh:maxCount 1 ;
                sh:hasValue "/gripper/unobserve"
            ]
        ]
    ] , [
        sh:path hmas:hasInput ;
        sh:minQualifiedShape 1 ;
        sh:maxQualifiedShape 1 ;
        sh:qualifiedValueShape ex:CallbackURIBody
    ] .
```

For the Action affordance the following values are allowed invokeaction, queryaction, cancelaction 

```turtle
@prefix hmas: <https://purl.org/hmas/> .
@prefix hmas-dev: <https://purl.org/hmas/dev#> .
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix hctl: <https://www.w3.org/2019/wot/hypermedia#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix ex: <https://www.example.org/> .

# Example of invokeaction Action Specification
ex:ActionablePrinting a sh:NodeShape ;
    sh:class hmas:ActionExecution ;
    sh:property [
        sh:path prov:used ;
        sh:minQualifiedShape 1 ;
        sh:maxQualifiedShape 1 ;
        sh:qualifiedValueShape [
            sh:class hctl:Form ;
            sh:property hmas-dev:InvokeAction, hmas-dev:PostMethod, hmas-dev:forApplicatonJson, [
                sh:path hctl:hasTarget ;
                sh:minCount 1 ;
                sh:maxCount 1 ;
                sh:hasValue "/print"
            ]
        ]
    ] , [
	sh:path: hmas:hasInput ;
        sh:minQualifiedShape 1 ;
        sh:maxQualifiedShape 1 ;
        sh:qualifiedValueShape ex:documentDescriptionBody
    ] , [
        sh:path: hmas:hasOutput ;
        sh:minQualifiedShape 1 ;
        sh:maxQualifiedShape 1 ;
        sh:qualifiedValueShape ex:printerStatus
    ] .

# Example of invokeaction Action Specification
ex:CheckableProcess a sh:NodeShape ;
    sh:class hmas:ActionExecution ;
    sh:property [
        sh:path prov:used ;
        sh:minQualifiedShape 1 ;
        sh:maxQualifiedShape 1 ;
        sh:qualifiedValueShape [
            sh:class hctl:Form ;
            sh:property hmas-dev:QueryAction, hmas-dev:PostMethod, hmas-dev:forApplicatonJson, [
                sh:path hctl:hasTarget ;
                sh:minCount 1 ;
                sh:maxCount 1 ;
                sh:hasValue "/get-progress"
            ]
        ]
    ] , [
        sh:path: hmas:hasOutput ;
        sh:minQualifiedShape 1 ;
        sh:maxQualifiedShape 1 ;
        sh:qualifiedValueShape ex:progressStatus
    ] .

# Example of cancelaction Action Specification
ex:CancelablePrinting a sh:NodeShape ;
    sh:class hmas:ActionExecution ;
    sh:property [
        sh:path prov:used ;
        sh:minQualifiedShape 1 ;
        sh:maxQualifiedShape 1 ;
        sh:qualifiedValueShape [
            sh:class hctl:Form ;
            sh:property hmas-dev:CancelAction, hmas-dev:PostMethod, hmas-dev:forApplicatonJson, [
                sh:path hctl:hasTarget ;
                sh:minCount 1 ;
                sh:maxCount 1 ;
                sh:hasValue "/print/cancel"
            ]
        ]
    ] .
```

And finally for the Event Affordance the following terms are implemented: subscribeevent, unsubscribeevent, or both 

```turtle
@prefix hmas: <https://purl.org/hmas/> .
@prefix hmas-dev: <https://purl.org/hmas/dev#> .
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix hctl: <https://www.w3.org/2019/wot/hypermedia#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix ex: <https://www.example.org/> .

# Example of subscribeevent Action Specification
ex:SubscribableOverheating a sh:NodeShape ;
    sh:class hmas:ActionExecution ;
    sh:property [
        sh:path prov:used ;
        sh:minQualifiedShape 1 ;
        sh:maxQualifiedShape 1 ;
        sh:qualifiedValueShape [
            sh:class hctl:Form ;
            sh:property hmas-dev:SubscribeEvent, hmas-dev:PostMethod, hmas-dev:forApplicatonJson, [
                sh:path hctl:hasTarget ;
                sh:minCount 1 ;
                sh:maxCount 1 ;
                sh:hasValue "/overheat/subscribe"
            ]
        ]
    ] , [
	sh:path: hmas:hasInput ;
        sh:minQualifiedShape 1 ;
        sh:maxQualifiedShape 1 ;
        sh:qualifiedValueShape ex:callbackUrisBody
    ] , [
        sh:path: hmas:hasOutput ;
        sh:minQualifiedShape 1 ;
        sh:maxQualifiedShape 1 ;
        sh:qualifiedValueShape ex:NotificationSpecification
    ] .

# Example of unsubscribeevent Action Specification
ex:UnsubscribableOverheating a sh:NodeShape ;
    sh:class hmas:ActionExecution ;
    sh:property [
        sh:path prov:used ;
        sh:minQualifiedShape 1 ;
        sh:maxQualifiedShape 1 ;
        sh:qualifiedValueShape [
            sh:class hctl:Form ;
            sh:property hmas-dev:InvokeAction, hmas-dev:PostMethod, hmas-dev:forApplicatonJson, [
                sh:path hctl:hasTarget ;
                sh:minCount 1 ;
                sh:maxCount 1 ;
                sh:hasValue "/overheat/unsubscribe"
            ]
        ]
    ] , [
	sh:path: hmas:hasInput ;
        sh:minQualifiedShape 1 ;
        sh:maxQualifiedShape 1 ;
        sh:qualifiedValueShape ex:callbackUrisBody
    ] .
```

# 4. SHACL and JSON Data Schema Alignment

# 5. Summary

# 6. Acknowledgements

This document was produced by the HyperAgents research team, spread over the laboratories of INRIA Nice Sophia (Fabien Gandon, Christopher Leturc, Olivier Corby, Franck Michel, Andrea Tettamanzi, Serena Villata, Nicolas Robert), École des Mines de Saint-Étienne (Antoine Zimmermann, Maxime Lefrançois, Victor Charpenay, Luis Gustavo Nardin, Olivier Boissier, Gauthier Picard) and the University of Saint Gallen (Andrei Ciortea, Danai Vachtsevanou, Simon Mayer).

# 6. References

[WOT-THING-DESCRIPTION]

Web of Things (WoT) Thing Description 1.1. Sebastian Käbisch; Michael McCool; Ege Korkan. W3C. 5 December 2023. W3C Recommendation. URL: https://www.w3.org/TR/wot-thing-description/ 



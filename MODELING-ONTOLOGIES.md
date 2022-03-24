
# Modeling ontologies

This file explains :
* how to use different classes and properties for modeling ontologies ;
* ...

(notice : deleting/creating is more related to the contributing file and it should be integrated to the contributed file as specifical rules)

## Using the current classes and properties

1) Use rather hmas:directlyContains and do not use hmas:transitivelyContains (only for requests)

Related issues :
https://github.com/HyperAgents/ns.hyperagents.org/issues/6


2) When should you use rdfs:seeAlso instead of dct:source?

Use dct:source when the described resource is derived from the related resource in whole or in part e.g. a particular comment that justifies the described resource or the motivating scenario.

Use rdfs:seeAlso for every resources that is related to the described resource e.g. the rationale given in issues, similar resources.

Related issues :
...

3) Use rdfs:comments to give the definition of your described resource
 
Related issues :
...

## Creating new classes and properties

1) Do not duplicate the same difference in properties, classes and ranges/domains

We mean by do not duplicating e.g. do not create a class hmas:containsArtifact if hmas:contains is enough since the type of ressource allows you to know the nature of the container. 

Related issues :
https://github.com/HyperAgents/ns.hyperagents.org/issues/6

### Modifying a class or a property




## Deleting a class or a property

1) If a class is not necessary for the ontology and not justified by a motivating scenario, then this class can be delete.

We seek to express our ontology in the most minimalist and simplest way possible. 
We believe that the elegance of a formalism lies in its simplicity and generalization. 
Apply the philosophy of an Occam's razor.

Related issues :
https://github.com/HyperAgents/ns.hyperagents.org/issues/6




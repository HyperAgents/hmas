# Organizational Hierarchy

## Short description
Organizations can be structured using multiple levels of authority and a vertical link between superior and subordinate levels of the organization.

## Examples
1. [Mobility as a Service](../../scenarios/mobility-as-a-service.md)
2. Extended Enterprise

## Glossary
* **Situated Regulated Organization Entity** is an Organization situated on Agents and Artifacts, regulated by a normative system. The Agents' actions on Artifacts and Agents' interactions with other Agents of the same entity are regulated by the normative system (i.e., regulative norms resulting from the enactment of abstract regulative norms part of the normative specification of the Organization).

## Competency questions
```
identifier: 1
question: ** Question  **
outcome: ** The result of your question **
exemplar_answers:
|- ** Example of answers **

** name of file of the motivating scenario ; **
  -
depends_on: [hmas]
```
(...)

## Formal description
```
cq: ** identifier of the competency question it **
query: |-
 ** Example : SELECT ?workspace ?agent WHERE { ?workspace hmas:hosts ?agent } **
output: ** Result :  { (<w>,<a>) s.t.<w> hmas:hosts <a>  }  **
```
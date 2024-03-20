# Discover catalogs

## Description

A warehouse has deployed several agents exposing different messaging signifiers, implementing different metamodels and it bought 4 robotic arms from the same manufacturer therefore having the same set of signifiers represented in a unique shared reference description.

The robotic arms are meant for moving objects from the real world from one place to another place.

Some agents need to discover some set of required signifiers from the available artifacts in order to know which artifacts can be used to perform the task of grabbing an object and moving it to another place.

The agents must also discover which of them use some specific standard jade messaging signifiers in order to send messages to each other.

The warehouse and the robot manufacturer wish to limit the duplication of descriptions and reuse descriptions as much as possible to ease maintenance.

## Competency Questions

| ID | Question in natural language | Example of answer |
|---|---|---|
| q1 | Which artifacts have the signifiers required to grip and move an object? | Artifacts Ar1, Ar3 and Ar5 |
| q2 | Which agents implement the fipa messaging signifiers with the performative Request ? | Ag2 and Ag3 |

## Glossary

* [**SignifiersCatalog**](https://purl.org/hmas/ns/SignifiersCatalog): A class expressing a set of reusable signifiers that can be available for any hMAS referencing it in a resource profile
* [**exposesSignifierFrom**](https://purl.org/hmas/ns/exposesSignifierFrom): A property that a Resource profile can have to refer to a reusable set of signifiers it exposes
* [**globalSpecification**](https://purl.org/hmas/ns/globalSpecification ): A property that a resource profile can have to express additional shapes that the action executions related to the artifact's resource profile should validate
* [**proposesSignifier**](https://purl.org/hmas/ns/proposesSignifier ): A property that a Signifier catalog can have to refer to a reusable signifier it has
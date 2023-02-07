# Discovery of Workspaces, Agents, and Artifacts in Hypermedia Environments

## Description

A production engineer uses a Web frontend to configure and operate a factory. The factory’s shop floor is composed of multiple production cells. Each production cell contains various industrial artifacts (industrial robots, conveyor belts, laser engravers, video cameras, etc.) as well as human and artificial agents that may operate the artifacts. To access the factory, the engineer points their Web browser to the URI of the factory. The browser dereferences the URI to retrieve a representation of the factory. The manufacturing environment is composed of a hierarchy of workspaces with one root workspace that represents the shop floor and sub-workspaces for each production cell. The industrial artifacts and agents contained and operating within the factory workspace are also contained within the sub-workspace that represents the production cell in the hypermedia environment. This allows the production engineer to use the Web frontend to navigate the shop floor, to intervene in the operation of industrial artifacts, to interact with agents, and to program artificial agents. The production engineer can navigate the hierarchy of workspaces in both directions — from parent to child workspace and from child to parent workspace. Furthermore, the Web frontend allows the production engineer to search for a specific agent on the shop floor. Metadata about workspaces, agents, artifacts, and the means to interact with all these resources are conveyed to the Web frontend at run time through resource profiles.

## Competency Questions

| ID | Question in natural language | Example of answer |
|---|---|---|
| q1 | What are the workspaces directly contained in a given workspace? | Workspaces contained on the factory's ground floor `ex:groundFloor`: `ex:productionCell1` and `ex:productionCell2` |
| q2 | What are all the workspaces contained in a given workspace (directly or indirectly)? | All workspaces contained in factory `ex:factory`: `ex:groundFloor`, `ex:productionCell1`, and `ex:productionCell2` |
| q3 | What is the parent workspace of a given workspace? | Parent workspace of ground floor workspace `ex:groundFloor`: `ex:factory` |
| q4 | What are the artifacts contained in a given workspace? | Artifacts contained in workspace `ex:productionCell1`: `ex:ur5` and `ex:phantomX` |
| q5 | What are the agents contained in a given workspace? | Agents contained in workspace `ex:productionCell1`: `ex:autonomousBob` and `ex:factorySupervisor` |
| q6 | What are all the workspaces that contain a given agent? | Workspaces containing agent `ex:autonomousBob`: `ex:productionCell1` and `productionCell2` |
| q7 | What is the profile of a given resource? | Resource profile of the factory workspace `ex:factory`: `ex:factoryProfile` |

## Glossary

* [**Workspace**](https://purl.org/hmas/core#Workspace): A logical container of one or multiple interactions among agents and artifacts.
* [**Agent**](https://purl.org/hmas/core#Agent): An entity that is capable of autonomous behavior.
* [**Artifact**](https://purl.org/hmas/core#Artifact):  A resource that can be dynamically constructed, shared, and used by agents to support their activities.
* [**Resource Containment**](	https://purl.org/hmas/core#contains): A relation that refers to a logical containment relation and is related to the definition of a workspace as a logical container.
* [**Resource Profile**](https://purl.org/hmas/core#ResourceProfile): Structured data describing a resource through general metadata, domain- and application-specific metadata, and signifiers.
* [**Signifier**](https://purl.org/hmas/core#Signifier): see [Other scenario](../discover-signifiers/README.md).

### Recommendations

The term `hmas:Agent` relates to [foaf:Agent](http://xmlns.com/foaf/0.1/#term_Agent), [foaf:Person](http://xmlns.com/foaf/0.1/#term_Person), [schema:Person](https://schema.org/Person), [stn:Agent](https://w3id.org/stn/core#Agent), [stn:Person](https://w3id.org/stn/core#Person), [dbpedia-owl:Agent](http://dbpedia.org/ontology/Agent), [prov:Agent](http://www.w3.org/ns/prov#Agent).
The term `hmas:Workspace` relates to [ldp:Container](https://www.w3.org/ns/ldp#Container).

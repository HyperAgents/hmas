# Discovery of Workspaces, Agents, and Artifacts in Hypermedia Environments

## Description

A production engineer uses a Web frontend to configure and operate a factory composed of multiple production cells. To access the manufacturing environment, the engineer points their Web browser to the URI of the factory. The browser dereferences the URI to retrieve a representation of the factory. The factory is organized as a hierarchy of workspaces with one root workspace that represents the factory and sub-workspaces for each production cell on the shop floor. Each production cell contains various industrial artifacts (industrial robots, conveyor belts, laser engravers, video cameras, etc.) as well as human and artificial agents that may operate the artifacts. The industrial artifacts and agents contained within a given production cell are also reflected and contained within the sub-workspace that represents the production cell in the hypermedia environment. This allows the production engineer to use the Web frontend to navigate the factory, to intervene in the operation of industrial artifacts, to interact with agents, and to program artificial agents. The production engineer can navigate the hierarchy of workspaces in both directions — from parent to child workspace and from child to parent workspace. Furthermore, the Web frontend allows the production engineer to search for a specific agent on the shop floor. Metadata about workspaces, agents, artifacts, and the means to interact with all these resources are conveyed to the Web frontend at run time through resource profiles.

## Competency Questions

| ID | Question in natural language | Example of answer |
|---|---|---|
| q1 | What are the workspaces directly contained in a given workspace? | an example instance |
| q2 | What are all the workspaces contained in a given workspace (directly or indirectly)? | an example instance |
| q3 | What is the parent workspace of a given workspace? | an example instance |
| q4 | What are the artifacts contained in a given workspace? | an example instance |
| q5 | What are the agents contained in a given workspace? | an example instance |
| q6 | What are all the workspaces that contain a given agent? | an example instance |
| q7 | What is the profile of a given resource? | an example instance |

## Glossary

* [**Workspace**](https://ci.mines-stetienne.fr/hmas/core#Workspace): A logical container of one or multiple interactions among agents and artifacts.
* [**Agent**](https://ci.mines-stetienne.fr/hmas/core#Agent): An entity that is capable of autonomous behavior.
* [**Artifact**](https://ci.mines-stetienne.fr/hmas/core#Agent):  A resource that can be dynamically constructed, shared, and used by agents to support their activities.
* [**Resource Containment**](https://ci.mines-stetienne.fr/hmas/core#Agent): A relation that refers to a logical containment relation and is related to the definition of a workspace as a logical container.
* [**Resource Profile**](https://ci.mines-stetienne.fr/hmas/core#Agent): Structured data describing a resource through general metadata, domain- and application-specific metadata, and signifiers.
* [**Signifier**](https://purl.org/hmas/ns/OtherTerm): see [_Other scenario_](../other-scenario/README.md).

### Recommendations

_If the newly defined terms are to be used in a particular way, details can be given here to make readers understand what is considered a good practice. Similarly, a comparison with existing vocabularies can be given here, such that readers understand how to combine these vocabularies with the newly defined terms or why these vocabularies are not suitable here._
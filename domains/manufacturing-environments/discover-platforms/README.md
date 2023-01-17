# Discovery of Hypermedia MAS Platforms and their Profiles

## Description

A manufacturing agent operating on a shop floor in St. Gallen is delegated a goal for which it needs to interact with a manufacturing agent operating on a shop floor in Saint-Étienne. The St. Gallen agent is given the URI of the Saint-Étienne agent but still needs to find a means to communicate with the agent. The St. Gallen agent dereferences the URI of the Saint-Étienne agent to retrieve its resource profile for more information. The agent’s resource profile includes a relation to the Hypermedia MAS Platform that hosts the agent. The St. Gallen agent then dereferences the URI of the hosting platform to retrieve the platform’s resource profile as well. From the platform’s resource profile, the St. Gallen agent discovers that this platform is FIPA-compliant. Furthermore, the platform's resource profile includes a signifier for a FIPA Message Transport Service that the St. Gallen agent can use to send messages via HTTP to any agent hosted on the platform, including the Saint-Étienne agent it needs to interact with. The St. Gallen agent uses this information to contact the Saint-Étienne agent.

## Competency Questions

| ID | Question in natural language | Example of answer |
|---|---|---|
| q1 | What is the Hypermedia MAS platform that hosts a given agent? | Hypermedia MAS Platform that hosts Saint-Étienne agent `ex:agentSaintEtienne`: `ex:platformSaintEtienne` |
| q2 | What is the resource profile of a given agent? | Resource profile of Saint-Étienne agent `ex:agentSaintEtienne`: `ex:agentSaintEtienneProfile` |
| q3 | What is the resource profile of a given Hypermedia MAS platform? | Resource profile of Saint-Étienne Hypermedia MAS Platform `ex:platformSaintEtienne`: `ex:platformSaintEtienneProfile` |
| q4 | What is a signifier for a FIPA message transport service of a given platform? | Signifier exposed in the resource profile of the Saint-Étienne Hypermedia MAS Platform `ex:platformSaintEtienne`: `ex:signifer` |

For competency question q4, it is outside the scope of this scenario to represent the actual signifier (e.g., a signifier that describes a FIPA message transport service). The terms required to create such a representation will be introduced by the interaction ontology.

## Glossary

* [**Hypermedia MAS Platform**](https://purl.org/hmas/core#HypermediaMASPlatform): A Hypermedia MAS platform is a system providing a collection of features to support Hypermedia MAS.
* [**Resource Hosting**](https://purl.org/hmas/core#isHostedOn): A relation between a resource (e.g., an agent) and the Hypermedia MAS Platform that hosts the resource.
* [**Agent**](https://purl.org/hmas/core#Agent): see [Other scenario](../discover-core/README.md).
* [**Resource Profile**](https://purl.org/hmas/core#ResourceProfile): see [Other scenario](../discover-core/README.md).
* [**Signifier**](https://purl.org/hmas/core#Signifier): see [Other scenario](../discover-signifiers/README.md).

### Recommendations

TODOs:
- [ ] TODO
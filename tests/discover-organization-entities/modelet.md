# Discover Organization

## Description
Organizations are entities that Agents should be able to find and possibly join in order to achieve their goals.

## Examples
1. [Mobility as a Service](../../scenarios/mobility-as-a-service.md)
2. [Extended Enterprise](../../scenarios/extended-enterprise.md)

## Competency questions

| ID | Question in natural language |
|---|---|
| q1 | What are the existing Organization Entities? |
| q2 | What are the existing Organization Entities in a Workspace? |
| q3 | What are the members of an Organization Entity? |
| q4 | What are the Organization Entities that an Agent can join? |
| q5 | How can an Agent join an Organization Entity? |
| q6 | What are the Artifacts in an Organization Entity? |

## Glossary

* **Organization Entity**: Organization Entity is an organization situated on Agents and Artifacts, and regulated by a normative system.

### Recommendations

Schema.org includes the classes [`schema:Organization`](https://schema.org/Organization) and [`schema:OrganizationRole`](https://schema.org/OrganizationRole) but these classes are mostly used for human organizations. They may be considered as sub-classes of the classes defined in the HyperAgents vocabularies.

The [W3C ORG ontology](https://www.w3.org/TR/vocab-org/) defines ground concepts that may be reused in the HyperAgents regulation vocabulary.

Although the `schema.org` and `W3C ORG` ontologies have the Organization or similar class that could be used to describe an Organization Entity in HyperAgents, these ontologies have a membership property (e.g., `memberOf`) enabling an organization to be included in another. The Organization Entity in HyperAgents, however, will represent a more flexible relationship concept enabling any form of structuring and it will not be limited to membership.

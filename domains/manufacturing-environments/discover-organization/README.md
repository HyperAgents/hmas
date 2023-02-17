# Discover Organizations, their Members and Materials in Hypermedia Environments

## Description
A factory contains various industrial artifacts (e.g., industrial machinery, industrial robots, conveyor belts, laser engravers, video cameras) as well as human and artificial agents that may operate them. Besides, the factory operates in accordance to a set of regulations that reflect its values, structure, goals, configuration and norms. A production engineer uses a Web frontend to check and set the factory's regulations. The engineer points the Web browser to the URI of the factory organization, which dereferences the URI to retrieve its representation in the hypermedia environment. This allows the production engineer to use the Web frontend to identify the industrial artifacts composing the factory and the agents that belongs to the factory and are assigned to operate its industrial artifacts. These agents and artifacts may be contained in one or multiple workspaces. In addition, the production engineer can check the factory's regulations and modify them if deemed necessary.

## Competency Questions

| ID | Question in Natural Language | Example |
|----|------------------------------|---------|
| q1 | What are the discoverable organizations in a given workspace? | What are the discoverable organizations in the factory building workspace? **ex:factoryOrganization** |
| q2 | What are the members of a given organization?                 | What are the members of the factory organization? **ex:autonomousBob**, **ex:factorySupervisor**      |
| q3 | What are the materials of a given organization?               | What are the materials of the factory organization? **ex:ur5**, **ex:phantomX**                       |

## Glossary

* **Organization**: An Organization is an entity representing a collection of Agents and Artifacts, and regulated by a regulation system.
* **Member**: A Member refers to an Agent that belongs to an Organization.
* **Material**: A Material refers to an Artifact that belongs to an Organization.

## Recommendations

1. The term [hmas:Organization](https://purl.org/hmas/Organization) relates to the terms [org:Organization](https://www.w3.org/TR/vocab-org/#org:Organization), [schema:Organization](https://schema.org/Organization), and [foaf:Group](http://xmlns.com/foaf/0.1/#term_Group).
2. The term [hmas:Organization](https://purl.org/hmas/Organization) does not relate to the term [foaf:Organization](http://xmlns.com/foaf/0.1/#term_Organization) or the term [prov:Organization](https://www.w3.org/TR/2013/REC-prov-o-20130430/#Organization) because [foaf:Organization](http://xmlns.com/foaf/0.1/#term_Organization) assumes that an organization is a kind of [foaf:Agent](http://xmlns.com/foaf/0.1/#term_Agent) and [prov:Organization](https://www.w3.org/TR/2013/REC-prov-o-20130430/#Organization) is a subclass of [prov:Agent](https://www.w3.org/TR/2013/REC-prov-o-20130430/#Agent).
3. The property [hmas:isMemberOf](https://purl.org/hmas/isMemberOf) relates to [org:memberOf](https://www.w3.org/TR/vocab-org/#property-memberof), [schema:member](https://schema.org/member), and [foaf:member](http://xmlns.com/foaf/0.1/#term_member).

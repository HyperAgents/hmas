# Discovery Organizations in Hypermedia Environments

## Description
A factory contains various industrial artifacts (e.g., industrial machinery, industrial robots, conveyor belts, laser engravers, video cameras) as well as human and artificial agents that may operate them. Besides, the factory operates in accordance to a set of regulations that reflect its values, structure, goals, configuration and norms. A production engineer uses a Web frontend to check and set the factory's regulations. The engineer points the Web browser to the URI of the factory organization, which dereferences the URI to retrieve its representation in the hypermedia environment. This allows the production engineer to use the Web frontend to identify the industrial artifacts composing the factory and the agents that belongs to the factory and are assigned to operate the industrial artifacts. These agents and artifacts situate the organization in one or multiple workspaces. In addition, the production engineer can check the factory's regulations and modify them if deemed necessary.

## Competency Questions

| ID | Question in Natural Language | Example |
|----|------------------------------|---------|
| q1 | What is the organization regulating X?                             | What is the organization regulating the factory? **ex:factoryOrganization**                                           |
| q2 | What are the organizations of a given workspace?                   | What are the organizations of the productionCell1 workspace? **ex:factoryOrganization**                               |
| q3 | What are the workspaces in which a given organization is situated? | What are the workspaces in which the factory organization is situated? **ex:productionCell1**, **ex:productionCell2** |
| q4 | What are the agents member of a given organization?                | What are the agents member of the factory organization? **ex:autonomousBob**, **ex:factorySupervisor**                |
| q5 | What are the artifacts part of a given organization?               | What are the artifacts part of the factory organization? **ex:ur5**, **ex:phantomX**                                  |

## Glossary

* **Organization**: An Organization is an entity situated on Agents and Artifacts, and regulated by a regulation system.
* **Situated Organization**: An Organization is situated through its Members and Materials.
* **Member**: A Member refers to an Agent that belongs to an Organization.
* **Material**: A Material refers to an Artifact that belongs to an Organization.

## Recommendations

None

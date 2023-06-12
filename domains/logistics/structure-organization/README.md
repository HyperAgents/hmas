# Structure the Social Context within an Organization

## Description
John had decided to copy the SL Logistics' organizational model to create the FL Logistics organization. Therefore, he structures the FL Logistics into five departments: Human Resources (HR), Finance, Commercial, Planning, and Shipping. In addition, the HR and Finance departments are allocated under a super-department, the Administrative department, while the Commercial, Planning, and Shipping departments are allocated under the Operations super-department. Each of these super-departments have a director. The same person cannot be the director on both super-departments at the same time.

Associated to each of these departments, the organization defines a set of job positions as follows:
1. Administrative department : _administrative director_
2. Human Resources department : _human resources officer_
3. Finance department : _finance office_
4. Operations department : _operations director_
5. Commercial department : _account manager_
6. Planning department : _planner_
7. Shipping department : _carrier_, _collector_, and _deliverer_

Some of these job positions have a clear relationship among themselves. For example, the agent acting as _planner_ in the Planning department has to be able to communicate with agents acting as _carrier_, _collector_, and _deliverer_ in the Shipping department since it is envisioned that the former will set the schedule of collects and deliveries for the latter.

In the enterprise, job positions are not allowed to be played by the same agent, except for the _collector_ and _deliverer_ that can also be played together with the _carrier_ role.

The FL Logistics advertises available job positions and hire humans and deploy artificial agents to fulfill them.

The job positions for the HR, Finance, and Commercial departments are required to be performed by human since they demand sophisticated interactions with other humans (e.g., customers) involving complex negotiation and creativity skills. The job positions for the Planning and Shipping departments can be played by a mix of humans and artificial agents (e.g., autonomous delivery trucks).

Frank, the SL Logistics' Humans Resources Officer, receives a request to evaluate what are the job positions in the enterprise that are not currently being performed by anyone. Frank checks the organizational chart and the current list of employees, and concludes that there is a carrier job position vacant.

Jane, an artificial agent, is deployed as a carrier. Jane can communicate with the planner in the Planning department to know the tasks to perform. Because she was not informed who is the planner, she looks at the organizational chart of the enterprise and identifies Igor as the planner.

## Competency Questions

| ID | Question in Natural Language | Example |
|----|------------------------------|---------|
| q1 | What are the job positions not being played by anyone in the organization X?                              | What are the roles not being played by anyone in the FL Logistics organization? `ex:FL_AccountManager`, `ex:FL_Carrier`, `FL_Deliverer`                                            |
| q2 | What are the other agents to whom agent A can communicate with in the department Y in the organization X? | What are the other agents to whom Jane can communicate with in the Planning group in the FL Logistics organization? `ex:Igor`                                                      |
| q3 | What are the other roles to which role Y is compatible with in the department Y of the organization X?    | What are the other roles to which a FL_Carrier is compatible with in the Shipping group in the FL Logistics organization? `ex:FL_Collector`, `ex:FL_Deliverer`                     |
| q4 | What are the departments not fully populated in organization X?                                           | What are the groups not fully populated in the FL Logistics organization? `ex:FL_CommercialDepartment` |
| q5 | What are the job positions of agent A in the organization X?                                              | What are the roles played by agent Igor in the FL Logistics organization? `ex:FL_Planner`              |
| q6 | What are the sub-departments of department X?                                                             | What are the sub-groups of the Administrative group? `ex:FL_HumanResources`, `ex:FL_Finance`           |

## Glossary

* **Group**: A Group structures an Organization.
* **Group Relationship**: A Group Relationship refers to a relationship between Groups.
* **Sub-Group Relationship**: A relation that refers to a subgroup relationship between two Groups.
* **Membership**: A Membership indicates the Role played by an Agent in a Group of an Organization.
* **Social Link**: A Social Link is a type of interaction that can take place between Agents playing roles in the same or different Groups.
* **Compatibility Link**: A Compatibility Link is a relation between two roles of the same or different groups. It enables an agent to adopt the target role while already playing the source role (by default roles are incompatible, i.e., they cannot be played by the same agent in the organization).

## Recommendations

* The **Group Relationship**, **Social Link**, and **Compatibility Link** are generic terms to represent abstract relationships among the **Membership** and **Group**. Because these relationships cannot be precisely enumerated, we preferred they are represented as SHACL shapes when using the ontology.

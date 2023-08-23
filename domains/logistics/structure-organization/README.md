# Structure the Social Context within an Organization

## Description
John had decided to copy the SL Logistics' organization model to create the FL Logistics organization. John structures the FL Logistics into seven departments: Human Resources (HR), Finance, Commercial, Planning, Shipping, Administrative, and Operations. The HR and Finance departments are allocated under the Administrative department, while the Commercial, Planning, and Shipping departments are allocated under the Operations department. The Administrative and Operations departments have a director. The same person cannot be the director of both departments at the same time.

Associated to each of these departments, the organization defines a set of job positions as follows:
1. Administrative department : _administrative director_
2. Human Resources department : _human resources officer_
3. Finance department : _finance office_
4. Operations department : _operations director_
5. Commercial department : _account manager_
6. Planning department : _planner_
7. Shipping department : _carrier_, _collector_, and _deliverer_

Job positions may have explicit relationships (e.g., communicate, authority, acquaintance) among themselves. For example, the _planner_ in the Planning department has to be able to communicate with the _carrier_, _collector_, and _deliverer_ in the Shipping department since it is envisioned that the former will set the schedule of collects and deliveries for the latter. The _collector_ and _deliverer_ job positions must be played by someone already playing the _carrier_ job position.

Additionally, the _administrative director_ has authority over the agents playing any job position in the departments under the Administrative department, and the _operations director_ has authority over the agents playing any job position in the departments under the Operations department.

The FL Logistics advertises available job positions and hires human agents or deploys artificial agents to fulfill them.

The job positions for the HR, Finance, and Commercial departments are required to be performed by human agents since they demand sophisticated interactions with other humans (e.g., customers) involving complex negotiation and creativity skills. The job positions for the Planning and Shipping departments can be played by a mix of humans and artificial agents (e.g., autonomous delivery trucks).

Frank, the _human resources officer_, receives a request to evaluate what are the job positions in the FL Logistics that are not currently being played by anyone. Frank checks the organizational chart and the current list of employees, and concludes that the _account manager_ and _carrier_ job positions are vacant.

Jane, an artificial agent, is deployed as a  _carrier_. Jane can communicate with the _planner_ in the Planning department to know the tasks to perform. Because she was not informed who the _planner_ is, she checks the organizational chart of the enterprise and identifies Igor as the _planner_.

## Competency Questions

| ID | Question in Natural Language | Example |
|----|------------------------------|---------|
| q1 | What are the job positions not being played by anyone in the organization X?                        | What are the job positions not being played by anyone in the FL Logistics organization? `ex:FL_AccountManager`       |
| q2 | What are the agents to whom agent A can communicate with in the department Y in the organization X? | What are the agents to whom Jane can communicate with in the Planning department in the FL Logistics organization? `ex:Igor`                                                                     |
| q3 | What are the memberships not fully populated in the organization X?                                 | What are the memberships not fully populated in the FL Logistics organization? `ex:AccountManager_Commercial_Membership`                                                                         |
| q4 | What are the job positions of agent A in the organization X?                                        | What are the job positions played by agent Igor in the FL Logistics organization? `ex:FL_Planner`                    |
| q5 | What are the departments in the organization X                                                      | What are the departments in the FL Logistics organization? `ex:FL_AdministrativeDepartment`, `ex:FL_CommercialDepartment`, `ex:FL_FinanceDepartment`, `ex:FL_HumanResourcesDepartment`, `ex:FL_OperationsDepartment`, `ex:FL_PlanningDepartment`, `ex:FL_ShippingDepartment` |
| q6 | What are the departments under the department Y in the organization X?                               | What are the departments under the Administrative department in the FL Logistics organization? `ex:FL_FinanceDepartment`, `ex:FL_HumanResourcesDepartment`                                      |
| q7 | What are the job positions to which job position Y is incompatible with in the organization X?      | What are the job positions to which a FL_Director_Administrative is incompatible with in the FL Logistics organization? `ex:FL_Director_Operations`                                              |

## Glossary

![image](structure-organization.png)

* **Membership**: A Membership indicates the Role played by an Agent in a Group of an Organization.
* **Membership Relationship**: A relation that refers to the interaction between Agents member of two Memberships.
* **Incompatibility Link**: A Compatibility Link imposes a constraint that two Memberships are incompatible and they cannot be played by the same agent.
* **Group**: A Group structures an Organization.
* **Group Relationship**: A relation that refers to the interaction between Agents member of two Memberships involving two Groups.
* **Sub-Group Relationship**: A relation that refers to a subgroup relationship between two Groups.
* **Organization Model**: see [Create an Organization](https://github.com/HyperAgents/hmas/blob/master/domains/logistics/create-organization/README.md) scenario
* **Role**: see [Create an Organization](https://github.com/HyperAgents/hmas/blob/master/domains/logistics/create-organization/README.md) scenario
* **Organization**: see [Discover Organizations, their Members and Materials in Hypermedia Environments](https://github.com/HyperAgents/hmas/blob/master/domains/manufacturing-environments/discover-organization/README.md) scenario
* **Agent**: see [Discover Organizations, their Members and Materials in Hypermedia Environments](https://github.com/HyperAgents/hmas/blob/master/domains/manufacturing-environments/discover-organization/README.md) scenario

## Recommendations

* The **Membership Relationship** and **Group Relationship** must not be instantiated directly, they must be sub-classed to precise the exact relation between memberships and groups respectively.

* The **Incompatibility Link** imposes a constraint in the adoption of **Membership**s, so it will be represented as SHACL shapes when using the ontology.

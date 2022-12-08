# Structure an Organization

## Description
John had decided to copy the SL Logistics' organizational model. Therefore, he structures the FL Logistics into five departments: Human Resources (HR), Finance, Commercial, Planning, and Shipping. In addition, the HR and Finance departments are allocated under a super-department, the Administrative department, while the Commercial, Planning, and Shipping departments are allocated under the Operations department.

Associated to each of these departments, the enterprise defines a set of job positions as follows:
1. Human Resources department : _human resources officer_
2. Finance department : _finance office_
3. Commercial department : _account manager_
4. Planning department : _planner_
5. Shipping department : _carrier_, _collector_, and _deliverer_

Some of these job positions have a clear relationship among themselves. For example, the agent acting as _planner_ has to be able to communicate with agents acting as _carrier_, _collector_, and _deliverer_ since it is envisioned that the former will set the schedule of collects and deliveries for the latter.

The enterprise advertises available job positions and hire humans and artificial agents to fulfill them. Agents hired for a job position in the enterprise becomes employees of the enterprise.

The positions for the HR, Finance, and Commercial departments are required to be performed by human agents since they demand sophisticated interactions with humans (e.g., customers) involving complex negotiation and creativity skills. The positions for the Planning and Shipping departments can be played by a mix of humans and artificial agents (e.g., autonomous delivery trucks).

Frank, the SL Logistics' Humans Resources Officer, receives a request to evaluate what are the job roles in the enterprise that are not currently being performed by anyone. Frank determines by checking the organizational chart and the current list of employees that there is a carrier job position vacant.

Jane is hired as a carrier. She was instructed to wait until she receives the schedule from someone from the Planning department to start her tasks. However, she was not given the name of the person(s) she should interact with. Thus, she looks at the organizational chart of the enterprise and identifies that she should interact with Igor who is the planner in the enterprise.

## Competency Questions

| ID | Question in Natural Language | Example |
|----|------------------------------|---------|
| q1 | What are the job positions not being performed by anyone in the enterprise X?    | What are the job positions not being performed by anyone in the enterprise ex:FL\_Logistics? **ex:FL\_AccountantManager** |
| q2 | What are the other agents to whom agent A can interact with in the department X? | What are the other agents to whom Jane can interact with in the Planning department? **ex:Igor**                         |

## Glossary

* **Group**: A Group is a set of Agents that can exist in the structure of an Organization.
* **Group Relationship**: A Group Relationship refers to the possible relations between groups.
* **Social Link**: A Social Link is a type of interaction that can take place among agents when playing specific Roles in a Group.

## Recommendations

None

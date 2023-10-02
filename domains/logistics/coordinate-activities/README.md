# Coordinate activities within an Organization

## Description

The new FL Logistics enterprise has different main organizational goals that can be pursued in parallel: hire employees, handle invoices, maintain client relationship, and plan and deliver goods. To achieve these goals, the enterprise has defined a set of processes:
* **hiring**: contract signed, candidates interviewed
* **handling invoice**: invoices processed, payable invoices payed, invoices payments received
* **client relationship**: client relationship maintained, logistic services prospected, logistic services sold
* **delivery services**: schedule delivery of goods optimized

The **hiring process** has a set of interdependent activities, i.e., **hiring**, the root activity (i.e., an activity that there is no other activity dependent on it), depends on the completion of the **signing contract** depends on the completion of the **selecting candidate**, that depends on the completion of **assessing recommendations** and **interviewing candidates**, that depends on the completion of **preselecting candidates**, that depends on the completion of **announcing job position**, and finally depends on the completion of **writing job position description**. The **assessing recommendations** activity facilitates the **interviewing candidates** activity and influences the **selecting candidate** activity.

Each of these activities is associated to an organizational goal, i.e., **hired**, **contract signed**, **candidate selected**, **recommendations assessed**, **candidates interviewed**, **interviewees selected**, **job position announced**, and **job position description wrote**. The organizational goal **candidates interviewed** has several sub-goals, **interviews scheduled** and **interviews conducted**. The organizational goals **hired**, **contract signed**, and **job position announced** are missions of the human resources, while the **candidate selected**, **recommendations assessed**, **candidates interviewed** including its sub-goals, **candidates preselected**, and **job position description wrote** are missions of the director.

A new person has to be hired in the Commercial department for the Account Manager job position. Frank, the Human Resources Officer, commits to the organizational goals under the human resources missions, while Kate, the Director of the Operations Department, commits to the organizational goals under the director missions.

## Competency questions

| ID | Question in Natural Language | Example |
|----|------------------------------|---------| 
| q1 | What are the organizational goals agent Y has to achieve in the organization X?              | What are the organizational goals Frank has to achieve in the FL Logistics organization? | |
| q2 | What are the agent Y's activities in the organization X and when they have to be performed ? | What are the Frank's activities in the FL Logistics and when they have to be performed?  | |

| q3 | What are the other agents responsible for activity Y of the enterprise X?                    | What are the other agents with responsibilities in the carry activity? | |

## Glossary

* **Process Scheme**: A Process Scheme is an entity that represents a set of Activity Schemes intended by one or more Agents to achieve some Organizational Goals.
* **Activity Scheme**: An Activity Scheme is a planned activity.
* **Root Activity Scheme**: An Root Activity Scheme is the origin of an interdependent set of Activity Schemes.
* **Activity Scheme Dependence**: A relation that refers to the dependence relationship between two Activity Schemes.
* **Activity Scheme Influence**: A relation that refers the capacity of an Activity Scheme to have an effect on another Activity Scheme.
* **Organizational Goal**: An Organizational Goal is a state of affairs.
* **Sub-Organizational Goal Relationship**: A relation that refers to a hierarchical relationship between two Organizational Goals.
* **Commitment**: A relation that refers to a Mission to which an Agent is committed.
* **Mission**: see [Create an Organization](https://github.com/HyperAgents/hmas/blob/master/domains/logistics/create-organization/README.md) scenario
* **Organization**: see [Discover Organizations, their Members and Materials in Hypermedia Environments](https://github.com/HyperAgents/hmas/blob/master/domains/manufacturing-environments/discover-organization/README.md) scenario
* **Agent**: see [Discover Organizations, their Members and Materials in Hypermedia Environments](https://github.com/HyperAgents/hmas/blob/master/domains/manufacturing-environments/discover-organization/README.md) scenario

## Recommendations

* All terms are related to a single Organization.

* An **Activity Scheme** has at most one **Process Scheme**.

* The **Root Activity Scheme** can be inferred in a set of Activity Schemes because it is the Activity Scheme that has no other Activity Scheme dependent on it.

* The **Activity Scheme Dependence** must not be used directly, a sub-property must be created to specify the exact type of dependence being represented between activity schemes. Examples of temporal dependencies are the [Allen's interval relations](https://doi.org/10.1145/182.358434), but other types of dependencies like spatial dependencies may be possible between activity schemes.

* The **Activity Scheme Influence** must not be used directly, a sub-property must be created to specify the exact type of influence being represented between activity schemes.

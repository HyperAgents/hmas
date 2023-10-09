# Coordinate activities within an Organization

## Description

The new FL Logistics enterprise has different main organizational goals that can be pursued in parallel: hire employees, handle invoices, maintain client relationship, and plan and deliver goods. To achieve these goals, the enterprise has defined a set of processes, e.g., **hiring**, **handling invoice**, **prospecting client**, and **delivering goods**.

The **hiring process**, for instance, has a set of interdependent activities, i.e., **hiring**, the root activity, depends on the completion of the **signing contract** activity, that depends on the completion of the **selecting candidate** activity, that depends on the completion of the **assessing recommendations** and **interviewing candidates** activities, that depend on the completion of the **selecting interviewees** activity, that depends on the completion of the **announcing job position**, that finally depends on the completion of the **writing job position description**. The **assessing recommendations** activity facilitates the **interviewing candidates** activity and biases the **selecting candidate** activity.

Each activity is associated to an organizational goal, i.e., **hired**, **contract signed**, **candidate selected**, **recommendations assessed**, **candidates interviewed**, **interviewees selected**, **job position announced**, and **job position description wrote**. The organizational goal **candidates interviewed** has two sub-goals, **interviews scheduled** and **interviews conducted**. The organizational goals **hired**, **contract signed**, and **job position announced** are missions of the human resources, while the organizational goals **candidate selected**, **recommendations assessed**, **candidates interviewed**, **interviewees selected**, and **job position description wrote** are missions of the department director.

A new person has to be hired in the Commercial department for the Account Manager job position. Frank, the Human Resources Officer, commits to the organizational goals under the human resources missions, while Kate, the Director of the Operations Department, commits to the organizational goals under the department director missions.

## Competency questions

| ID | Question in Natural Language | Example |
|----|------------------------------|---------| 
| q1 | What are the organizational goals and subgoals agent Y has to achieve when committed to the organization X?                   | What are the organizational goals and subgoals Kate has to achieve when committed to the FL Logistics organization? `ex:FL_AccountManager_CandidateSelected`, `ex:FL_AccountManager_RecommendationsAssessed`, `ex:FL_AccountManager_CandidatesInterviewed`, `ex:FL_AccountManager_InterviewsScheduled`, `ex:FL_AccountManager_InterviewsConducted`, `ex:FL_AccountManager_IntervieweesSelected`, `ex:FL_AccountManager_JobPositionWrote`                            |
| q2 | What are the agent Y's activities in process Z when committed to the organization X and how they are dependent on each other? | What are Frank's activities in the process of hiring an Account Manager when committed to the FL Logistics organization and how they are dependent on each other? `ex:FL_AccountManager_AnnouncingJobPosition,ex:isPrecededBy,ex:FL_AccountManager_WritingJobPosition`, `ex:FL_AccountManager_SigningContract,ex:isPrecededBy,ex:FL_AccountManager_SelectingCandidate`, `ex:FL_AccountManager_Hiring,ex:isPrecededBy,ex:FL_AccountManager_Signingcontract`          |
| q3 | What are all the agents committed to the activities of process Y in the organization X?                                       | What are all the agents committed to the activities of process of hiring an Account Manager in the FL Logistics organization? `ex:Frank`, `ex:Kate` |

## Glossary

![image](coordinate-activities.png)

* **Process Scheme**: A Process Scheme is an entity that represents a connected set of Activity Schemes intended to achieve Organizational Goals.
* **Activity Scheme**: An Activity Scheme is a planned activity.
* **Root Activity Scheme**: A Root Activity Scheme is an Activity Scheme origin of a connected set of Activity Schemes and is associated to a Process Scheme.
* **Activity Scheme Dependence**: A relation that refers to the way in which two Activity Schemes are related to each other, and one is affected by the other.
* **Organizational Goal**: An Organizational Goal is a pursued state of affairs.
* **Sub-Organizational Goal Relationship**: A relation that refers to a hierarchical relationship between two Organizational Goals.
* **Commitment**: A relation that refers to a Mission to which an Agent is committed.
* **Mission**: see [Create an Organization](https://github.com/HyperAgents/hmas/blob/master/domains/logistics/create-organization/README.md) scenario.
* **Organization**: see [Discover Organizations, their Members and Materials in Hypermedia Environments](https://github.com/HyperAgents/hmas/blob/master/domains/manufacturing-environments/discover-organization/README.md) scenario.
* **Agent**: see [Discover Organizations, their Members and Materials in Hypermedia Environments](https://github.com/HyperAgents/hmas/blob/master/domains/manufacturing-environments/discover-organization/README.md) scenario.

## Recommendations

* The concept of activity can be the execution of a simple action, a complex set of actions, or any other useful arrangement employed to achieving organizational goals. An activity can be represented using, for instance, the PROV Ontology.

* The **Activity Scheme Dependence** should not be used directly, a sub-property must be created to specify the exact type of dependence between two activity schemes. Examples of dependencies can be temporal dependencies like the [Allen's interval relations](https://doi.org/10.1145/182.358434), spatial dependencies, or other dependencies of influence like _facilitates_ (i.e., an Activity Scheme eases another), _informs_ (i.e., an Activity Scheme advises another), or _prioritizes_ (i.e., an Activity Scheme increases the importance of another).

# Coordinate activities within an Organization

## Description

The new FL Logistics enterprise has different main organizational goals that can be pursued in parallel: hire employees, handle invoices, maintain client relationship, and plan and deliver goods. To achieve these goals, the enterprise has defined a set of processes, e.g., **hiring process**, **handling invoice process**, **prospecting client process**, and **delivering goods process**.

The **hiring process**, for instance, has a set of interdependent activities. The **hiring** activity, the root activity of this process, depends on the completion of the **signing contract** activity, that depends on the completion of the **selecting candidate** activity, that depends on the completion of both the **assessing recommendations** and **interviewing candidates** activities, that depend on the completion of the **selecting interviewees** activity, that depends on the completion of the **announcing job position** activity, that finally depends on the completion of the **writing job position description** activity. Additionally, the **assessing recommendations** activity facilitates the **interviewing candidates** activity and biases the **selecting candidate** activity.

Each activity is associated to an organizational goal, i.e., **hired**, **contract signed**, **candidate selected**, **recommendations assessed**, **candidates interviewed**, **interviewees selected**, **job position announced**, and **job position description written**. The **candidates interviewed** organizational goal has two sub-goals, **interviews scheduled** and **interviews conducted**. The human resources is responsible for the **hired**, **contract signed**, and **job position announced** organizational goals, while the department director is responsible for the **candidate selected**, **recommendations assessed**, **candidates interviewed**, **interviewees selected**, and **job position description written** organizational goals.

A new person has to be hired in the Commercial department for the Account Manager job position. Frank, the Human Resources Officer, commits to the organizational goals under the human resources responsibilities, while Kate, the Director of the Operations Department, commits to the organizational goals under the department director responsibilities.

## Competency questions

| ID | Question in Natural Language | Example |
|----|------------------------------|---------| 
| q1 | What are the organizational goals and subgoals agent Y has to achieve because is committed to the mission Z in the organization X? | What are the organizational goals and subgoals Kate has to achieve because is committed to the department director mission in the FL Logistics organization? `ex:CandidateSelected`, `ex:CandidatesInterviewed`, `ex:IntervieweesSelected`, `ex:InterviewsConducted`, `ex:InterviewsScheduled`, `ex:JobPositionWritten`, `ex:RecommendationsAssessed`                                                 |
| q2 | What are the activities in process Z proposed by the organization X and how these activities are dependent on each other?          | What are the activities in the Account Manager Hiring process proposed by the FL Logistics organization and how these activities are dependent on each other? `ex:FL_AccountManager_AnnouncingJobPosition,ex:isPrecededBy,ex:FL_AccountManager_WritingJobPosition`, `ex:FL_AccountManager_Hiring,ex:isPrecededBy,ex:FL_AccountManager_SigningContract`, `ex:FL_AccountManager_InterviewingCandidates,ex:isFacilitatedBy,ex:FL_AccountManager_AssessingRecommendations`, `ex:FL_AccountManager_SelectingCandidate,ex:isBiasedBy,ex:FL_AccountManager_AssessingRecommendations`, `ex:FL_AccountManager_SelectingCandidate,ex:isPrecededBy,ex:FL_AccountManager_AssessingRecommendations`, `ex:FL_AccountManager_SelectingCandidate,ex:isPrecededBy,ex:FL_AccountManager_InterviewingCandidates`, `ex:FL_AccountManager_SelectingInterviewees,ex:isPrecededBy,ex:FL_AccountManager_AnnouncingJobPosition`, `ex:FL_AccountManager_SigningContract,ex:isPrecededBy,ex:FL_AccountManager_SelectingCandidate`                                |
| q3 | What are the agents responsible for fulfilling the activities of process Y in the organization X?                                  | What are the agents responsible for fulfilling the activities of the process of hiring an Account Manager in the FL Logistics organization? `ex:Frank`, `ex:Kate` |

## Glossary

![image](coordinate-activities.png)

* **Process Scheme**: A Process Scheme is an entity that represents a set of connected Activity Schemes.
* **Activity Scheme**: An Activity Scheme is a plan for an activity intended to achieve Organizational Goals.
* **Root Activity Scheme**: A Root Activity Scheme is an Activity Scheme origin of a set of connected Activity Schemes and is associated to a Process Scheme.
* **Activity Scheme Dependence**: A relation that refers to the way in which two Activity Schemes are related to each other, and one is affected by the other.
* **Organizational Goal**: see [Create an Organization](https://github.com/HyperAgents/hmas/blob/master/domains/logistics/create-organization/README.md) scenario.
* **Sub-Organizational Goal Relationship**: A relation that refers to a hierarchical relationship between two Organizational Goals. A Sub-Organizational Goal is an Organizational Goal that has to be achieved for the parent Organizational Goal to be achieved.
* **Mission**: A Mission gathers the Organizational Goals that Agents have to achieve in the context of a Process Scheme.
* **Mission Commitment**: A relation that refers to a Mission to which an Agent is committed.
* **Mission Relationship**: A relation that refers to the relationship between two Missions, e.g., _complementary missions_.
* **Mission Incompatibility**: A relation that imposes a constraint in which the same Agent cannot commit to two missions simultaneously.
* **Mission Constraint**: A relation that refers to a constrain imposed on the Mission, e.g., limiting the number of Agents committing to it.
* **Organization**: see [Discover Organizations, their Members and Materials in Hypermedia Environments](https://github.com/HyperAgents/hmas/blob/master/domains/manufacturing-environments/discover-organization/README.md) scenario.
* **Agent**: see [Discover Organizations, their Members and Materials in Hypermedia Environments](https://github.com/HyperAgents/hmas/blob/master/domains/manufacturing-environments/discover-organization/README.md) scenario.

## Recommendations

* The concept of activity can be the execution of a simple action, a complex set of actions, or any other useful arrangement employed to achieve the Organizational Goals. An activity can be represented using, for instance, the [PROV Ontology](https://www.w3.org/TR/prov-o/).

* The **Activity Scheme Dependence** should not be used directly, a sub-property must be created to specify the exact type of dependence between two activity schemes. Examples of dependencies can be temporal dependencies like the [Allen's interval relations](https://doi.org/10.1145/182.358434), spatial dependencies, or other dependencies of influence like _facilitates_ (i.e., an Activity Scheme eases another), _informs_ (i.e., an Activity Scheme advises another), or _prioritizes_ (i.e., an Activity Scheme increases the importance of another).

* There are different ways of implementing the mechanisms to indicate that an **Organizational Goal** has been achieved: (1) associate a specific [Signifier](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-signifiers/README.md) to the Organizational Goal meaning that when the behavior associated to that [Signifier](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-signifiers/README.md) is performed, the Organizational Goal is achieved, (2) define a generic Organizational Goal and generic [Signifier](https://github.com/HyperAgents/hmas/blob/main/domains/manufacturing-environments/discover-signifiers/README.md) allowing Agents to identify the association between them and the Organizational Goal achievement.

* The **Mission Relationship** must not be used directly, a sub-property must be created to specify the exact type of relation being represented between missions.

* The **Mission Incompatibility** and **Mission Constraint** are represented as a SHACL shape instead of an RDF triple. For example, the SHACL shape constraining the number of Agents that can commit to the Mission is

```
ex:MissionCardinalityShape a sh:NodeShape ;
    sh:targetClass hmas:Mission ;
    sh:sparql [
        a sh:SPARQLConstraint ;
        sh:message "The number of agents member of a mission cannot be greater than 1." ;
        sh:prefixes ex:, hmas:, rdfs: ;
        sh:select """
			      SELECT (?agent as $this) (COUNT(?s) as ?c)
            WHERE {
              ?m a ?missionModel ;
                ?s hmas:isMissionOf ?agent .
            }
            HAVING (COUNT(?s) > 1)
			    """ ;
        ] .
```

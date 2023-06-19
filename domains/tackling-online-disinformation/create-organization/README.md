# Create an Organization

## Description
Alice has experience working as a journalist in a reputable news organization, the DPr Network. 
Throughout her career, she has witnessed the growing problem of online disinformation and the negative impact it has on society. 
Motivated to combat these issues on a broader scale, she decides to create her own organization dedicated to tackle online disinformation, the TOD organization. 
Inspired by her experience at the DPr Network, Alice intends to use the News Network organization model based on which the DPr Network organization has been enacted, as reference to organize the TOD organization.

Alice is contained in the News Network workspace, a shared space for news network members, including members of the DPr Network. The workspace also contains a repository artifact that is used for storing and managing organization models. Alice interacts with the repository artifact to retrieve the News Network organization models. 

To ensure the effectiveness of the upcoming TOD organization, she conducts a comparative analysis between the News Network organization model and and other similar organization models, as well as theoretical organization models proposed by experts in the field. She concludes that the News Network organization model provides a solid foundation for the creation of the TOD organization.

Any organization enacted based on the News Network organization model is characterized by the following properties:

+ The organization has the following organizational values:
  + _Accountability_: Accompany information evaluations with details about who contributed to the tackling disinformation process, e.g. which agents evaluated the information. 
  + _Transparency_: Accompany information evaluations with details about how one contributed to the tackling disinformation process, e.g. what external services were used to evaluate the information.
 
+ The organization provides the following roles with their responsibilities:
  1. _Active user_: Evaluate online information or consume the aggregated evaluation of prior active users.
  2. _Journalist_: Evaluate online information (a type of active user).
  3. _General evaluator_: Annotate online information based on the general impression of the information (a type of journalist).
  4. _General investigator_: Annotate online information based on the credibility rating of the information, publishers, authors etc. (a type of journalist).
  5. _Image investigator_: Annotate online information based on the original sources of its images (a type of journalist).
  7. _Admin_: Ensure the functionality of the system, e.g. by assigning missions to groups of agents.
  8. _Aggregator_: Annotate online information based on aggregated evaluations to give a summarized overview of the evaluation results (a type of admin).
  9. _Control_: Control the functionality of the system, e.g. by ensuring that community guidelines are met.

+ The organization proposes the following facility that members of the organization can use to achieve organizational goals:
  + _News network annotating service_: Agents can interact with the facility to search for the original sources of images and annotate online information with the discovered sources.

## Competency Questions

| ID | Question in Natural Language | Example |
|----|------------------------------|---------|
| q1 | What are the available organization models that can be used to create a new organization? | What are the available organization models that can be used by Alice to create the TOD organization? `ex:NewsNetwork`, `ex:Manufacturing`    |
| q2 | What are the elements composing a given organization model?  | What are the elements composing the News Network organization model? `ex:ActiveUser`, `ex:Journalist`, `ex:GeneralEvaluator`, `ex:GeneralInvestigator`, `ex:ImageInvestigator`, `ex:Admin`, `ex:Aggregator`, `ex:Control`, `ex:ContentEvaluationMission`, `ex:ArticleCredibilityMission`, `ex:ImageProvenanceMission`, `ex:SystemFunctionalityMission`, `ex:ControlMission`, `ex:NewsNetworkAnnotatingService`       |
| q2 | What are the organizational values of an organization that is enacted based on a given organization model?  | What are the organizational values of an organization that is enacted based on the News Network organization model? `ex:Accountability`, `ex:Transparency`   |
| q4 | What are the roles provided by an organization that is enacted based on a given organization model?  | What are the roles provided by an organization that is enacted based on the News Network organization model? `ex:ActiveUser`, `ex:Journalist`, `ex:GeneralEvaluator`, `ex:GeneralInvestigator`, `ex:ImageInvestigator`, `ex:Admin`, `ex:Aggregator`, `ex:Control` |
| q5 | What are the missions proposed by an organization that is enacted based on a given organization model?     | What are the missions proposed by an organization that is enacted based on the News Network organization model? `ex:ContentEvaluationMission`, `ex:ArticleCredibilityMission`, `ex:ImageProvenanceMission`, `ex:SystemFunctionalityMission`, `ex:ControlMission`                                                   |
| q6 | What are the facilities proposed by an organization that is enacted based on a given organization model?   | What are the facilities proposed by an organization that is enacted based on the News Network organization model? `ex:NewsNetworkAnnotatingService`                                     |

## Glossary

* **Organization Model**: see [Create an Organization](https://github.com/HyperAgents/ns.hyperagents.org/tree/master/domains/logistics/create-organization/README.md) scenario.
* **Organizational Value**: see [Create an Organization](https://github.com/HyperAgents/ns.hyperagents.org/tree/master/domains/logistics/create-organization/README.md) scenario.
* **Role**: see [Create an Organization](https://github.com/HyperAgents/ns.hyperagents.org/tree/master/domains/logistics/create-organization/README.md) scenario.
* **Mission**: see [Create an Organization](https://github.com/HyperAgents/ns.hyperagents.org/tree/master/domains/logistics/create-organization/README.md) scenario.
* **Facility**: see [Create an Organization](https://github.com/HyperAgents/ns.hyperagents.org/tree/master/domains/logistics/create-organization/README.md) scenario.
* **Organization**: see [Discover Organizations, their Members and Materials in Hypermedia Environments](https://github.com/HyperAgents/ns.hyperagents.org/blob/master/domains/manufacturing-environments/discover-organization/README.md) scenario.
* **Agent**: see [Discovery of Workspaces, Agents, and Artifacts in Hypermedia Environments](https://github.com/HyperAgents/ns.hyperagents.org/blob/master/domains/manufacturing-environments/discover-core/README.md) scenario.
* **Artifact**: see [Discovery of Workspaces, Agents, and Artifacts in Hypermedia Environments](https://github.com/HyperAgents/ns.hyperagents.org/blob/master/domains/manufacturing-environments/discover-core/README.md) scenario.
* **Workspace**: see [Discovery of Workspaces, Agents, and Artifacts in Hypermedia Environments](https://github.com/HyperAgents/ns.hyperagents.org/blob/master/domains/manufacturing-environments/discover-core/README.md) scenario.

## Recommendations

In the hypermedia environment, agents can discover organization models in order to examine the modeling choices of existing organizations or create new organizations using the discovered organization models. This can be achieved through various methods, including:
- Interacting with shared artifacts that offer the possibility to retrieve, store, and manage organization models. 
- Interacting with artifacts that are materials of organizations themselves, and they offer the possibility to retrieve, store, and manage the organization models of their associated organizations.
- Discovering organization models through the resource profiles of the organizations that are enacted based on these models. 

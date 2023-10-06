# Configuring the Physical Context within an Organization

## Description

In the FL Logistics organization, activities take place on various depots. Those depots are located in France and in Switzerland. Complementing the job positions and departments that structure the FL Logistics organization, dedicated configurations on each of these depots enables the coordination and regulation of the activities of the organization members and materials. These configurations, in relation to the physical places where the activities of the organization take place, are complementary to the social structure of FL Logistics.

In France, the activities of the FL Logistics are organized around three physical workspaces: Lyon Depot, Saint-Etienne Depot and Transport Zone between both depots.

In each configuration, agents will undertake activities according to their *memberships to* that *configuration* and to the artefacts through their memberships as *facilities* in that *configuration*.

Two configurations are considered:
* *picking* configuration with a *collector* role and a *picking area* facility
* *receiving* configuration with a *deliverer* role and an *receiving area* facility

The Transport Zone doesn't have any configuration to further coordinate and regulate its activities.

These configurations are used by the agents acting and facilities available in the *lyon depot*, *saint-etienne depot* workspaces as follows:
* *lyon depot* with *picking* and *receiving* configurations
* *saint-etienne depot* with the two same types of configurations: *picking* and *receiving*

The agents having a membership in the *transporter* group use these configurations in the *lyon depot* and *saint-etienne depot* to help their coordination: when getting a membership in the *delivering* (resp. *picking*) configuration through the *deliverer* role (resp. *collector* role).

In the same approach, the *delivering machine* and *picking machine* artifacts materials of FL logistics organization, operating in these workspaces, will be accessed through dedicated facilities of these configurations, providing selected set of actions to the agents: the *delivering machine* artifact is considered as an *receiving* area facility in the *receiving* configuration; the *picking machine* artifact is considered as a *picking area* facility in the *picking* configuration.

Activities will take place according to the configurations that lead to picking, unpicking and transporting actions with different artifacts. Goods are collected using different facilities and are delivered with other facilities according to the plan elaborated by the agent having a membership of planner in the corresponding group.

## Competency questions

| ID | Question in Natural Language | Example |
|----|------------------------------|---------|
| q1 | What are the memberships that an agent of FL Logistics can have in configuration X? | `ex:SL_Collector in ex:SL_Picking, ex:SL_Deliverer in ex:SL_Receiving` |
| q2 | What are the possible configurations of FL Logistics? | `ex:SL_Picking, ex:SL_Receiving` |
| q3 | What are the facilities that artifacts can have in configuration X? | `ex:SL_PickingArea in ex:SL_Picking`, `ex:SL_ReceivingArea in ex:SL_Receiving` |
| q4 | What are the agents that have a membership in the configuration X? | |

## Glossary

![image](configure-organization.png)

* **Configuration**: A Configuration denotes the distributed articulation of facilities (i.e., Artifacts) and roles (i.e., Agents) enacted from the Configuration definition. Configurations may have interaction relations between them constraining the way agents can access to them (e.g. compatibility, i.e. being part of both configurations, ...).
* **Membership**: see [Structure the Social Context within an Organization](https://github.com/HyperAgents/hmas/blob/master/domains/logistics/structure-organization/README.md) scenario.
* **Facility**: see [Create an Organization](https://github.com/HyperAgents/ns.hyperagents.org/blob/master/domains/logistics/create-organization/README.md) scenario.
* **Role**: see [Create an Organization](https://github.com/HyperAgents/ns.hyperagents.org/blob/master/domains/logistics/create-organization/README.md) scenario.
* **Organization**: see [Discover Organizations, their Members and Materials in Hypermedia Environments](https://github.com/HyperAgents/hmas/blob/master/domains/manufacturing-environments/discover-organization/README.md) scenario.
* **Agent**: see [Discover Organizations, their Members and Materials in Hypermedia Environments](https://github.com/HyperAgents/hmas/blob/master/domains/manufacturing-environments/discover-organization/README.md) scenario.
* **Artifact**: see [Discover Organizations, their Members and Materials in Hypermedia Environments](https://github.com/HyperAgents/hmas/blob/master/domains/manufacturing-environments/discover-organization/README.md) scenario.

## Recommendations

* When spatial context is expressed as a condition, the condition is tested against the current situation and, if satisfied, activates the policy. The agent didn't make an explicit and intentional decision to realize the satisfaction of the context condition.
* When spatial context is expressed as a configuration with memberships, the agent makes an explicit move or decision to acquire that specific membership. We are able to capture the explicit decision or commitment of the agent w.r.t. this membership.

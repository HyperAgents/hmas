# Configuring an Organization

## Description

In the FL Logistics organization, activities take place on various depots located in France and in Switzerland. In all depots, there are a _receiving_ area, a _storage_ area, and a _picking_ area.

In each _receiving_ area, there are available standard material handling equipment like forklifts and pallet jacks as well as barcode readers to gain maximum efficiency.


Complementing the job positions and departments that structure the FL Logistics, dedicated configurations arrange these physical organization workplaces where activities can be undertaken. 

Artifacts situated in these 

The usage of these configurations identifies the 

usages enable identifying the possible uses of artifacts situated in these depots. These configurations, e.g., arrangement of the physical workplaces where activities of the organization can take place, are complementary to the social structure and activity coordination of the FL Logistics.

In France, the FL Logistics' activities can take place in three physical workplaces: Lyon Depot, Saint-Etienne Depot and Transport Zone between both depots.

In each configuration, agents can undertake their activities using the available facilities attached to artifacts.

Two configurations are considered:

* *picking* configuration with a *collector* usage and a *picking area* facility
* *receiving* configuration with a *deliverer* usage and an *receiving area* facility

The agents acting in the *lyon depot*, *saint-etienne depot* workspaces have to consider both depots according to those two configurations. In the Transport Zone the agents don't have to consider any configuration to further coordinate and regulate their activities.

The agents having a membership in the *transporter* group use these configurations in the *lyon depot* and *saint-etienne depot* to help their coordination: when committing to a usage in the *delivering* (resp. *picking*) configuration through the *deliverer* usage (resp. *collector* usage).

In the same approach, the *delivering machine* and *picking machine* artifacts materials of FL logistics organization, operating in these workspaces, will be accessed through dedicated facilities of these configurations, providing selected set of actions to the agents: the *delivering machine* artifact is considered as an *receiving area* facility in the *receiving* configuration; the *picking machine* artifact is considered as an *picking area* facility in the *picking* configuration.

Activities will take place according to the configurations that lead to picking, unpicking and transporting actions with different artifacts. Goods are collected using different facilities and are delivered with other facilities according to the plan elaborated by the agent having a membership of planner in the corresponding group.

## Competency questions

| ID | Question in Natural Language | Example |
|----|------------------------------|---------|
| q1 | What are the usage that an agent A of organization X can have in configuration Y? | |
| q2 | What are the possible configurations of organization X?                           | |
| q3 | What are the facilities that artifacts X can have in configuration Y?             | |
| q4 | What are the agents that are part of the usage Z in the configuration X?          | |

## Glossary

![image](configure-organization.png)

* **Usage**: A Usage identifies the Facilities associated to Artifacts that Agents can use in a Configuration.
* **Usage Incompatibility**: A relation that imposes a constraint in which the same Agent cannot be part of two Usages simultaneously.
* **Usage Constraint**: A relation that refers to a constrain imposed on the Usages, e.g., limiting the number of Agents participating in that Usage.
* **Configuration**: A Configuration is an arrangement of elements (physical or logical) of an Organization.
* **Configuration Connectedness**: A relation that refers how two Configurations are linked.
* **Facility**: see [Create an Organization](https://github.com/HyperAgents/ns.hyperagents.org/blob/master/domains/logistics/create-organization/README.md) scenario.
* **Organization**: see [Discover Organizations, their Members and Materials in Hypermedia Environments](https://github.com/HyperAgents/hmas/blob/master/domains/manufacturing-environments/discover-organization/README.md) scenario.
* **Agent**: see [Discover Organizations, their Members and Materials in Hypermedia Environments](https://github.com/HyperAgents/hmas/blob/master/domains/manufacturing-environments/discover-organization/README.md) scenario.
* **Artifact**: see [Discover Organizations, their Members and Materials in Hypermedia Environments](https://github.com/HyperAgents/hmas/blob/master/domains/manufacturing-environments/discover-organization/README.md) scenario.

## Recommendations

* https://www.jstor.org/stable/pdf/2563428.pdf?refreqid=fastly-default%3A1bf3cc6b0c876a22b471ab9a58a68da2&ab\_segments=&origin=&initiator=&acceptTC=1
* In the OntoZoning ontology (https://pdf.sciencedirectassets.com/312220/1-s2.0-S2226585623X0003X/1-s2.0-S2226585623000067/main.pdf?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQD%2F0cOO8Ci1dle6bP1t%2FMdy4%2Bpe5poMgoopD9KLVOKZlgIgQN0XVkKb9wvSk14qb4EVsRb6ROOHGNHBgJGJqTKgfu4qswUIMhAFGgwwNTkwMDM1NDY4NjUiDIIWg3I77gLJsk%2F21SqQBa4FtRSZAPGt0FoJmh8yQAC7Qb9d3AzUs3YJLPgDtScksnYLFY5UQgZzD9OroSCSj7gnc2Ft0OvIXJmuwOmAyd9thOFTA9weqJICqwSzsZSd%2Fc6LxGMU655JstjmBKscftYvFd8nJx7sXgoEJ5wzjih3J3oYapBlVIGFeUB9%2F2N5zazM%2FDpS5jourS%2BNViRobzfF5kLEiQ2gTZeovELSb8gyGjIWk%2Bw0jtr5MGiUh6EZp8RsMFuXDpLGAhLK7oRljl7ALkORfG4KjFjY5QLcoYyA42rLM75sGhD4znEBmUTvdr7%2BWdr16WUZYFmumV2L97oo8u5kvVw9FfKOjfcSqAC7TVsP20%2FshubhiH1pLyEkM4gaWXrax1OF1LiThKVUYUuV5nFDG0DUedPZHtuWxhj%2F%2FQe2tT066GJXUPcVesocDdXPwlOaHmRrxyPIDU1bqwSnPsYqIifxPspvZfRQJYZjNfcQxURY03jK50GkE8ymPiVSq%2BbRvugLZ5qtGqVKpSWaZvMuDaNafK2eIK%2FC5EVEnLAYUxllglOiCHiDKxX4Y175vGSJ5jDG9Wfy696ntm082iXtFpi4Nby%2FJ3x9kzIhbq9sIGCot7y8HtiaeuG5ay0UTmgeOuCHYOC2sZRD%2BWfJGQWlZaVz789UWLnzzfckhPulm8isYToRUtyuUSrem3D6NfTmRBXZrf8wsSmC1SLYFsvYMls56tXMdl2GXGyOWSGDUtgCRzxkbjQRcXg0YA4NsBHVpp68GbkhD499AITOBjwRS40mjDdI6hhcL7WSInfH76H3AoObYW2%2Fsc6g4OoRGVW4sKtj%2FRvbF4bCZzEF8m4Z%2FhLnmqobf4FKhMYuUg8zIiflI05DVxR4ArMNMJm2rasGOrEBHs1ckoRfpYQ%2BKnxKGjf7HFGJOnn6Njzd7Du71UJ%2FMRwgF98xsrw8ktkjnLONhsY0cfjtkPkV5Gh453Ywg8xTJD%2BIZNQQpEZW479lorH8y1r8XWFhawHdnjDufnFn0mCGhS3oCnC%2FCA24E6A1KEebuk3ige4YNPB455FUeXjiCTxZYj3bfNqjkBbYBHnkUdIKCC9IuWE%2BSdsOOxYaogpDNTKoTxUluFBzsqa2IC%2FiY%2BXL&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231202T165011Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAQ3PHCVTYSOMH3THG%2F20231202%2Fus-east-1%2Fs3%2Faws4\_request&X-Amz-Signature=cc3679c26353699d369beba87b57856ecb2f272315a10967be78fea065616090&hash=c2d10e1950ff4bf5ea88d0a505d35a055c7b89b4fb0e6df8700dbbf8cea13091&host=68042c943591013ac2b2430a89b270f6af2c76d8dfd086a07176afe7c76c2c61&pii=S2226585623000067&tid=spdf-fedd5843-00fd-4a6c-8cb8-467b6d73b38a&sid=1d4d608a37af8745d508f165995130d0d4b8gxrqb&type=client&tsoh=d3d3LnNjaWVuY2VkaXJlY3QuY29t&ua=1c145b530854555556520a&rr=82f51140ea9a03fd&cc=fr) use of other terms *Zoning*, *Land use*, *Programme*
* The Configuration (better named Workspace Configuration) is targeting the regulation of the use or workspace by agents in a hmas application. That is to say: the regulation of accessing/using artifacts through their signifiers (abstracted as facilities). This workspace configuration should be complemented at some point with `landmarks` with geospatial coordinate properties, regulating the places agents can be situated at. OLD ToBeSuppressed: When spatial context is expressed as a condition, the condition is tested against the current situation and, if satisfied, activates the policy. The agent didn't make an explicit and intentional decision to realize the satisfaction of the context condition.
* OLD ToBeSuppressed: When spatial context is expressed as a configuration with memberships, the agent makes an explicit move or decision to acquire that specific membership. We are able to capture the explicit decision or commitment of the agent w.r.t. this membership.

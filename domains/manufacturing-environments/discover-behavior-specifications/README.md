# Discover Behavior Specifications

Feature: Discovery of Behavior Specifications


## Description
An agent is situated in a manufacturing workspace that contains a robotic arm artifact. The agent has discovered a signifier in the profile of the artifact that reveals information about the affordance resetable, which affords the agent to reset the state of the robotic arm.

The agent has the objective of resetting the robotic arm based on the discovered signifier. The signifier reveals information about the specification of a behavior — here, the specification of an action that the agent can execute to exploit the affordance resetable. The specification specifies a form that implements the action.

The agent provides the expected input and uses the form in order to reset the robotic arm. 

## Competency Questions

| ID | Question in Natural Language | Example |
|----|------------------------------|---------|
| q1 | What are the action specifications that signifiers of a given resource profile signify?          | |
| q2 | What is the action specification that that a given signifier signifies?                          | |
| q3 | What are the forms that implement a given specified action?                                      | |
| q4 | What are the forms that implement a given specified action?                                      | |

## Glossary
- Behavior (https://purl.org/hmas/interaction#Behavior): A course of action (i.e., an ordered process, a succession of actions, a pattern of activity) that is performed by an agent when exploiting an affordance. (e.g., the execution of an AgentSpeak plan, or a behavior as defined in subsumption architecture, or a JADE behavior).
-	ActionExecution (https://purl.org/hmas/interaction#ActionExecution): A behavior that is the execution of exactly one action.
-	BehavioralSpecification (https://purl.org/hmas/interaction#BehavioralSpecification): A specification that specifies a behavior.
-	ActionSpecification (https://purl.org/hmas/interaction#ActionSpecification): A specification that specifies how to execute an action.
-	signifies (https://purl.org/hmas/interaction#signifies): A relation between a behavior and a signifier that signifies it.
-	hasForm (https://purl.org/hmas/interaction#hasForm): A relation between an action specification and a form (https://www.w3.org/2019/wot/hypermedia#Form) that describes an implementation of the specified action.
-	hasAction (https://purl.org/hmas/interaction#hasAction): A relation between a behavioral specification and the specification of an action whose execution is part of the specified behavior.
-	Signifier (https://purl.org/hmas/core#Signifier): see [_Other scenario TBA_]().

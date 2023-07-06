# Discover Behavior Specifications

Feature: Discovery of Behavior Specifications


## Description
An agent is situated in a manufacturing workspace that contains a robotic arm artifact. In the same workspace, a signifier signifies information about how to exploit a behavior possibility offered by the robotic arm artifact, specifically, information about how to move the gripper of the robotic arm. This information specifies a set of contraints on how to execute the action of moving the gripper:
- the action execution should have an [`onto:GripperJoint`](https://ci.mines-stetienne.fr/kg/ontology#GripperJoint) as input;
- the action execution should use on of the following hypermedia controls: 
  - a form describing an HTTP request,
  - a form describing a request based on the Constrained Application Protocol (CoAP).

The agent discovers the signifier, that is exposed in the profile of the robotic arm artifact. Based on the signified information, the agent moves the gripper by providing an [`onto:GripperJoint`](https://ci.mines-stetienne.fr/kg/ontology#GripperJoint) as input, and sends an HTTP request based on one of the forms.
 
## Competency Questions

| ID | Question in Natural Language | Example                                                                                                                                   |
|----|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| q1 | What is the action execution specification that a given signifier signifies? | Specification that signifier `ex:gripperMovable` signifies: `ex:moveGripperShape`  |
| q2 | What are the constraints on the input that an action execution should have based on a given specification? | Constaints on the input that the execution of moving the gripper should have based on `ex:moveGripperShape`: `ex:gripperJointShape` |
| q3 | What is the type of the input that an action execution should have based on a given specification? | Type of the input that the execution of moving the gripper should have based on `ex:moveGripperShape`: `onto:GripperJoint` |
| q4 | What are the properties that the input of an action execution should have based on a given specification? | Properties of the input that the execution of moving the gripper should have based on `ex:moveGripperShape`: `ex:hasGripperValue` |
| q5 | What are forms that an action execution should use based on a given specification?  | Forms that the execution of moving the gripper should use based on `ex:moveGripperShape`: `ex:httpForm`, `ex:coapForm` |



## Glossary
- **Behavior Execution**: A course of action performed by an agent upon exploiting a behavior possibility.
- **Action Execution**: A behavior execution that is the execution of exactly one context-free action, e.g. of a context-free HTTP request.
- **Input**: An input of an action, for example, in the representation of an action execution.
- **Form**: A hypermedia control that describes how to execute an action as defined here, for example, an [`hctl:Form`](https://www.w3.org/2019/wot/hypermedia#Form).
- **Signification of Behavior**: The act of revealing information about how to exploit a behavior possibility.
- **Signifier**: see [Discovery of Signifiers](../discover-signifiers/README.md).
- **Signifier Exposure**: see [Discovery of Signifiers](../discover-signifiers/README.md).
- **Situatedness**: see [Discovery of Signifiers](../discover-signifiers/README.md).
- **Workspace**: see [Discovery of Workspaces, Agents, and Artifacts in Hypermedia Environments](../discover-core/README.md).
- **Resource Containment**: see [Discovery of Workspaces, Agents, and Artifacts in Hypermedia Environments](../discover-core/README.md).
- **Artifact**: see [Discovery of Workspaces, Agents, and Artifacts in Hypermedia Environments](../discover-core/README.md).
- **Agent**: see [Discovery of Workspaces, Agents, and Artifacts in Hypermedia Environments](../discover-core/README.md).
- **Resource Profile**: see [Discovery of Workspaces, Agents, and Artifacts in Hypermedia Environments](../discover-core/README.md).


## Recommendations
- A signifier can signify a behavior specification for revealing information about how to exploit the relevant behavior possibility.
- This scenario focuses on signifying a behavior specification that is the specification of exactly one action. However, a signifier may concern a behavior that is more generic than a single action execution. In the latter case, implementation details (e.g. an [`hctl:Form`](https://www.w3.org/2019/wot/hypermedia#Form)) will remain attached directly to the actions of the specified behavior, and not the behavior specification itself. The above aim to the following:
  -	To enable the action-oriented design of hypermedia by keeping the implementation details attached to a specified action, considering that this is a simple design style, and a style easily relatable to how signifiers are used on the Web.
  - To preserve the freedom of designers to create signifiers that concern behaviors with higher-level semantics on top of actions. 
  - To enable extension points for defining behaviors based on how human agents reason about action and perform behaviors when exploiting behavior possibilities. 

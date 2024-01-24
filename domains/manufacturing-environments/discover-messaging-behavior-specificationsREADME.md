# Discover Behavior Specifications for Sending Messages to Agents
Feature: Discovery of Behavior Specifications for Sending Messages to Agents


## Description
Two agents are situated in a manufacturing workspace: Agent A manages the scheduling of production goals. Agent B operates a robotic arm artifact, that is contained in the workspace, towards achieving production goals. Agent A knows that Agent B is situated in the same workspace, and discovers a signifier that reveals information about how to send a message to Agent B for requesting to move the gripper of the robotic arm artifact.
Agent A discovers the signifier that is exposed in the resource profile of Agent B, which reveals information about how to send a [FIPA Request](http://www.fipa.org/specs/fipa00037/SC00037J.html#_Toc26729708) message to Agent B. This information specifies a set of contraints on how to execute the action of sending the message: 
- the action execution should have a [FIPA ACL Message](http://www.fipa.org/specs/fipa00061/SC00061G.html) as input;
- the action execution should use an HTTP form based on the [FIPA Agent Message Transport Protocol for HTTP](http://www.fipa.org/specs/fipa00084/XC00084C.html);
- The action execution may be part of a behavior execution that is specified in the [FIPA Request Interaction Protocol Specification](http://www.fipa.org/specs/fipa00026/SC00026H.html)

Agent A executes the action by sending a message to Agent B, where the message has the following parameters:
- Agent A as sender 
- Agent B as receiver 
- the Request Communicative Act from the [FIPA Communicative Act Library](http://www.fipa.org/specs/fipa00037/SC00037J.html) as performative 
- An Action Execution specification as content 
- The [FIPA SL Content Language](http://www.fipa.org/specs/fipa00008/SC00008I.html) as language of the content 

Agent B receives the message, and by interpreting the sender of the message, it retrieves the resource profile of Agent A. Agent B discovers the signifiers that are exposed in the resource profile of Agent A, which reveal information about how to send FIPA Agree and FIPA Refuse messages to Agent A.

 
## Competency Questions

| ID | Question in Natural Language                                                                                              | Example                                                                                                                   |
|----|---------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| q1 | What are the signifiers that are exposed by a given resource profile, and that reveal information about how to send a message? | Signifier exposed in the profile `ex:agentBProfile` that reveals information about how to send a `fipa:ACLMessage`: `ex:agentBProfile` |                                      |
| q2 | What is the action execution specification that a given signifier signifies? | Action execution specification that the signifier `ex:requestable` signifies: `ex:requestActionSpecification`|
| q3 | What is the specification of the input based on a given action execution specification? | Specification of the input based on the action execution specification `ex:requestActionSpecification`: `ex:requestMessageSpecification` |
| q4 | What are the types of the input that an action execution should have based on a given action execution specification? | Type of the input that the action execution should have based on the action execution specification `ex:requestActionSpecification`: `fipa:ACLMessage`| 
| q5 | What are the properties that the input of an action execution should have based on a given action execution specification? | Properties that the input of an action execution should have based on the action execution specification `ex:requestActionSpecification`: `fipa:hasSender`, `fipa:hasReceiver`, `fipa:hasPerformative`, `fipa:hasContent`, `fipa:hasLanguage` |
| q6 | What is the suprotocol that an action execution should use based on a given action execution specification? | Subprotocol that an action execution should use based on the action execution specification `ex:requestActionSpecification`: "fipa.mts.mtp.http.std" |
| q7 | What are the types of a behavior execution in which a given specified action execution is included? | Types of a behavior execution in which an action execution specified in the action execution specification `ex:requestActionSpecification` is included: `fipa:RequestInteractionProtocolEnactment`, `dul:PlanExecution` |  

## Glossary
- **Message**: The individual unit of communication between two or more agents.
- **Subrotocol**: An extension mechanism to a transport protocol [1], such as the [FIPA Agent Message Transport Protocol for HTTP](http://www.fipa.org/specs/fipa00084/XC00084C.html), that can be, for example, specified as part of the hypermedia control (e.g. an [hctl:Form](https://www.w3.org/2019/wot/hypermedia#Form)) describing how to execute an action.
- **Agent Interaction Protocol**: A specification of interaction between two or more autonomous agents that serves as a standard of correctness for agent behavior in a multi-agent system [2].
- **Action Execution as part of a Behavior Execution**: An action exection that takes place upon the execution of a (more complex) behavior, for example, as part of the execution of a plan, or of the enactment of an agent interaction protocol.
- **Behavior Execution**: see [Discovery of Behavior Specifications](../discover-behavior-specifications/README.md).
- **Action Execution**: see [Discovery of Behavior Specifications](../discover-behavior-specifications/README.md).
- **Input**: see [Discovery of Behavior Specifications](../discover-behavior-specifications/README.md).
- **Form**: see [Discovery of Behavior Specifications](../discover-behavior-specifications/README.md).
- **Signification of Behavior**: see [Discovery of Behavior Specifications](../discover-behavior-specifications/README.md).
- **Signifier**: see [Discovery of Signifiers](../discover-signifiers/README.md).
- **Signifier Exposure**: see [Discovery of Signifiers](../discover-signifiers/README.md).
- **Situatedness**: see [Discovery of Signifiers](../discover-signifiers/README.md).
- **Workspace**: see [Discovery of Workspaces, Agents, and Artifacts in Hypermedia Environments](../discover-core/README.md).
- **Resource Containment**: see [Discovery of Workspaces, Agents, and Artifacts in Hypermedia Environments](../discover-core/README.md).
- **Artifact**: see [Discovery of Workspaces, Agents, and Artifacts in Hypermedia Environments](../discover-core/README.md).
- **Agent**: see [Discovery of Workspaces, Agents, and Artifacts in Hypermedia Environments](../discover-core/README.md).
- **Resource Profile**: see [Discovery of Workspaces, Agents, and Artifacts in Hypermedia Environments](../discover-core/README.md).

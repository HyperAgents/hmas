# Discover Behavior Specifications

Feature: Discovery of Behavior Specifications


## Description
An agent A is situated in a manufacturing workspace that contains a robotic arm artifact. The resource profile of the robotic arm artifact exposes a signifier S that reveals information about a behavior possibility ⁠—⁠ it signifies a specification SP describing how to move the gripper of the robotic arm artifact. Specifically, the SP describes the behavior of moving the gripper as an action that:
- is of type [onto:SetGripper](https://ci.mines-stetienne.fr/kg/ontology#SetGripper),
- expects an input I of a schema [onto:GripperJoint](https://ci.mines-stetienne.fr/kg/ontology#GripperJoint), and 
- can be executed based on a set of hypermedia controls. The set of hypermedia controls contains two forms ⁠—⁠ a form describing an HTTP request, and a form describing a CoAP request.

Agent A has discovered the exposed signifier and has the objective of behaving based on the signified specification. For this, agent A provides an input of the schema [onto:GripperJoint](https://ci.mines-stetienne.fr/kg/ontology#GripperJoint), and sends an HTTP request based on one of the hypermedia controls. 

## Competency Questions

| ID | Question in Natural Language | Example |
|----|------------------------------|---------|
| q1 | What are the behavior specifications that a given signifier signifies?           |What are the behavior specifications that signifier S signifies?|
| q2 | What are the action specifications that a given signifier signifies?             |What are the action specifications that signifier S signifies?|
| q3 | What are the forms that describe how to execute a given specified action?        |What are the forms that describe how to execute moving the gripper of the robotic arm artifact based on SP?|
| q4 | What is the input that is expected by a given specified action?                  |What is the input that is expected for moving the gripper of the robotic arm artifact based on SP?|
| q5 | What are the schemas of a given expected input?                                  |What are the schemas of the expected input I?|


## Glossary
- **Behavior Execution**: A course of action performed by an agent upon exploiting a behavior possibility.
-	**Action Execution**: A behavior execution that is the execution of exactly one context-free action, e.g. of a context-free HTTP request. 
-	**Behavior Specification**: A specification that describes a behavior, for example, as procedural knowledge (e.g., AgentSpeak plan) or code-on-demand (e.g., a script that implements a behavior).
-	**Action Specification**: A specification that describes an action (e.g., through preconditions and postconditions) and how to execute the action, e.g. as a context-free request through a form.
-	**Form**: A hypermedia control that describes how to execute an action as defined here: https://www.w3.org/2019/wot/hypermedia#Form.
-	**Input**: An input of an action, which may include variables. The input may be used, for instance, in an action specification or in the representation of an action execution.
- **Schema**: The schema of an input. For example, the schema may be a JSON data schema (https://www.w3.org/2019/wot/json-schema#DataSchema) or a SHACL shape (http://www.w3.org/ns/shacl#Shape).
- **Signification of Behavior**: The act of revealing information about how to exploit a behavior possibility. 


## Recommendations
- A signifier can signify a behavior specification for revealing information about how to exploit the relevant behavior possibility.
- This scenario focuses on the signification of a behavior specification that is the specification of exactly one action. However, a signifier may concern a behavior that is more generic than a single action execution. In the latter case, implementation details (e.g. an [hctl:Form](https://www.w3.org/2019/wot/hypermedia#Form)) will remain attached directly to the actions of the specified behavior, and not the behavior specification itself. The above aim to the following:
  -	To enable the action-oriented design of hypermedia by keeping the implementation details attached to a specified action, considering that this is a simple design style, and a style easily relatable to how signifiers are used on the Web.
  - To preserve the freedom of designers to create signifiers that concern behaviors with higher-level semantics on top of actions. 
  - To enable extension points for defining behaviors based on how human agents reason about action and perform behaviors when exploiting behavior possibilities. 

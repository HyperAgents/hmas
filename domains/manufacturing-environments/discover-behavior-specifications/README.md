# Discover Behavior Specifications

Feature: Discovery of Behavior Specifications


## Description
An agent A is situated in a manufacturing workspace that contains a robotic arm artifact. The resource profile of the robotic arm artifact exposes a signifier that reveals information about a behavior possibility ⁠—⁠ it signifies a specification describing how to move the gripper of the robotic arm artifact. Specifically, the specification describes the behavior of moving the gripper as an action that:
- is of type [onto:SetGripper](https://ci.mines-stetienne.fr/kg/ontology#SetGripper),
- expects an input of a schema [onto:GripperJoint](https://ci.mines-stetienne.fr/kg/ontology#GripperJoint), and 
- can be executed based on a set of hypermedia controls. The set of hypermedia controls contains two forms ⁠—⁠ a form describing an HTTP request, and a form describing a CoAP request.

Agent A has discovered the exposed signifier and has the objective of behaving based on the signified specification. For this, agent A provides an input of the schema [onto:GripperJoint](https://ci.mines-stetienne.fr/kg/ontology#GripperJoint), and sends an HTTP request based on one of the hypermedia controls. 

## Competency Questions

| ID | Question in Natural Language | Example |
|----|------------------------------|---------|
| q1 | What are the behavior specifications that a given signifier signifies?           | |
| q2 | What are the action specifications that a given signifier signifies?             | |
| q3 | What are the forms that describe how to execute a given specified action?        | |
| q4 | What is the input that is expected by a given specified action?                  | |
| q5 | What are the schemas of a given expected input?                                  | |


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
A signifier can signify a behavior specification for revealing information about how to exploit the relevant behavior possibility.

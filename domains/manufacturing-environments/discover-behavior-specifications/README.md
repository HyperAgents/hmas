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
- **Behavior Execution**: A course of action performed by an agent upon exploiting a behavior possibility.
-	**Action Execution**: A behavior execution that is the execution of exactly one context-free action, e.g. of a context-free HTTP request. 
-	**Behavior Specification**: A specification that specifies a behavior, for example, as procedural knowledge (e.g., AgentSpeak plan) or code-on-demand (e.g., a script that implements a behavior).
-	**Action Specification**: A specification that describes an action (e.g., through preconditions and postconditions) and how to execute the action, e.g. as a context-free request through a form.
-	**Form**: A hypermedia control that describes how to execute an action as defined here: https://www.w3.org/2019/wot/hypermedia#Form.
-	**Input**: An input of an action, which may include variables. The input may be used, for instance, in an action specification or in the representation of an action execution.
- **Schema**: The schema of an input. For example, the schema may be a JSON data schema (https://www.w3.org/2019/wot/json-schema#DataSchema) or a SHACL shape (http://www.w3.org/ns/shacl#Shape).

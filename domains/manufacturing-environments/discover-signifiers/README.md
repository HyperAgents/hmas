# Discover Signifiers

Feature: Discovery of Signifiers


## Description
An agent is situated in a manufacturing workspace that contains  industrial artifacts, e.g. industrial devices. The agent discovers signifiers in the workspace, that reveal information about the affordances offered to the agent by the industrial artifacts. 

The agent may search for all the signifiers in the manufacturing workspace, or for all the signifiers exposed in a specific artifact profile, such as the profile of a robotic arm. (The related affordances may be currently exploitable by the agent or not).

## Competency Questions

| ID | Question in Natural Language | Example |
|----|------------------------------|---------|
| q1 | What are the signifiers with a given IRI?                            | |
| q2 | What are the signifiers exposed in the profile of a given artifact?  | |
| q3 | What are the signifiers available in a given workspace?              | |

## Glossary
-	**Signifier**: A perceivable sign/cue that can be interpreted meaningfully by an agent to reveal information about behavior possibilities.
-	**Signifier Exposure**: The condition of signfiers being available in the environment, and the act of making signifiers available in the environment.
-	**Resource Profile**: see [_Other scenario TBA_]().
-	**Artifact**: see [_Other scenario TBA_]().
-	**Workspace**: see [_Other scenario TBA_]().

## Recommendation 
- The resource profile of an artifact can expose signifiers which reveal information about behavior possibilities offered by the artifact.
- Agent can discover and interpret exposed signifiers to receive information about:
   1. how to exploit behavior possibilities;
   2. under which circumstances to exploit behavior possibilities.

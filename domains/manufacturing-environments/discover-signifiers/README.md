# Discover Signifiers

Feature: Discovery of Signifiers


## Description
An agent is situated in a manufacturing workspace that contains industrial artifacts, e.g. industrial devices, and other agents. The agent is responsible for operating a robotic arm artifact in the workspace, and cooperating with the other agents towards achieving production goals. For this, the agent has the objective of discovering signifiers, i.e. cues in the workspace that reveal information about how to interact with the robotic arm artifact and the other agents.

The agent discovers signifiers exposed in the profile of the robotic arm that is contained in the workspace, and signifiers exposed in the profile of an agent whose body is contained in the workspace.

## Competency Questions

| ID | Question in Natural Language | Example |
|----|------------------------------|---------|
| q1 | What are the signifiers exposed in a given resource profile?                          | |
| q2 | What are the signifiers exposed in resource profiles contained in a given workspace?  | |
| q3 | What are the signifiers exposed in resource profiles of a given artifact?             | |
| q4 | What are the signifiers exposed in resource profiles of a given agent?                | |

## Glossary
-	**Signifier**: A perceivable sign/cue that can be interpreted meaningfully by an agent to reveal information about behavior possibilities.
-	**Signifier Exposure**: The condition of signifiers being available in the environment, and the act of making signifiers available in the environment.
-	**Workspace**: see [_Other scenario TBA_]().
-	**Resource Containment**: see [_Other scenario TBA_]().
-	**Artifact**: see [_Other scenario TBA_]().
-	**Agent**: see [_Other scenario TBA_]().
-	**Resource Profile**: see [_Other scenario TBA_]().
-	**Agent Body**: see [_Other scenario TBA_]().

## Recommendation 
- The resource profile of an artifact can expose signifiers which reveal information about behavior possibilities offered by the artifact.
- Agent can discover and interpret exposed signifiers to receive information about:
   1. how to exploit behavior possibilities;
   2. under which circumstances to exploit behavior possibilities.

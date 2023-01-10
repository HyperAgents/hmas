# Discover Signifiers

Feature: Discovery of Signifiers


## Description
An agent A is situated in a manufacturing workspace that contains industrial artifacts (e.g.UR5 collaborative robot arm and a PhantomX robot arm) and other agents. The agent is responsible for operating a robotic arm artifact in the workspace, and cooperating with the other agents towards achieving production goals. To this end, agent A has the objective of discovering signifiers, i.e. cues in the workspace that reveal information about how to interact with the robotic arm artifact and the other agents.

Agent A discovers signifiers exposed in the profile P1 of the robotic arm, and signifiers exposed in the profile P2 of a FIPA agent platform that the agent can use to send messages to other agents (e.g. via HTTP).  Both the robotic arm and the FIPA agent platform are contained in the workspace along with their profiles.

## Competency Questions

| ID | Question in Natural Language | Example                                                                              |
|----|------------------------------|--------------------------------------------------------------------------------------|
| q1 | What are the signifiers exposed in a given resource profile?                          | What are the signifiers exposed in resource profile P1?                              |
| q2 | What are the signifiers exposed in resource profiles contained in a given workspace?  | What are the signifiers exposed in resource profiles in the manufacturing workspace? |
| q3 | What are the signifiers exposed in resource profiles of a given artifact?             | What are the signifiers exposed in resource profiles of the robotic arm artifact?    |

## Glossary
- **Signifier**: A perceivable sign/cue that can be interpreted meaningfully by an agent to reveal information about behavior possibilities.
- **Signifier Exposure**: The condition of signifiers being available in the environment, and the act of making signifiers available in the environment.
- **Affordance**: A behavior possibility that is a relationship between an ability of an agent and a situation that includes agents and features of the environment.
- **Resource Containment**: see [_Other scenario TBA_]().
- **Artifact**: see [_Other scenario TBA_]().
- **Agent**: see [_Other scenario TBA_]().
- **Resource Profile**: see [_Other scenario TBA_]().

## Recommendation 
- The resource profile of an artifact can expose signifiers which reveal information about behavior possibilities offered by the artifact.
- Agents can discover and interpret exposed signifiers to receive information about:
   1. how to exploit behavior possibilities;
   2. under which circumstances to exploit behavior possibilities.

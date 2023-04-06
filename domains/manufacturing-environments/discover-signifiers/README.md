# Discover Signifiers

Feature: Discovery of Signifiers


## Description
An agent is contained in a manufacturing workspace that contains industrial artifacts (e.g. a UR5 collaborative robot arm and a PhantomX robot arm). The agent operates the robotic arm artifact in the workspace towards achieving production goals. To this end, the agent discovers signifiers, i.e. perceivable signs/cues that can be interpreted meaningfully by an agent to reveal information about behavior possibilities, such as how to move the gripper of the robotic arm artifact.

The agent discovers signifiers exposed in the profile of the robotic arm artifact.

## Competency Questions

| ID | Question in Natural Language                                                                      | Example                                                                                                                      |
|----|---------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| q1 | What are the signifiers exposed in a given resource profile?                                      | Signifiers exposed in resource profile `ex:ur5Profile`: `ex:gripperMovable`                                                  |
| q2 | What are the signifiers exposed in resource profiles of artifacts contained in a given workspace? | Signifiers exposed in resource profiles of artifacts contained in workspace `ex:manufacturingWorkspace`: `ex:gripperMovable` |
| q3 | What are the signifiers exposed in resource profiles of a given artifact?                         | Signifiers exposed in resource profiles of artifact `ex:ur5`: `ex:gripperMovable`                                            |

## Glossary
- **Signifier**: A perceivable sign/cue that can be interpreted meaningfully by an agent to reveal information about a behavior possibility.
- **Signifier Exposure**: The state of signifiers being available in the environment.
- **Signifier Exposing**: The act of making signifiers available in the environment.
- **Affordance**: A behavior possibility that is a relationship between an ability of an agent and a situation that includes agents and features of the environment.
- **Workspace**: see [_Other scenario TBA_]().
- **Resource Containment**: see [_Other scenario TBA_]().
- **Artifact**: see [_Other scenario TBA_]().
- **Agent**: see [_Other scenario TBA_]().
- **Resource Profile**: see [_Other scenario TBA_]().

## Recommendation 
- The resource profile of an artifact can expose signifiers which reveal information about behavior possibilities offered by the artifact.
- Agents can discover and interpret exposed signifiers to receive information about:
   1. how to exploit behavior possibilities;
   2. under which circumstances to exploit behavior possibilities.
- TODOS:
  - [ ] position `hmas:Signifier` w.r.t to [td:InteractionAffordance](https://www.w3.org/2019/wot/td#InteractionAffordance).

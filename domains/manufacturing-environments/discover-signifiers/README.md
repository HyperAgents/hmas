# Discover Signifiers

Feature: Discovery of Signifiers


## Description
An agent is situated in a manufacturing workspace that contains industrial artifacts (e.g. a UR5 collaborative robot arm and a PhantomX robot arm). The agent operates the robotic arm artifact in the workspace towards achieving production goals. To this end, the agent discovers signifiers, i.e. perceivable signs/cues that can be interpreted meaningfully by an agent to reveal information about behavior possibilities, such as how to move the gripper of the robotic arm artifact.

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
- **Affordance**: A behavior possibility that is a relationship between an ability of an agent and a situation that includes agents and features of the environment [Chemero and Turvey, 2007].
- **Situatedness**: The relation between the environment and an agent that perceives and act on the environment, that affects the way an agent behaves in the environment [Brooks, 1991]. For example, a situated agent may respond in a timely fashion to its inputs from the environment, and perceive the signifiers that are exposed in the environment. 
- **Workspace**: see [Discovery of Workspaces, Agents, and Artifacts in Hypermedia Environments](../discover-core/README.md).
- **Resource Containment**: see [Discovery of Workspaces, Agents, and Artifacts in Hypermedia Environments](../discover-core/README.md).
- **Artifact**: see [Discovery of Workspaces, Agents, and Artifacts in Hypermedia Environments](../discover-core/README.md).
- **Agent**: see [Discovery of Workspaces, Agents, and Artifacts in Hypermedia Environments](../discover-core/README.md).
- **Resource Profile**: see [Discovery of Workspaces, Agents, and Artifacts in Hypermedia Environments](../discover-core/README.md).

[Chemero and Turvey, 2007] Chemero, A., & Turvey, M. T. (2007). Complexity, hypersets, and the ecological perspective on perception-action. Biological Theory, 2(1), 23-36.

[Brooks, 1991] Brooks R. A. (1991). Intelligence without reason. In Proceedings of the 12th international joint conference on Artificial intelligence, Volume 1, 569–595.

## Recommendation 
- The resource profile of an artifact can expose signifiers which reveal information about behavior possibilities offered by the artifact.
- Agents can discover and interpret exposed signifiers to receive information about:
   1. how to exploit behavior possibilities;
   2. under which circumstances to exploit behavior possibilities.
- TODOS:
  - [ ] position `hmas:Signifier` w.r.t to [td:InteractionAffordance](https://www.w3.org/2019/wot/td#InteractionAffordance).

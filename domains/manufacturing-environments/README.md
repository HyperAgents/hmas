# Manufacturing Domain

## Overview
The Manufacturing domain is illustrated using the example of an industrial shop floor where autonomous agents and factory workers operate industrial devices and cooperate with one another towards achieving production goals.  

The scenarios illustrate the following features of Hypermedia MAS: 

## Core Vocabulary

### Feature: Situatedness through Workspaces (see scenarios: [Workspaces: Discovery of industrial devices and their profiles](https://partage.imt.fr/index.php/f/544004763), [Workspaces: Discovery of agents and their profiles](https://partage.imt.fr/index.php/f/544004762), [Workspaces: Discovery of sub-workspaces and their profiles](https://partage.imt.fr/index.php/f/544004764)) 

A workspace is a logical container for agents and other entities. Workspaces define a notion of situatedness in Hypermedia MAS by capturing locality and context. For example, a manufacturing workspace on an industrial shop floor typically contains industrial devices, autonomous agents, and factory workers. The workspace allows agents to discover other entities in their local context on the shop floor that might help them achieve their production goals. 

### Feature: Uniform Interaction with Agents and Artifacts (see scenarios: [Workspaces: Discovery of industrial devices and their profiles](https://partage.imt.fr/index.php/f/544004763), [Workspaces: Discovery of agents and their profiles](https://partage.imt.fr/index.php/f/544004762)) 

Agents interact with heterogeneous entities in a Hypermedia MAS based on a uniform external characterization of those entities in terms of agents and artifacts: entities exhibiting autonomous behavior are modeled as agents, and entities exhibiting non-autonomous behavior are modeled as artifacts. Agents interact with one another by exchanging messages, and they can perceive and act on artifacts. For example, a UR5 robotic arm is modeled as an artifact whereas a software entity that operates the robotic arm to achieve a production goal is modeled as an agent. The UR5 operator agent interacts with the UR5 artifact by invoking operations, and other agents (e.g., factory workers) interact with the UR5 operator agent through messages. 

### Feature: Describing Non-information Resources through Resource Profiles (see scenarios: [Workspaces: Discovery of industrial devices and their profiles](https://partage.imt.fr/index.php/f/544004763), [Workspaces: Discovery of agents and their profiles](https://partage.imt.fr/index.php/f/544004762), [Workspaces: Discovery of sub-workspaces and their profiles](https://partage.imt.fr/index.php/f/544004764), [Hypermedia-driven Discovery of Platform Services](https://partage.imt.fr/index.php/f/544004765)) 

Many resources in a Hypermedia MAS are non-information resources, such as autonomous agents, people, organizations, etc. Resource Profiles allow agents to obtain useful information when dereferencing the URI of a non-information resource. For example, an agent in a manufacturing workspace can dereference the URI of a UR5 robotic arm to retrieve a Resource Profile with general information about the robotic arm and the means to operate it. 

### Feature: Hypermedia-driven Discovery via Containment Relations (see scenarios:[ Workspaces: Discovery of industrial devices and their profiles](https://partage.imt.fr/index.php/f/544004763), [Workspaces: Discovery of agents and their profiles](https://partage.imt.fr/index.php/f/544004762), [Workspaces: Discovery of sub-workspaces and their profiles](https://partage.imt.fr/index.php/f/544004764)) 

Containment relations between workspaces and the entities they contain allow agents to discover the rest of a Hypermedia MAS. For example, a shop floor can be structured along multiple workspaces, which may contain sub-workspaces, agents, industrial devices, etc. Given a workspace as an entry point into the system, an agent can crawl containment relations to discover other entities on the shop floor. 

### Feature: Hypermedia-driven Discovery of Platform Information via Hosting Relations (see scenario: [Hypermedia-driven Discovery of Platform Services](https://partage.imt.fr/index.php/f/544004765)) 

Agents, artifacts, documents, and other entities in a Hypermedia MAS are hosted on one or multiple platforms that provide various services to support the MAS. Hosting relations allow agents to discover hosting platforms together with any services they may provide. For example, a Hypermedia MAS for manufacturing may be implemented using a FIPA-compliant platform such as JADE. An agent in such a system is then hosted on an instance of a JADE platform, which provides an HTTP-based message transport service for interacting with the agents it hosts. A hosting relation can be used to advertise the hosting platform in the Resource Profile of an agent. Dereferencing the URI of the hosting platform would then retrieve a Resource profile of the platform, including any services the platform may provide. 

## Interaction Vocabulary
The following features aim to enable autonomous agents to discover and interpret how to exploit affordances for interacting with artifacts and other agents in hypermedia environments. 

### Feature: Discovery of Signifiers (see scenario: [Discovery of Signifiers](https://partage.imt.fr/index.php/f/544005321)) 

The discovery of signifiers enables an agent to discover information about how to exploit affordances for interacting with artifacts and other agents in a hypermedia environment. For example, an agent on an industrial shop floor can discover signifiers that reveal information about how to operate industrial devices. 

### Feature: Discovery of Profiles of Agent Bodies (see scenario: [Discovery of Profiles of Agent Bodies](https://partage.imt.fr/index.php/f/544005324)) 

The discovery of profiles of agent bodies enables an agent to discover information about the agents that are situated in a given workspace in a hypermedia environment, e.g. for discovering with which agents it can interact in the workspace. Situatedness is indicated by the containment of an agent’s body in the workspace. For example, an agent on an industrial shop floor can discover the profiles of agents whose bodies are contained in the shop floor to discover with whom it can cooperate for achieving a production goal.  

### Feature: Discovery of Signifiers of Situated Agents (see scenario: [Discovery of Signifiers of Situated Agents](https://partage.imt.fr/index.php/f/544005323)) 

The discovery of signifiers of situated agents enables an agent to discover information about how to exploit affordances for interacting with agents that are situated in a given workspace in a hypermedia environment. Specifically, the affordances offered by the environment for interacting with a given agent, are offered by the body of the agent that is contained in the environment. Thus, an agent can discover signifiers exposed in the profile of an agent body to discover information about how to exploit affordances of the agent body and interact with the agent (that has the body). For example, an agent on an industrial shop floor can discover the signifiers exposed in the profile of a given agent’s body that is contained in the shop floor to discover how to cooperate with the given agent for achieving a production goal. 

### Feature: Discovery of Behavioral Specifications (see scenario: [Discovery of Behavioral Specifications](https://partage.imt.fr/index.php/f/544005325)) 

The discovery of behavioral specifications enables an agent to discover how to behave for exploiting a related affordance in the hypermedia environment. For example, an agent in the industrial shop floor can discover a behavioral specification that specifies how to reset a robotic arm, e.g. by making an HTTP request for exploiting the affordance resetable of the robotic arm.  

### Feature: Discovery of Input for Behavior Parametrization (see scenario: [Discovery of Input for Behavior Parametrization](https://partage.imt.fr/index.php/f/544005327)) 

The discovery of input for behavior parametrization enables an agent to discover how it can parametrize a behavior that is specified in a behavioral specification. For example, an agent on an industrial shop floor can discover the input that is expected for the behavior of modifying the gripper of a robotic arm, e.g. the gripper value that is expected and the schema of the expected gripper value. 

### Feature: Discovery of Signifiers for Behavior Evaluation (see scenario: [Discovery of Signifiers for Behavior Evaluation](https://partage.imt.fr/index.php/f/544005320)) 

The discovery of signifiers for behavior evaluation enables an agent to discover information about how to exploit an affordance for evaluating a given behavior. For example, an agent on an industrial shop floor can discover a signifier for evaluating the behavior of modifying the gripper of a robotic arm, e.g. the signifier that reveals information about how to exploit the affordance gripper-perceivable of the robotic arm. 

### Feature: Discovery of Agent Abilities (see scenario: [Discovery of Agent Abilities](https://partage.imt.fr/index.php/f/544005322)) 

The discovery of agent abilities enables an agent to discover the qualities of other agents to perform behaviors for exploiting affordances, e.g. to decide whether to delegate goals to agents with given abilities. For example, an agent on an industrial shop floor can discover the planning ability of a given agent to ask the agent to synthesize a plan.  

### Feature: Discovery of Recommended Contexts (see scenario: [Discovery of Recommended Contexts](https://partage.imt.fr/index.php/f/544005326)) 

The discovery of contexts recommended by signifiers enables an agent to discover what are the constraints to which the agent’s situation is recommended to conform for exploiting an affordance. For example, an agent in the industrial workshop can discover that for exploiting the affordance gripper-modifiable of a robotic arm the constraints are the following: The agent has the objective of picking an item and placing it in a target location, and the item’s current location and the target location are in the range of the robotic arm. 

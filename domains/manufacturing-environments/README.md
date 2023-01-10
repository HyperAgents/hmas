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

### Feature: Discovery of Signifiers (see scenario: [Discovery of Signifiers](https://partage.imt.fr/index.php/f/544005321)) 

The discovery of signifiers enables an agent to discover information about how to exploit interaction possibilities for interacting with artifacts and other agents in a hypermedia environment. For example, an agent on an industrial shop floor can discover signifiers that reveal information about how to operate industrial devices and collaborate with other agents towards achieving production goals. 

## Interaction Vocabulary
The following features aim to enable autonomous agents to discover and interpret how to exploit interaction possibilities for interacting with artifacts and other agents in hypermedia environments.  

### Feature: Discovery of Behavior Specifications (see scenario: [Discovery of Behavioral Specifications](https://partage.imt.fr/index.php/f/544005325)) 

The discovery of behavior specifications enables an agent to discover how to behave for exploiting behavior possibilities in the hypermedia environment. For example, an agent on the industrial shop floor can discover a behavioral specification that specifies how to modify the gripper state of a robotic arm, e.g. by providing a gripper value as input and making an HTTP request.  

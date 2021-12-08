# Core Vocabulary Scenarios: Manufacturing agents

## Feature: discovery of devices, device profiles, and affordances to interact with devices
A production engineer uses a Web front-end to define and delegate a manufacturing goal to an artificial agent. The agent is situated in a manufacturing workspace that allows it to discover what industrial devices are available and what affordances they offer. The agent discovers all the affordances it needs to achieve the manufacturing goal, so that it may execute a manufacturing plan that achieves the manufacturing goal.

## Feature: discovery of agents, agent profiles, and affordances to interact with agents
The production engineer delegates a new manufacturing goal to the artificial agent, but this time the agent can use the industrial devices available in its workspace to achieve the manufacturing goal only partially. The manufacturing goal therefore overcomes the capabilities of the agent, so the agent needs to discover other manufacturing agents that can help it achieve the manufacturing goal. To this end, the manufacturing workspace allows the agent to discover other agents working in the same workspace, and agent profiles are used by the agent to determine which agents are relevant to interact with and to convey the affordances to interact with those agents. The agent uses all this metadata to interact and delegate a sub-goal to another agent in the same manufacturing workspace.

## Feature: discovery of workspaces, workspace profiles and sub-workspaces
The production engineer delegates a new manufacturing goal to the artificial agent, but this time this would require the agent to build a product across multiple manufacturing workspaces. To this end, the agent first needs to discover all manufacturing workspaces in the factory that are relevant to its manufacturing goal. The factory is organized in a hierarchy of workspaces with one root workspace that represents the factory. The agent is thus situated in a manufacturing workspace that is a sub-workspace in the larger factory workspace structure. The relations among workspaces in the factory (e.g., containment relations, relations of similarity) allow the agent to discover all relevant workspaces for achieving its manufacturing goal. To help agents determine what workspaces are relevant for achieving their manufacturing goals, each workspace carries a semantic profile that includes manufacturing-specific metadata, and relations to other workspaces, agents, and industrial devices available in that workspace. Once relevant workspaces are discovered, the agent can join (<--- here is the implicit workspace affordance that I meant) those workspaces to use any available industrial devices or to interact with other manfuacturing agents in that workspace.


## Feature : discovery of norms associated with a workspace and sub-workspace 

e.g. rules for using a tool 



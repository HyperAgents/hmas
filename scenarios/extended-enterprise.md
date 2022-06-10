# Extended Enterprise Domain

## Overview
The Extended Enterprise (EE) domain is illustrated using the example of an eco-system of enterprises working alltogether and forming a supply chain. 

To make it more concrete, let's imagine that one of them is situated in Saint-Etienne (IT'M Factory at MSE), another one is situated in St Gallen at HSG. 

When looking at their agentification on the Web, there are three workspaces (« PW » (Pot production Workspace) situated in HSG, « FW » (Pot filling Workspace) situated in MSE and « TW » (Transport Workspace ensuring the logistic of pot transportation from HSG to MSE). The transporter agents « Transporter » are situated in the «TW». The « HSG » agents are situated in the « PW », the « MSE » agents are situated in the « FW » and  « EE » is situated in the three workspaces. 

The interactions and coordination in the EE (sends a port order, makes an order for pot supply, supply pots) take place in the context of the « EE ».  

## Features

### Feature: [Discover Organization Entities](../tests/discover-organization-entities/modelet.md)

- A community composed of three organization entities HSG, MSE, EE. 
- « HSG », « MSE » and « EE » are respectively situated in workspace PW, FW and (PW,FW,TW).
- Some Agents situated in PW belong to HSG, others don’t, those situated in FW only belong to MSE, all belong to EE. 
- Transport agent may only belongs to EE. 
- If an agent is situated in two workspaces, it may belong to the three Organization entities.
- Artifacts situated in PW may count-as material of HSG, those in FW count-as material of MSE and all may count-as material of EE.


### Feature: [Organizational Relations](../tests/organizational-relations/modelet.md)

- TODO: add the relations among the organization entities.
- 
### Feature: Laws, Norms, and Sanctions

### Feature: Regulation dependencies

### Feature: Multiple agents belonging to one Organization

### Feature: Agents belonging to multiple Organizations

### Feature: Artifacts belonging to multiple Organizations

### Feature: Multiple Artifacts belonging to one Organization

### Feature: Organization Evolution


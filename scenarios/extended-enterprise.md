# Collaborative Enterprises Domain

## Overview
The Collaborative Enterprises (CE) domain is illustrated using the example of a network of factories working alltogether and forming a dynamic supply chain between them and eventually with other factories, suppliers or customers. As described in [Factories of the Future Multi-annual roadmap for the contractual PPP under the Horizon 2020](https://www.effra.eu/sites/default/files/factories_of_the_future_2020_roadmap.pdf), the trend of collaboration between multiple manufacturing enterprises is becoming an essential feature for day-to-day operations of both SMEs and large manufacturing enterprise irrespective of their size.

To make it more concrete, we will consider one factory situated in Saint-Etienne (IT'M Factory at MSE) dedicated to filling product in pots produced in a factory situated in St Gallen at HSG. Both factories are connected by a supply chain.

## Agentification
The agentification of these two factories and transport company on the Web results in three workspaces (« PW » (Pot production Workspace) situated in HSG, « FW » (Pot filling Workspace) situated in MSE and « TW » (Transport Workspace ensuring the logistic of pot transportation from HSG to MSE). 

## Organisations, Community
The organisation «TO» of transporter agents is situated in «TW». The organisation «HSGO» of agents working in HSG Factory are situated in « PW », the organisation «MSEO» of agents working in MSE Factory is situated in « FW ». The community « CFC » built from these three organisations is situated in the three workspaces, by the way of those three organisations that compose it. 

The interactions and coordination in the « CFC » community (e.g. sending of pot orders for pot supply, acknowledgement of pots delivery) take place in the context of this community. Other interactions involving only agents of an organisation entity take place within the organisation entity (e.g. in « HSG » or « MSE »). 

The community « CFC » is composed of three organization entities HSGO, MSEO, TO. It is working over three workspace PW, FW and TW.

HSGO, MSEO and TO are respectively contained in workspace PW, FW and TW. 

Some Agents contained in PW are members of HSGO, others don’t. All agents contained in FW are members of MSEO. All agents situated in TW are members of TO. All agents who are members of these organisations are members of CFC. 

All artifacts contained in PW count-as material of HSGO. Those in FW count-as material of MSEO. All count-as material of CFC.

HSGO, MSEO, CFC are respectively contained in workspace PW, FW and (PW,FW,TW). 

HSG, MSE respectively containted in workspace PW and FW. EE includes HSG and MSE. It is thus contained in PW and FW. Agents contained in PW and FW may belong to one or several of organization entities. Artifacts of PW may be counted as material of HSG but not MSE. Artifacts of FW may be counted as material of MSE but not HSG. Artifacts of PW and FW may be counted as material of EE.

## Features

### Feature: [Discover Organization Entities](../tests/discover-organization-entities/modelet.md)


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


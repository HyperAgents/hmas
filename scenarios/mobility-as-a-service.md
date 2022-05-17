# Mobility as a Service Domain

## Overview
The Mobility as a Service domain is illustrated using the example of a multinational enterprise available in all countries of the European Union that provides mobility service by making available autonomous vehicles for transporting people.

This example assumes that Autonomous Vehicles (AV) subscribed to provide service to Users of the Mobility as a Service (MaaS) enterprise can move freely among countries of the European Union (the same is valid for vehicles moving among states in US). People subscribed as Users to the Mobility as a Service (MaaS) enterprise located in any of the European Union countries can request mobility services through the MaaS enterprise.

Countries have their own consumer legislation regulating the relationship between consumers (i.e., Users) and service providers (i.e., AVs), and traffic legislation regulating vehicles (i.e., AVs) and other traffic including pedestrians, animals, and other conveyances.

The MaaS enterprise regulates the relationship between AVs and Users as well as define its own traffic regulation (more or less restrictive than the countries' legislation).

Countries regulations are valid on their own territory, while the MaaS enterprise regulations can be valid in all or in specific territories.

MaaS enterprises' regulations are abide by the Country regulation where they are located or operate.

AVs and Users shall abide by the country's regulations where they are located and by the MaaS enterprise's regulations. Because AVs and Users may move countries, they abide by different regulations over time.

Countries and the MaaS enterprise specify their regulations via norms and sanctions. Norms specify the expected behavior of the agents (i.e., AVs and Users), and sanctions specify what are the consequences to the deviation to the norm.

Example of countries law and sanctions are:
* Law No person shall drive a vehicle at a speed greater than is reasonable or prudent and in no event at a speed which endangers the safety of persons or property. The maximum speed are:
  + 130 km/h in highways
  + 110 km/h in a one-way road separated by a central empty area
  + 80 km/h in other roads
* Sanctions
  + Exceed speed limit in less than 20 km/h in a road with speed limit <= 50; 135 Euro, -1 Point
  + Exceed speed limit in less than 20 km/h in a road with speed limit > 50; 68 Euro, -1 Point
  + Exceed speed limit in more than 20 km/h and less than 29 km/h in a road with speed limit > 50; 135 Euro, -2 Point
  + Exceed speed limit in more than 30 km/h and less than 39 km/h in a road with speed limit > 50; 135 Euro, -3 Point
  + Exceed speed limit in more than 40 km/h and less than 49 km/h in a road with speed limit > 50; 135 Euro, -4 Point
  + Exceed speed limit in more than 50 km/h in a road with speed limit > 50; up to 1500 Euro, -6 Point

Examples of MaaS enterprise norms and sanctions are:
* Norm
  + The AV has to pick up the User in a 5 minute window of the agreed time
* Sanctions
  + The mobility service agreed price decreases in 5% for every minute of lateness
  + (Sanction) The MaaS enterprise gives 5% fee discount to the AV if the latter arrives to the pick up location earlier than the agreed time

## Features

### Feature: [Discover Organization Entities](../../tests/discover-organization-entities/modelet.md)
People who want to use a mobility service identifies existing MaaS organizations to decide which they want to join in order to achieve their goal of moving from one location to another. They also may want to know which other MaaS organizations they may join without conflicting with their existing membership.

### Feature: [Organizational Relations](./../tests/organizational-relations/modelet.md)
Mobility as a Service (MaaS) enterprises and countries are defined as Situated Regulated Organization Entities. MaaS enterprise SROEs are member of one or multiple country SROEs and the former regulations are subject to the laws and regulations of the latter.

### Feature: Laws, Norms, and Sanctions
Countries and the MaaS enterprise specify their regulations via norms and sanctions. Norms specify the expected behavior of the agents (i.e., AVs and Users), and sanctions specify what are the consequences to the deviation to the norm.

Example of countries law and sanctions are:
* Law No person shall drive a vehicle at a speed greater than is reasonable or prudent and in no event at a speed which endangers the safety of persons or property. The maximum speed are:
  + 130 km/h in highways
  + 110 km/h in a one-way road separated by a central empty area
  + 80 km/h in other roads
* Sanctions
  + Exceed speed limit in less than 20 km/h in a road with speed limit <= 50; 135 Euro, -1 Point
  + Exceed speed limit in less than 20 km/h in a road with speed limit > 50; 68 Euro, -1 Point
  + Exceed speed limit in more than 20 km/h and less than 29 km/h in a road with speed limit > 50; 135 Euro, -2 Point
  + Exceed speed limit in more than 30 km/h and less than 39 km/h in a road with speed limit > 50; 135 Euro, -3 Point
  + Exceed speed limit in more than 40 km/h and less than 49 km/h in a road with speed limit > 50; 135 Euro, -4 Point
  + Exceed speed limit in more than 50 km/h in a road with speed limit > 50; up to 1500 Euro, -6 Point

Examples of MaaS enterprise norms and sanctions are:
* Norm
  + The AV has to pick up the User in a 5 minute window of the agreed time
* Sanctions
  + The mobility service agreed price decreases in 5% for every minute of lateness
  + (Sanction) The MaaS enterprise gives 5% fee discount to the AV if the latter arrives to the pick up location earlier than the agreed time

### Feature: Regulation dependencies

### Feature: Multiple agents belonging to one Organization

### Feature: Agents belonging to multiple Organizations

### Feature: Artifacts belonging to multiple Organizations

### Feature: Multiple Artifacts belonging to one Organization

### Feature: Organization Evolution

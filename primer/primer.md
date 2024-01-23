# HMAS Model Primer

# Abstract

This document is an introduction to the HMAS ontology, which proposes a vocabulary to describe a multi-agents system evolving in a environment that can be not embodied, namely the web. This ontology aims to fit the different approaches of the multi-agent programming as well as the existing standards of the modern web and the web of things.

This documents provides an overview of the key concepts of the vocabulary as well as some examples that can be reused for implementation.

# 1. Introduction

This document is an introduction to the *Hypermedia Multi-Agents Systems* (HMAS) ontology that is meant for describing a Multi Agents System with agents exploring a Web environment.

A Multi Agents System (MAS) is a system composed of several entities with autonomous behaviors in an environment performing tasks while following some organization. This definition brings 3 aspects what this ontology abroaches:

- agents: how to represent the knowledge base and the goals of the agents?
- environment: how to represent the objects, their usages, and the environment itself where these objects can be found?
- organization: how to represent the different roles, rules, and missions that must be given to agents?

The modern Web relies on the Hypermedia mechanisms in order to interact with the resources that can be found there, in a way that the user is agnostic from its implementation details. That is why we consider here the web as a *Hypermedia* environment.

This ontology is meant to be able to describe a MAS that is not necessarily embodied, and also where agents can be softwares as well as human beings. A social network with humans posting content in interaction with software agents browsing the platform for moderation is a good example of what this ontology can describe.

The later sections of this document should provide you:

- high-level definitions of the key concepts of the HMAS ontology
- simple scenarii for each of these concepts and their implementations both in [TURTLE] format and in RDF/XML

Finally this document ends with a summary of the features available in HMAS 

# 2. Overview of HMAS

This session is meant to explain the key classes of the HMAS ontology. We will go further into detail for each of them. Here is an overview of the structure of the main HMAS model.

![Untitled](./schema.png)

The terms of this vocabulary are stored in different modules, namely:

- core: Provides the main concepts for providing a Hypermedia MAS platform
- interaction: Provides the needed terms to describe the interactions that an agents has with its environment
- regulation: Provides the needed terms to describe a MAS as an organizational structure with rules, roles and missions

## 2.1 Agent

An agent is an entity capable of autonomous behavior. It can be a human being or a software and the MAS is agnostic of that. An agent should join an organization, adopt a role and perform missions that it is given. In order to achieve its missions, the agent can interact with the environment where it is.

## 2.2 Artifact

A resource that can be dynamically constructed, shared, and used by agents to support their activities. In a Hypermedia MAS, an artifact exposes and can be accessed through a hypermedia interface (in addition to other possible interfaces, such as a physical interface). An artifact can have many forms as:

- a resource that the agent can find in the environment (an API, a database, a file, …)
- an artifact meant to represent a part of the environment that can be joined or left
- an artifact made to use several other artifacts at the same time
- an organizational artifact meant to share data among agents about missions and roles
- a communication artifact that can be used by agents to interact with other agents
- etc…

The artifacts can have different lifetimes:

- some of them can be static environment parts of the MAS
- some of them can be dynamically created or deleted on the fly

An artifact has features, named *Signifiers*, that are available for use by the agents the way they intend to use it. For a given artifact, a summary of all its available signifiers can be found in its *Resource Profile*

## 2.3 Resource Profiles

A resource profile is structured data describing a resource through general metadata, domain- and application-specific metadata, and signifiers. Any artifact has its own Resource Profile. This allows an agent to discover the features of an artifact at runtime. This concepts comes directly from the Web of Things.

**Example:** A robotic arm is an artifact and its resource profile explains that there is an endpoint that allows to set the position of this arm.

## 2.4 Signifiers

A signifier is a perceivable sign/cue that can be interpreted meaningfully by an agent to reveal information about a behavior possibility. Please note that a signifier does not explain what to use the artifact for, but what can be used from the artifact instead.

A signifier should always give the minimal constraints that are expected to the input data as well as the minimal constraints that you should expect from the output data.

**Example**: The robotic arm can be moved in order to move objects from a truck into a box, but it can also be used to hammer nails. The signifier itself only states that the arm can be moved, describing the constraints of what is expected as input, and the constraints of what is going to be returned to the agent.

## 2.5 Workspace

A logical container for any resource in general and in particular for agents, artifacts or other workspaces. Workspaces can be created or deleted by agents on a needed basis. All agent interactions happen in the context of a workspace whether or not the worspace was explicitly reified. A workspace can be, for instance, implemented on top of an LDP (Linked Data Platform) indirect container.

Therefore a workspace can:

- represent a bounded space of the environment and therefore remain static
- be created and deleted at runtime in order to create a temporary common space between agents from several organizations

## 2.6 Organization

An Organization is an entity situated on Agents and Artifacts, and regulated by a regulation system. It should regulate the following aspects:

- which values drive the organization?
- what are the groups structuring the organization?
- what are the roles of the agents within the organization?
- which missions should the agent perform?
- what are each artifact meant for in this organization?

## 2.7 Platform

A Hypermedia MAS (HMAS) platform is a system providing a collection of features to support Hypermedia MAS. Common features include support for communication and interaction, runtime environments for agents, artifacts, or organizations, etc.

This ontology is agnostic of the implementation details so even if support has been made for JaCaMo, it can be possibly any system.

# 3 Examples of key concepts of HMAS

Now that we have an overview of the main classes available in HMAS, this section should provide for each of them a small scenario as well as an implementation of that scenario. Each implementation will be provided both in turtle format and in RDF/XML.

## 3.1 Agent

Here we simply want the software HyperReader2000, to be agent on our platform platf, in the workspace forumPlatf

**Turtle Example**

```
@prefix hmas: <https://purl.org/hmas/> .
@prefix platf: <http://www.example.org/platforms/platf#> .
@prefix forumPlatf: <http://www.example.org/workspaces/forumPlatf#> .
@prefix HyperReader2000: <http://www.example.org/agents/HyperReader2000#> .

HyperReader2000:agent a hmas:Agent ;
	hmas:isHostedOn platf:platform ;
	hmas:isContainedIn forumPlatf:workspace ;
	hmas:hasProfile HyperReader2000: .
```

**XML Example**

```
<?xml version="1.0" encoding="utf-8" ?>
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
         xmlns:hmas="https://purl.org/hmas/">

  <rdf:Description rdf:about="http://www.example.org/agents/HyperReader2000#agent">
    <rdf:type rdf:resource="https://purl.org/hmas/Agent"/>
    <hmas:isHostedOn rdf:resource="http://www.example.org/platforms/platf#platform"/>
    <hmas:isContainedIn rdf:resource="http://www.example.org/workspaces/forumPlatf#workspace"/>
    <hmas:hasProfile rdf:resource="http://www.example.org/agents/HyperReader2000#"/
  </rdf:Description>

</rdf:RDF>
```

## 3.2 Artifact

Here we want an artifact named forumAccount contained in the workspace forumPlatf

**Turtle Example**

```
@prefix forumPlatf: <http://www.example.org/artifacts/forumAccount#> .

forumAccount:artifact a hmas:Artifact ;
  hmas:hasProfile forumAccount: ;
  hmas:isHostedOn platf:platform ;
  hmas:isContainedIn forumPlatf:workspace .
```

**XML Example**

```
<?xml version="1.0" encoding="utf-8" ?>
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
         xmlns:hmas="https://purl.org/hmas/">

  <rdf:Description rdf:about="http://www.example.org/artifacts/forumAccount#artifact">
    <rdf:type rdf:resource="https://purl.org/hmas/Artifact"/>
    <hmas:isHostedOn rdf:resource="http://www.example.org/platforms/platf#platform"/>
    <hmas:isContainedIn rdf:resource="http://www.example.org/workspaces/forumPlatf#workspace"/>
    <hmas:hasProfile rdf:resource="http://www.example.org/artifacts/forumAccount#"/
  </rdf:Description>

</rdf:RDF>
```

## 3.3 Resource Profiles

Our artifact ForumAccount should have a Resource Profile exposing one signifier for getting a post from the forum. The signifier should be defined later.

**Turtle Example**

```
@prefix sign: <http://www.example.org/signifiers/> .

forumAccount: a hmas:ResourceProfile ;
# not mandatory since we defined the hmas:hasProfile of the artifact earlier
	hmas:isProfileOf forumAccount:artifact ;
	hmas:exposesSignifier sign:getPost .
```

**XML Example**

```
<?xml version="1.0" encoding="utf-8" ?>
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
         xmlns:hmas="https://purl.org/hmas/">

  <rdf:Description rdf:about="http://www.example.org/artifacts/forumAccount#">
    <rdf:type rdf:resource="https://purl.org/hmas/ResourceProfile"/>
    <hmas:isProfileOf rdf:resource="http://www.example.org/artifacts/forumAccount#artifact"/>
    <hmas:exposesSignifier rdf:resource="http://www.example.org/signifiers/getPost"/>
    <hmas:exposesSignifier rdf:resource="http://www.example.org/signifiers/moderatePost"/>
  </rdf:Description>

</rdf:RDF>
```

## 3.4 Signifiers

In this part we will implement the signifiers themselves for the same artifact than in the previous section.

### 3.4.1 The signifiers

**Turtle Example**

```
@prefix shape: <http://www.example.org/shapes/> .
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix hctl: <https://www.w3.org/2019/wot/hypermedia#> .
@prefix htv: <http://www.w3.org/2011/http#> .
@prefix dcterms: <http://purl.org/dc/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix prov: <http://www.w3.org/ns/prov#> .

# Defining the signifier itself

sign:getPost a hmas:Signifier ;
	hmas:signifies shape:getPost .

# Defining the form of the input

shape:getPostForm a sh:NodeShape ;
	sh:class hctl:Form ;
	sh:property [
		sh:path hctl:forContentType ;
		sh:minCount 1 ;
		sh:maxCount 1 ;
		sh:hasValue "application/json"
	] , [
		sh:path htv:methodName ;
		sh:minCount 1 ;
		sh:maxCount 1 ;
		sh:hasValue "POST"
	] , [
		sh:path hctl:hasTarget ;
		sh:minCount 1 ;
		sh:maxCount 1 ;
		sh:hasValue <http://www.example.org/api/getPost>
	] .

# Defining the form of the output

shape:getPostOutput a sh:NodeShape ;
	sh:class shape:postSchema ;
  sh:property [
		sh:path dcterms:identifier ;
		sh:minCount 1 ;
		sh:maxCount 1 ;
		sh:datatype xsd:int ;
		sh:minExclusive 0 ;
		sh:maxExclusive 10000
	] , [
		sh:path dcterms:description ;
		sh:minCount 1 ;
		sh:maxCount 1 ;
		sh:datatype: xsd:string
	] .

# Defining the whole signifier shape

shape:getPost a sh:NodeShape ;
	sh:class hmas:ActionExecution ;
	sh:property [
		sh:path prov:used ;
		sh:minQualifiedShape 1 ;
		sh:maxQualifiedShape 1 ;
		sh:qualifiedValueShape shape:getPostForm
	] , [
		sh:path hmas:hasInput ;
		sh:minCount 1 ;
		sh:maxCount 1 ;
		sh:datatype 0 ;
		sh:minExclusive 0 ;
		sh:maxExclusive 10000
	] , [
		sh:path hmas:hasOutput ;
		sh:minQualifiedShape 1 ;
		sh:maxQualifiedShape 1 ;
		sh:qualifiedValueShape shape:getPostOutput
	] .
```

**XML Example**

```
<?xml version="1.0" encoding="utf-8" ?>
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
         xmlns:hmas="https://purl.org/hmas/"
         xmlns:sh="http://www.w3.org/ns/shacl#">

  <rdf:Description rdf:about="http://www.example.org/signifiers/getPost">
    <rdf:type rdf:resource="https://purl.org/hmas/Signifier"/>
    <hmas:signifies>
      <rdf:Description rdf:about="http://www.example.org/shapes/getPost">
        <rdf:type rdf:resource="http://www.w3.org/ns/shacl#NodeShape"/>
        <sh:class rdf:resource="https://purl.org/hmas/ActionExecution"/>
        <sh:property>
          <rdf:Description>
            <sh:path rdf:resource="http://www.w3.org/ns/prov#used"/>
            <sh:minQualifiedShape rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">1</sh:minQualifiedShape>
            <sh:maxQualifiedShape rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">1</sh:maxQualifiedShape>
            <sh:qualifiedValueShape>
              <sh:NodeShape rdf:about="http://www.example.org/shapes/getPostForm">
                <sh:class rdf:resource="https://www.w3.org/2019/wot/hypermedia#Form"/>
                <sh:property>
                  <rdf:Description>
                    <sh:path rdf:resource="https://www.w3.org/2019/wot/hypermedia#forContentType"/>
                    <sh:minCount rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">1</sh:minCount>
                    <sh:maxCount rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">1</sh:maxCount>
                    <sh:hasValue>application/json</sh:hasValue>
                  </rdf:Description>
                </sh:property>

                <sh:property>
                  <rdf:Description>
                    <sh:path rdf:resource="http://www.w3.org/2011/http#methodName"/>
                    <sh:minCount rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">1</sh:minCount>
                    <sh:maxCount rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">1</sh:maxCount>
                    <sh:hasValue>POST</sh:hasValue>
                  </rdf:Description>
                </sh:property>

                <sh:property>
                  <rdf:Description>
                    <sh:path rdf:resource="https://www.w3.org/2019/wot/hypermedia#hasTarget"/>
                    <sh:minCount rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">1</sh:minCount>
                    <sh:maxCount rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">1</sh:maxCount>
                    <sh:hasValue rdf:resource="http://www.example.org/api/getPost"/>
                  </rdf:Description>
                </sh:property>

              </sh:NodeShape>
            </sh:qualifiedValueShape>

          </rdf:Description>
        </sh:property>

        <sh:property>
          <rdf:Description>
            <sh:path rdf:resource="https://purl.org/hmas/hasInput"/>
            <sh:minCount rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">1</sh:minCount>
            <sh:maxCount rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">1</sh:maxCount>
            <sh:datatype rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">0</sh:datatype>
            <sh:minExclusive rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">0</sh:minExclusive>
            <sh:maxExclusive rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">10000</sh:maxExclusive>
          </rdf:Description>
        </sh:property>

        <sh:property>
          <rdf:Description>
            <sh:path rdf:resource="https://purl.org/hmas/hasOutput"/>
            <sh:minQualifiedShape rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">1</sh:minQualifiedShape>
            <sh:maxQualifiedShape rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">1</sh:maxQualifiedShape>
            <sh:qualifiedValueShape>
              <sh:NodeShape rdf:about="http://www.example.org/shapes/getPostOutput">
                <sh:class rdf:resource="http://www.example.org/shapes/postSchema"/>
                <sh:property>
                  <rdf:Description>
                    <sh:path rdf:resource="http://purl.org/dc/identifier"/>
                    <sh:minCount rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">1</sh:minCount>
                    <sh:maxCount rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">1</sh:maxCount>
                    <sh:datatype rdf:resource="http://www.w3.org/2001/XMLSchema#int"/>
                    <sh:minExclusive rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">0</sh:minExclusive>
                    <sh:maxExclusive rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">10000</sh:maxExclusive>
                  </rdf:Description>
                </sh:property>

                <sh:property>
                  <rdf:Description>
                    <sh:path rdf:resource="http://purl.org/dc/description"/>
                    <sh:minCount rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">1</sh:minCount>
                    <sh:maxCount rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">1</sh:maxCount>
                    <sh:datatype: rdf:resource="http://www.w3.org/2001/XMLSchema#string"/>
                  </rdf:Description>
                </sh:property>

              </sh:NodeShape>
            </sh:qualifiedValueShape>

          </rdf:Description>
        </sh:property>

      </rdf:Description>
    </hmas:signifies>

  </rdf:Description>

</rdf:RDF>
```

## 3.5 Workspace

We will now describe a workspace in the platform containing our agent and our platform.

**Turtle Example**

```
forumPlatf:workspace a hmas:Workspace ;
# this line is not mandatory since we already defined the agent and the artifact as contained in this workspace
	hmas:contains forumAccount:artifact , HyperReader2000:agent ;
	hmas:isHostedOn platf:platform .
```

**XML Example**

```
<?xml version="1.0" encoding="utf-8" ?>
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
         xmlns:hmas="https://purl.org/hmas/">

  <rdf:Description rdf:about="http://www.example.org/workspaces/forumPlatf#workspace">
    <rdf:type rdf:resource="https://purl.org/hmas/Workspace"/>
    <hmas:contains rdf:resource="http://www.example.org/artifacts/forumAccount#artifact"/>
		<hmas:contains rdf:resource="http://www.example.org/agents/HyperReader2000#agent"/>
    <hmas:isHostedOn rdf:resource="http://www.example.org/platforms/platf#platform "/
  </rdf:Description>

</rdf:RDF>
```

## 3.6 Organization

Now we can define our Reader organization

**Turtle Example**

```
@prefix HRorg: <http://www.example.org/organisations/HyperReaderOrg/> .
@prefix val: <http://www.example.org/values/> .
@prefix roles: <http://www.example.org/roles/> .
@prefix groups: <http://www.example.org/groups/> .
@prefix missions: <http://www.example.org/missions/> .
@prefix facility: <http://www.example.org/facilities/> .
@prefix memship: <http://www.example.org/memberships/> .

val:HyperIntenseReading a sh:NodeShape .

roles:HyperReader a sh:NodeShape .

groups:HyperReadingDepartment a sh:NodeShape .

memship:HyperReaderMembership a sh:NodeShape ;
	hmas:isMembershipOf HyperReader2000:agent .

missions:HyperReadingPosts a sh:NodeShape .

facility:HyperReadingArea a sh:NodeShape .

HRorg:organization a orgs:ReaderOrg ;
	hmas:hasResourceProfile HRorg: ;
	hmas:hasOrganizationalValue val:HyperIntenseReading ;
	hmas:providesRole roles:HyperReader ;
	hmas:isStructuredBy groups:HyperReadingDepartment ;
	hmas:proposesMission missions:HyperReadingPosts ;
	hmas:proposesFacility facility:HyperReadingArea .
```

**XML Example**

```
<?xml version="1.0" encoding="utf-8" ?>
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
         xmlns:hmas="https://purl.org/hmas/">

  <rdf:Description rdf:about="http://www.example.org/values/HyperIntenseReading">
    <rdf:type rdf:resource="http://www.w3.org/ns/shacl#NodeShape">
  </rdf:Description>

  <rdf:Description rdf:about="http://www.example.org/roles/HyperReader">
    <rdf:type rdf:resource="http://www.w3.org/ns/shacl#NodeShape"/>
  </rdf:Description>

  <rdf:Description rdf:about="http://www.example.org/groups/HyperReadingDepartment">
    <rdf:type rdf:resource="http://www.w3.org/ns/shacl#NodeShape"/>
  </rdf:Description>

  <rdf:Description rdf:about="http://www.example.org/memberships/HyperReaderMembership">
    <rdf:type rdf:resource="http://www.w3.org/ns/shacl#NodeShape"/>
    <hmas:isMembershipOf rdf:resource="http://www.example.org/agents/HyperReader2000#agent"/>
  </rdf:Description>

  <rdf:Description rdf:about="http://www.example.org/missions/HyperReadingPosts">
    <rdf:type rdf:resource="http://www.w3.org/ns/shacl#NodeShape"/>
  </rdf:Description>

  <rdf:Description rdf:about="http://www.example.org/facilities/HyperReadingArea">
    <rdf:type rdf:resource="http://www.w3.org/ns/shacl#NodeShape"/>
  </rdf:Description>

  <rdf:Description rdf:about="http://www.example.org/organisations/HyperReaderOrg/organization">
    <rdf:type rdf:resource="http://www.example.org/organisations/ReaderOrg"/>
    <hmas:hasResourceProfile rdf:resource="http://www.example.org/organisations/HyperReaderOrg/"/>
    <hmas:hasOrganizationalValue rdf:resource="http://www.example.org/values/HyperIntenseReading"/>
    <hmas:providesRole rdf:resource="http://www.example.org/roles/HyperReader"/>
    <hmas:isStructuredBy rdf:resource="http://www.example.org/groups/HyperReadingDepartment"/>
    <hmas:proposesMission rdf:resource="http://www.example.org/missions/HyperReadingPosts"/>
    <hmas:proposesFacility rdf:resource="http://www.example.org/facilities/HyperReadingArea"/>
  </rdf:Description>

</rdf:RDF>
```

## 3.7 Platform

Finally, we need to define our HMASPlatform hosting all of our artifacts, workspaces and agents

**Turtle Example**

```
platf:platform a HypermediaMASPlatform ;
# the rest of the statement is also not mandatory
platf:hosts forumAccount:artifact , forumPlatf:workspace , HyperReader2000:agent .
```

**XML Example**

```
<?xml version="1.0" encoding="utf-8" ?>
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
         xmlns:hmas="https://purl.org/hmas/">

  <rdf:Description rdf:about="http://www.example.org/platforms/platf#platform">
    <rdf:type rdf:resource="https://purl.org/hmas/HypermediaMASPlatform"/>
    <hmas:hosts rdf:resource="http://www.example.org/artifacts/forumAccount#artifact"/>
		<hmas:hosts rdf:resource="http://www.example.org/agents/HyperReader2000#agent"/>
    <hmas:hosts rdf:resource="http://www.example.org/workspaces/forumPlatf#workspace"/>
  </rdf:Description>

</rdf:RDF>
```

# 4 Summary

The implementations of the previous section aims to illustrate the following features:

- three independant approaches are covered by the HMAS
    - agent programming
    - environment programming
    - organization programming
- the artifact programming aims to fit with the Web of Things concepts through the notion of Resource Profile
- the MAS modelized here can be not embodied like an online forum
- an organization has a structure that can be seen as a combination of different approches:
    - values: the values that the organization aims to follow
    - groups: how to structure the organization
    - roles: the roles that must be given to the agents
    - missions: the missions that should be given to the agents from the organization
    - facility: what are the different places of the environment meant for

# A. **Acknowledgements**

This document was produced by the HyperAgents research team, spread over the laboratories of INRIA Nice Sophia (Fabien Gandon, Christopher Leturc, Olivier Corby, Franck Michel, Andrea Tettamanzi, Serena Villata, Nicolas Robert), École des Mines de Saint-Étienne (Antoine Zimmermann, Maxime Lefrançois, Victor Charpenay, Luis Gustavo Nardin, Olivier Boissier, Gauthier Picard) and the University of Saint Gallen (Andrei Ciortea, Danai Vachtsevanou, Simon Mayer)

# C. References

[TURTLE]

Eric Prud'hommeaux, Gavin Carothers; eds. [Turtle: Terse RDF Triple Language](http://www.w3.org/TR/2011/WD-turtle-20110809/). 9 August 2011. W3C Working Draft. URL: [http://www.w3.org/TR/2011/WD-turtle-20110809/](http://www.w3.org/TR/2011/WD-turtle-20110809/)

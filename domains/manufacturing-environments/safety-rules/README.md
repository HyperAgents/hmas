# Discover Regulative Norms
Feature: Discovery of Regulative Norms

## Description

In the i3S Organization, if there is a fire, then all the doors must be closed, it is forbidden for people to take the elevators and it is allowed for people to take the emergency exits. Thomas, a safety guard must ascertain which norms have not been respected and ensure that they are. Thus, Thomas must list a set of norms and which norms are applicable wrt their context of application, and be able to know norms that have not been respected. 

## Competency Questions


| ID | Question in Natural Language | Example                                                                                                                                   |
|----|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| q1 | What are the set of norms ?           |  `ex:AllDoorsShouldBeClosed` a `:RegulativeNorm`                                                    |
| q2 | What are the set of norms that are defined in an organization specification ?  |  `ex:AllDoorsShouldBeClosed` a `:RegulativeNorm`                                                    |
| q3  | What are the set of norms that are enforced in an organization ?  |  `ex:AllDoorsShouldBeClosed` a `:RegulativeNorm`                                                    |
| q4 | Who are the roles concerned by the regulative norm ?             | `ex:I3SStaff` a `hreg:SocialRole`                                                  |
| q5 | What are the norms that have not still been respected ?        | `ex:safetyRule` a `:RegulativeNorm`  |
| q6  | What are the norms that have been violated ?        | `ex:safetyRule` a `:RegulativeNorm`  |
| q7  | What are the behaviours that are explicitely allowed ?        | `ex:safetyRule` a `:RegulativeNorm`  |
| q8  | What are the behaviours that are not allowed (or <=> prohibited) ?        | `ex:safetyRule` a `:RegulativeNorm`  |
| q9 | What are the behaviours that are obliged ?        | `ex:safetyRule` a `:RegulativeNorm`  |
| q10 | What are the states of affairs that are allowed to be when a norm is applicable ?        | `ex:safetyRule` a `:RegulativeNorm`  |
| q11  | What are the states of affairs that ought not to be when a norm is applicable ?        | `ex:safetyRule` a `:RegulativeNorm`  |
| q12  | What are the states of affairs that ought to be when a norm is applicable?        | `ex:safetyRule` a `:RegulativeNorm`  |
| q13 | What norms are activated in an organization w.r.t. a context ?                  | `ex:safetyRule` a `:RegulativeNorm`                  |
| q14 | Who are in charge of enforcing a regulative norm ?                  | `ex:safetyRule` a `:RegulativeNorm`                  |
| q15 | Who are the set of possible worlds that describe the state of affairs of a workspace ?                  | `ex:safetyRule` a `:RegulativeNorm`                  |


## Glossary

* [**_Regulative Norm_**](https://purl.org/hmas/regulation#Norm): a specification of the standard behaviors one expects from others in an organization. 
* [**_Possible World_**](https://purl.org/hmas/regulation#PossibleWorld): a possible world is a ressource that describes a state of affairs of a world.
* [**_Normative Context_**](https://purl.org/hmas/regulation#NormativeContext):  a normative context is a possible world which describes a state of affairs when a norm is applicable. (At least one normative context should be verified.)
* [**_Normative Target_**](https://purl.org/hmas/regulation#NormativeTarget) :  an agent or a group of agents which have social roles. These social roles are concerned by the regulative norm. 
* [**_Deontic Specification_**](https://purl.org/hmas/regulation#NormativeModality) :  a deontic specification specifies from a possible world, what are the regulative norms that should be considered.
* [**_Obligation_**](https://purl.org/hmas/regulation#Obligation):  an obligation is a possible world which describes a state of affairs of what ought to be. It is associated with a norm and can specify a standard of behavior that must be achieved when a norm is activated. 
* [**_Prohibition_**](https://purl.org/hmas/regulation#Prohibition): a prohibition is a possible world which describes a state of affairs of what ought not to be. It is associated with a norm and can specify a standard of behavior that should never be achieved when a norm is activated. 
* [**_Permission_**](https://purl.org/hmas/regulation#Permission):  a prohibition is a possible world which describes a state of affairs of what is allowed to be. It is associated with a norm and can specify a standard of behavior that can be achieved when a norm is activated.  


## Recommendations

* An obligatory behaviour can be described explictly with a possible world where the obligatory behaviour occurred e.g. "close all the doors" is an explicite behaviour which is verified in this possible world typed as an obligation.
* An obligatory behaviour can be also described implictly by defining a set possible worlds that should be reached e.g. "all the doors must be closed" is a possible world typed as an obligation and describes all the behaviours that should bring it about this state of affairs.
* A prohibited behaviour can be described explictly with a possible world where the prohibited behaviour occurred e.g. "open all the doors" is an explicite behaviour which is verified in this possible world typed as a prohibition.
* A prohibited behaviour can be also described implictly by defining a set possible worlds that should be avoided e.g. "all the doors must be opened" is a possible world typed as a prohibition and describes all the behaviours that should prevent from reaching this state of affairs.
* [**_Modality_**](https://purl.org/hmas/regulation#NormativeModality) :  a modality would be a particular mode in which a possible world should be interpreted e.g. as an obligation, prohibition, or permission. It is not introduced in the glossary since there is no reason to introduce it explicitly.
* A possible world can be any ressource, a [named graph](https://en.wikipedia.org/wiki/Named_graph) or a [quoted graph](https://w3c.github.io/rdf-star/cg-spec/editors_draft.html). A possible world are reified triplets, it may also be described by [singleton property](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4350149/) or the [standard RDF reification or using N3](https://www.w3.org/DesignIssues/Reify.html). This choice of reification will change the given Competency Questions written in SPARQL. We choosed the standard RDF reification in this motivating scenario. For more details, we refer the reader to the issue [here](https://github.com/HyperAgents/ns.hyperagents.org/issues/141).

## Questions

* Should we call "possible world" or "possible hyperworld" ? 

## Related links

* [link toward issues that are associated to the domain](https://github.com/HyperAgents/ns.hyperagents.org/issues?q=manufacturing+environment)
* [link toward issues that are associated to this motivating scenario](https://github.com/HyperAgents/ns.hyperagents.org/issues?q=safety+rules)
* [link toward related features that are associated to this motivating scenario](https://github.com/HyperAgents/ns.hyperagents.org/issues?q=norm)





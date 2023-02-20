# Discover Regulative Norms
Feature: Discovery of Regulative Norms

## Description

In the i3S Organization, if there is a fire, then all the doors must be closed, it is forbidden for people to take the elevators and it is allowed for people to take the emergency exits. Thomas, a safety guard must ascertain which norms have not been respected and ensure that they are. Thus, Thomas must list a set of norms and which norms are applicable wrt their context of application, and be able to know norms that have not been respected. 

## Competency Questions


| ID | Question in Natural Language | Example                                                                                                                                   |
|----|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| q1 | What are the set of norms ?           |  `ex:AllDoorsShouldBeClosed` a `:RegulativeNorm`                                                    |
| q2 | Who are the agents under the regulation of a norm ?             | Example2                                                  |
| q3 | What are the norms that have not been respected ?        | Example3 |
| q4 | What norms are activated in an organization w.r.t. a context ?                  | Example4                  |
| q5 | What norms are activated in an organization w.r.t. a context ?                  | Example4                  |



## Glossary

* [**_Regulative Norm_**](https://purl.org/hmas/regulation#Norm): a specification of the standard behaviors one expects from others in an organization. 
* [**_Possible World_**](https://purl.org/hmas/regulation#PossibleWorld): a possible world is a ressource that describes a state of affair of a world.
* [**_Normative Context_**](https://purl.org/hmas/regulation#NormativeContext):  a normative context is a possible world which describes a state of affairs when a norm is applicable. (At least one normative context should be verified.)
* [**_Normative Target_**](https://purl.org/hmas/regulation#NormativeTarget) :  an agent or a group of agents which have social roles concerned by a regulative norm. 
* [**_Deontic Specification_**](https://purl.org/hmas/regulation#NormativeModality) :  a deontic specification specifies from a possible world, what are the regulative norms that should be considered.
* [**_Obligation_**](https://purl.org/hmas/regulation#Obligation):  a normative modality associated with a norm  that specifies a standard of behavior that must be achieved when a norm is activated. 
* [**_Prohibition_**](https://purl.org/hmas/regulation#Prohibition):  a normative modality associated with a norm  that specifies a standard of behavior that shouldn't be verified when a norm is activated.
* [**_Permission_**](https://purl.org/hmas/regulation#Permission):  a normative modality associated with a norm  that specifies a standard of behavior that is explicitly allowed when a norm is activated.

## Recommendations

- An obligatory behaviour can be described explictly with a possible world where the obligatory behaviour occurred e.g. "close all the doors" is an explicite behaviour which is verified in this possible world typed as an obligation.
- An obligatory behaviour can be also described implictly by defining a set possible worlds that should be reached e.g. "all the doors must be closed" is a possible world typed as an obligation and describes all the behaviours that should bring it about this state of affairs.
- A prohibited behaviour can be described explictly with a possible world where the prohibited behaviour occurred e.g. "open all the doors" is an explicite behaviour which is verified in this possible world typed as a prohibition.
- A prohibited behaviour can be also described implictly by defining a set possible worlds that should be avoided e.g. "all the doors must be opened" is a possible world typed as a prohibition and describes all the behaviours that should prevent from reaching this state of affairs.
* [**_Modality_**](https://purl.org/hmas/regulation#NormativeModality) :  a modality would be a particular mode in which a possible world should be interpreted e.g. as an obligation, prohibition, or permission. It is not introduced in the glossary since there is no reason to introduce it explicitly.


## Related links

* [link toward issues that are associated to the domain](https://github.com/HyperAgents/ns.hyperagents.org/issues?q=manufacturing+environment)
* [link toward issues that are associated to this motivating scenario](https://github.com/HyperAgents/ns.hyperagents.org/issues?q=safety+rules)
* [link toward related features that are associated to this motivating scenario](https://github.com/HyperAgents/ns.hyperagents.org/issues?q=norm)





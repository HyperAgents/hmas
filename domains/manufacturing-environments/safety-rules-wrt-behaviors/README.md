# Discover of Applicable Regulative Norms w.r.t. the states
Feature: Discovery of Applicable Regulative Norms w.r.t. the states

## Description

In the i3S Organization, if there is a fire, then it is forbidden for people to take the elevators and it is allowed for people to take the emergency exits. Thomas, a safety guard must ascertain that people follows the rules and adopts a good behavior. Thus, Thomas must list a set of prohibited behaviors and which behaviors are obliged or permitted. 

## Competency Questions


| ID | Question in Natural Language | Example                                                                                                                                   |
|----|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| q1  | What are the behaviours that are explicitely allowed ?        | `ex:safetyRule` a `:RegulativeNorm`  |
| q8  | What are the behaviours that are not allowed (or <=> prohibited) ?        | `ex:safetyRule` a `:RegulativeNorm`  |
| q9 | What are the behaviours that are obliged ?        | `ex:safetyRule` a `:RegulativeNorm`  |



## Glossary

* [** Prohibited Behavior Norm_**](https://purl.org/hmas/behavior#Norm): a specification of a prohibited behaviors in an organization. 



## Recommendations

* An obligatory behaviour can be described explictly with a possible world where the obligatory behaviour occurred e.g. "close all the doors" is an explicite behaviour which is verified in this possible world typed as an obligation.
* An obligatory behaviour can be also described implictly by defining a set possible worlds that should be reached e.g. "all the doors must be closed" is a possible world typed as an obligation and describes all the behaviours that should bring it about this state of affairs.
* A prohibited behaviour can be described explictly with a possible world where the prohibited behaviour occurred e.g. "open all the doors" is an explicite behaviour which is verified in this possible world typed as a prohibition.
* A prohibited behaviour can be also described implictly by defining a set possible worlds that should be avoided e.g. "all the doors must be opened" is a possible world typed as a prohibition and describes all the behaviours that should prevent from reaching this state of affairs.


## Questions

* ...

## ToDo

* ...

## Related links

* [link toward issues that are associated to the domain](https://github.com/HyperAgents/ns.hyperagents.org/issues?q=manufacturing+environment)
* [link toward issues that are associated to this motivating scenario](https://github.com/HyperAgents/ns.hyperagents.org/issues?q=safety+rules)
* [link toward related features that are associated to this motivating scenario](https://github.com/HyperAgents/ns.hyperagents.org/issues?q=norm)





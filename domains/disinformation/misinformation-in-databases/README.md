# Description

An agent, Christiano requests another artificial agent Celiano, about the list of current presidents.
Celiano has access to two huge databases (ex. DBpedia and Wikidata) to provide Christiano with an up-to-date answer.
However, Celiano encounters a problem : in DBBpedia, it is said that $(X, isThePresidentOf, England)$ (triple $T_1$), while in Wikidata, it says that $(X, isThePresidentOf, France)$ (triple $T_2$). This is a contradiction since we could assume that in such example the property $isPresidentOf$ has a range's cardinality of 1.


# Competency Questions

| ID | Question in natural language |
|---|---|
| q1 | What are the set of possible worlds ?|
| q2 | What is the Knowledge of the hyperagent Celiano ?|


# Glossary

* [**_Possible World_**](https://purl.org/hmas/regulation#Norm): a possible world is a reified set of RDF triples.
* [**_Accessibility Relation_**](https://purl.org/hmas/regulation#NormativeContext):  a N-ary relation that defines links between possible worlds.


# Related links

* [link toward issues that are associated to the domain](https://github.com/HyperAgents/ns.hyperagents.org/issues?q=disinformation)
* [link toward issues that are associated to this motivating scenario](https://github.com/HyperAgents/ns.hyperagents.org/issues?q=possible-worlds)
* [link toward related features that are associated to this motivating scenario](https://github.com/HyperAgents/ns.hyperagents.org/issues?q=possible-worlds)





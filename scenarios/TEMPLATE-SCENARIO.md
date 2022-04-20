# **Title of the motivating scenario**

** Short introduction to present the context and the problem that the motivating scenario is going to solve **


## **A short description**

** Give a short description of the covered features as a little story ? **


## **Covered features** 

The list of covered features : 
* ** Complete the list of covered features **


## **A set of examples**

** The list of examples show concrete use cases **


### The name of the use case

** Your informal use case **


## **A glossary of new terms**

List of new terms introduced by the motivating scenario :
* ** Present each item that represents a new term that the motivating scenario is going to introduce and definitions. The syntax is the following: `new term : definition of the term`  **


## **Competency questions**

** Please follow the following syntax for competency questions **
```
identifier: 1
question: ** Question  **
outcome: ** The result of your question **
exemplar_answers: 
|- ** Example of answers **

** name of file of the motivating scenario ; ** 
  -  
depends_on: [] 
```

(...)


## **Formal description** 

** Please give the formal SPARQL request **

```
cq: ** identifier of the competency question it **
query: |-
 ** Example : SELECT ?workspace ?agent WHERE { ?workspace hmas:hosts ?agent } **
output: ** Result :  { (<w>,<a>) s.t.<w> hmas:hosts <a>  }  **
```


### **Link to query the related issues** 
** Please use the search box to generate a link to the list of related issues.
Replace the following text by : (1) name of the scenario file that will be created and (2) the url to refer to related issues **

* https://github.com/HyperAgents/ns.hyperagents.org/issues?q=name-of-this-file.md

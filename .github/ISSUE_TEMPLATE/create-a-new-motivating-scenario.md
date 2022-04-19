---
name: Create a new motivating scenario
about: When a new motivating scenario should be created
title: "[CREATE MOTIVATING SCENARIO] ** Precise the name of your motivating scenario
  **"
labels: documentation, enhancement, motivating scenario
assignees: ''

---

# **Title of your new motivating scenario**


** Short introduction to present the context and the problem that the motivating scenario is going to solve **

## **A short description**

** Give a short description of the covered features as a little story ? **

## **Covered features** 

The list of covered features : 
* ** Complete the list of covered features **

## **A set of examples**

** The list of examples show concrete use cases **

### The unpacking example

Fabio Galvon unpacks a new robot in room 27 of the factory. 
    He boots the robot that start running the main controler agent. 
    The boot sequence of the robot contains a visual scanning that harvests any QR code visible arround. 
    The Agent gets a handler of its workspace (was: environment) and requests the contained descriptions of its environment including some known entry points. 
    Among the descriptions it discovers the interface to register itself to the entry point and places such a request. 
    The UI agent of Fabio shows the candidate addition to the entry point and he validates the addition. 
    The agent and the robot are now visible to the rest of the factory and vice-versa. 
    The user behind the UI Agent places requests to configure new goals for the agent controller of the robot.



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

motivating scenario1; 
  -  
depends_on: [] 
```

(...)

## **Formal description** 

** Please give the formal SPARQL request **

```
cq: ** identifier of the competency question it **
query: |-
 ** SELECT ?workspace ?agent WHERE { ?workspace hmas:hosts ?agent } **
output: ** { (<w>,<a>) s.t.<w> hmas:hosts <a>  }  **
```



### **Link to query the related issues** 
** Please use the search box to generate a link to the list of related issues.
Replace the following text by : (1) name of the scenario file that will be created and (2) the url to refer to related issues **

(name-of-your-motivating-scenario-that-will-be-created)[https://github.com/HyperAgents/ns.hyperagents.org/issues?q=name-of-your-motivating-scenario-that-will-be-created]

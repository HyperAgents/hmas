# Contributing to an ontology on GIT

## Objectives
This document provides guidelines to contribute to an ontology via GIT. 
In particular we explain the how to:
   1) create good issues or pull requests during the ontology design;
   3) link to external documentation, mailing lists, or a code of conduct ;
   4) act with the community and behavioral expectations ;
   5) how to create and link a new story.



## General rules for contributing
Be explicit and synthetic about the contribution you want to make to the project.
When contributing to this repository, please first discuss the change you wish to make :
1. by opening an issue before by following the rules how to open an issue (cf. Section~1); 
2. discuss the problem with the different contributors by following the code of conduct (cf. Section~2);
3. if a new feature is needed to the project, then create a new story by following the methodology  (cf. Section~3);
4. do a pull request and wait for approval by following the pull request process (cf. Section~4).



## Open an issue

Rules to open an issue : 
   * be sure that the issue has not been opened/closed before ;
   * do not use an existing issue to talk about another issues that should be opened ;
   * if the issue has been addressed and is closed, maybe it needs to be re-opened (how to do that ?) ;
   * the issue title should be specific and should address only one single issue? 
   * the title structure of issues is ... ?
   e.g.  Create/Update/Delete/UseAPropertyFrom/ProblemWith ClassName/Property/Definition / General question ? / Bug : ... / ???



## Motivating scenarios (or stories?)



A motivating scenario is a small story problem that provides a short description and a set of informal and intuitive examples to the problem it talks about. Usually, it implicitly bring with it an informal and intended semantics hidden behind natural language descriptions. [Source: SAMOD]

This is a shared common space to share stories for the HyperAgents project. A story is a template for collecting requirements.

### A story is composed of:

    Agent
        It is a research-based description of a typical user.
        It contains attributes such as name, age, occupation (if the persona has more than one role, indicate which one is their primary role and which one(s) the secondary role(s)), and relevant characteristics of the person such as their knowledge and skills and their interests.
     Goal
        It is a short textual description of the goal(s) that the persona needs to be addressed in the story.
        maximum number of characters: 1200
        The goal(s) is(are) also represented by a short (maximum 5) list of keywords.
    Scenario
        It is a story describing how the persona's task/need/problem is solved before, during and after interaction with the resource/software/service being developed.
        maximum number of characters: 1200
    Competency questions (CQs)
        Question(s) the persona needs the resource/software/service to answer for satisfying their task/need/problem.
    Resources (optional)
        List of resources (with references/links) where it is expected or known that the persona can find what she's looking for.

###  How to create a story

There is one folder for each Agent, named with the name of the Agent and their primary occupation.

    Check all existing Agents (there is one subfolder for each Persona in the "stories" folder), in order to see if there is already the Persona you need for your story. You will find a readme file in each folder, describing the Persona.
    If you find an Agent that suits you, create a new file in the respective folder, named Name-of-the-persona#progressive-number_KeywordRepresentingTheMainGoal.md, and fill the file with your story, following this example.
    If not, create a new folder, named Name-of-the-agent: Primary Occupation. If the persona has more than one role, use the primary role for naming the folder. Then, create a readme file (readme.md) describing the persona (see this example), and then a file with your story as this example.
    Besides providing information about the four components of the story, you should additionally fill in a table with this information:

    ID (Name-of-the-agent#progressive-number_KeywordRepresentingTheMainGoal)
    Agent (name of the agent)
    Keywords (representing their goals)
    WP (WPs involved in the story)
    Pilots (pilots involved in the story)
    Priority based on a “wow” scale, reflecting the impact that would be achieved by addressing the story, choosing from:
        must have (i.e. it is something that is already supported in other systems, it is state of the art)
        life improver (i.e. I would be able to make the same discovery/work in significant less time)
        life changer (i.e. I would be able to make discoveries/works that now cannot be done or are extremely hard to do)
        breakthrough (i.e. this would be a breakthrough in my field)

    After completing your story, you should update the "List of agents" and/or the "List of stories" in this README.md file.

    If you created a new Agent: add to "List of agents" the name of the folder, and a link to the folder, following the examples. Then, add to "List of stories" the name of the story you created, and a link to the file.
    If you reused an existing Persona for your story: add to "List of stories" the name of the story you created, and a link to the file.



Actually in our case, a motivating scenario is characterized by :
* name: e.g. robot unpacking in a workshop # characterises the motivating scenario
* description: natural language description that presents a problem to address
  Some description of the motivating scenario
* examples:
    Fabio Galvon unpacks a new robot in room 27 of the factory. 
    He boots the robot that start running the main controler agent. 
    The boot sequence of the robot contains a visual scanning that harvests any QR code visible arround. 
    The Agent gets a handler of its workspace (was: environment) and requests which contains descriptions of its environment including some known entry points. 
    "It discovers the interface to register itself" to the entrypoint and places such a request. 
    The UI agent of Fabio shows the candidate addition to the entry point and he validates the addition. 
    The agent and the robot is now visible to the rest of the factory and vice-versa. 
    The user behind the UI Agent places requests to configure new goals for the agent controler of the robot.
* glossary of terms: A glossary of terms is a list of term-definition pairs related to terms that are commonly used for talking about the domain in consideration. The term in each pair may be composed by one or more words or verbs, or even by a brief sentence, while the related definition is a natural language explanation of the meaning of such term. The terminology used for naming terms and for describing them must be as close as possible to the domain language. For example:
  1) Robot: A machine resembling a human being and able to replicate certain human movements and functions automatically.
  2) Workshop: A room or building in which goods are manufactured or repaired.


## Pull Request Process

1. Ensure any install or build dependencies are removed before the end of the layer when doing a 
   build.
2. Update the README.md with details of changes to the interface, this includes new environment 
   variables, exposed ports, useful file locations and container parameters.
3. Increase the version numbers in any examples files and the README.md to the new version that this
   Pull Request would represent. The versioning scheme we use is [SemVer](http://semver.org/). 
4. (Idea: The Pull Request must have the following title "Verb + object of the PR + ref to issue" e.g. Update definition of :Artifact #IssueArtifact" 
   Create class :Toto #IssueToto 
   A- The Pull Request's name must be as concise as possible
   B- The PR must corresponds to an issue and only one issue (Don't do a BIG PR that groups many different issues !) ) 
5. You may merge the Pull Request in once you have the sign-off of the different institution, or if you 
   do not have permission to do that, you may request the second reviewer to merge it for you.



## References 

This document is inspired from : 

https://mozillascience.github.io/working-open-workshop/contributing/ 

https://opensource.guide/fr/starting-a-project/

SAMOD methodology [REF](https://essepuntato.it/samod/)


[Polifonia project](https://github.com/polifonia-project/stories)

Examples of contributing files :

https://github.com/atom/atom/blob/master/CONTRIBUTING.md

https://github.com/rails/rails/blob/main/CONTRIBUTING.md

https://github.com/opengovernment/opengovernment/blob/master/CONTRIBUTING.md


## TODOs
> Ideas/questions for the contributing doc to add : 
* propose a standard name for title of issues / PR / for classes and properties ? How to name a new class / property ?  => Open A new issue about e.g. considering a new CamelCase notation for classes/properties ??
* the PR is usefull to make a vote and decide if we merge : say it !
* talk about how to decide if a set of PR is considered as a new version : it is when all the stories features has been addressed and accepted.
* how motivating scenario must be documented somewhere and how ontologies links to these motivating scenarios  
* the structure of this file should be : each step of the contributing process is explained by the plan section/subsections ?
* separate code of conduct from the contributing file ? 
* add in PR process when we close the issue i.e. when it seems there is a consensus and capture the consensus and rationale in the ontology itself 
* add in the PR process that you must keep a record summarizing the reflections in your PR by making a link toward the issue that is related and how to do that.
* take from polifonia the methodology to create a new story ?? 
* considering specifical files that refers all stories 
* should we consider a set of people with roles and stories in our approach ? here we would call this set : set of agents.
* Create an explicit file CODE-OF-CONDUCT.md (cf. https://opensource.guide/fr/code-of-conduct/)   where we present the behaviour we expect from the community and where we present the use of the different classes/properties e.g. put in this file the section #good-practices (because it shouldn't be in the contributing file : ) ??











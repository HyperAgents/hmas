# Contributing

This document is inspired from : 
https://mozillascience.github.io/working-open-workshop/contributing/ 
https://opensource.guide/fr/starting-a-project/

Objectives of this document :
* provide a CONTRIBUTING file template about how to apply via GIT the SAMOD methodology
* explain the methodology how to:
   1) create good issues or pull requests ;
   3) link to external documentation, mailing lists, or a code of conduct ;
   4) act with the community and behavioral expectations ;
   5) how to create a new story.

Ideas/questions for the contributing doc to add : 
* propose a standard name for title of issues / PR / for classes and properties ? How to name a new class / property ?  => Open A new issue about e.g. considering a new CamelCase notation for classes/properties ??
* the PR is usefull to make a vote and decide if we merge : say it !
* talk about how to decide if a set of PR is considered as a new version : it is when all the stories features has been addressed and accepted.
* how motivating scenario must be documented somewhere and how ontologies links to these motivating scenarios  
* the structure of this file should be : each step of the contributing process is explained by the plan section/subsections ?
* separate code of conduct from the contributing file ? 
* add in PR process when we close the issue i.e. when it seems there is a consensus and capture the consensus and rationale in the ontology itself 
* add in the PR process that you must keep a record summarizing the reflections in your PR by making a link toward the issue that is related and how to do that.
* take from polifonia the methodology to create a new story ?? 

When contributing to this repository, please first discuss the change you wish to make :
1. by opening an issue before by following the rules how to open an issue ; 
2. discuss the problem with the different contributors by following the code of conduct ;
3. if a new feature is needed to the project, then follow the methodology how to create a new story ;
4. do a pull request and wait for approval by following the pull request process.



## Open an issue


Rules to open an issue : 
   * be sure that the issue has not been opened/closed before 
   * Do not use an existing issue to talk about another issues that should be open
   * If the issue has been addressed and is closed, maybe it needs to be re-opened (how to do that ?)
   * The issue title should be specific and should address only one single issue. 

## Code of conduct

Please note we have a code of conduct, please follow it in all your interactions with the project.


### Our Pledge

In the interest of fostering an open and welcoming environment, we as
contributors and maintainers pledge to making participation in our project and
our community a harassment-free experience for everyone, regardless of age, body
size, disability, ethnicity, gender identity and expression, level of experience,
nationality, personal appearance, race, religion, or sexual identity and
orientation.

### Our Standards

Examples of behavior that contributes to creating a positive environment
include:

* Using welcoming and inclusive language
* Being respectful of differing viewpoints and experiences
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery and unwelcome sexual attention or
advances
* Trolling, insulting/derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or electronic
  address, without explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

### Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable
behavior and are expected to take appropriate and fair corrective action in
response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or
reject comments, commits, code, wiki edits, issues, and other contributions
that are not aligned to this Code of Conduct, or to ban temporarily or
permanently any contributor for other behaviors that they deem inappropriate,
threatening, offensive, or harmful.

### Scope

This Code of Conduct applies both within project spaces and in public spaces
when an individual is representing the project or its community. Examples of
representing a project or community include using an official project e-mail
address, posting via an official social media account, or acting as an appointed
representative at an online or offline event. Representation of a project may be
further defined and clarified by project maintainers.

### Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported by contacting the project team at hyperagents@listes.emse.fr. All
complaints will be reviewed and investigated and will result in a response that
is deemed necessary and appropriate to the circumstances. The project team is
obligated to maintain confidentiality with regard to the reporter of an incident.
Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good
faith may face temporary or permanent repercussions as determined by other
members of the project's leadership.













## Motivating scenarios (or stories?)











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

















## Good practices

This party should be removed ?

### Using the current classes and properties

1) Use rather hmas:directlyContains and do not use hmas:transitivelyContains (only for requests)

Related issues :
https://github.com/HyperAgents/ns.hyperagents.org/issues/6


2) When should you use rdfs:seeAlso instead of dct:source?

Use dct:source when the described resource is derived from the related resource in whole or in part e.g. a particular comment that justifies the described resource or the motivating scenario.

Use rdfs:seeAlso for every resources that is related to the described resource e.g. the rationale given in issues, similar resources.

Related issues :
...

3) Use rdfs:comments to give the definition of your described resource
 
Related issues :
...

### Creating new classes and properties

1) Do not duplicate the same difference in properties, classes and ranges/domains

We mean by do not duplicating e.g. do not create a class hmas:containsArtifact if hmas:contains is enough since the type of ressource allows you to know the nature of the container. 

Related issues :
https://github.com/HyperAgents/ns.hyperagents.org/issues/6

### Modifying a class or a property




### Deleting a class or a property

1) If a class is not necessary for the ontology and not justified by a motivating scenario, then this class can be delete.

We seek to express our ontology in the most minimalist and simplest way possible. 
We believe that the elegance of a formalism lies in its simplicity and generalization. 
Apply the philosophy of an Occam's razor.

Related issues :
https://github.com/HyperAgents/ns.hyperagents.org/issues/6












# Test Report Markdown export

This file is an export of the RDF test report made out of [EARL vocabulary](https://www.w3.org/TR/EARL10/)

This test is powered by Corese, check the [website](https://project.inria.fr/corese/) and the [repository](https://github.com/Wimmics/corese)

The original test report is available in turtle syntax [here](./data-test-manual-NicoRobertIn-2024-02-02T15-06-44.ttl).

# Test Context

Here is some context about under which context this test was made

|Assertor|[NicoRobertIn](https://github.com/NicoRobertIn)|
|----|-----|
|Title|NicoRobertIn using manual script|
|Description|Test triggered by [@NicoRobertIn](https://github.com/NicoRobertIn) by manual trigger|
|Script|[suite.py](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/data/suite.py)
|Date|2024-02-02 15:06:42|

***


# Statistic summary

Here is a short overview for this test report

47 Assertions

:boom:1 MajorFail, :exclamation:4 MinorFail, :warning:9 CannotTell, :grey_question:2 NotTested, :white_check_mark:31 Pass

<div  style="border-radius: 12px; height: 25px; overflow: hidden"><img src="../assets/red.png" width="2%" height="25px"/><img src="../assets/orange.png" width="8%" height="25px"/><img src="../assets/grey.png" width="19%" height="25px"/><img src="../assets/white.png" width="4%" height="25px"/><img src="../assets/green.png" width="67%" height="25px"/></div>

<br/>

According to the [EARL](https://www.w3.org/TR/EARL10-Schema/) vocabulary, each outcome type means:
* :x: Fail: The subject failed the test. 
* :warning: CannotTell: It is unclear if the subject passed or failed the test. This happens when an automated test requires human judgement to make a definite decision.
* :grey_question: NotTested:  The test has not been carried out. Here this is because a previous test that was mandatory to be passed did not end up as Pass.
* :white_check_mark: Pass: The subject passed the test.

***


# MajorFail Assertions

Here is the chapter related to the MajorFail assertion

:boom:1 MajorFail assertions

<details>
<summary>Fold/Unfold the 1 summary and details</summary>

## MajorFail Assertions Summary

[Jump to statistic summary](#statistic-summary)

:boom:1 MajorFail assertions

|*Jump*|*Number*|*Status*|*Subject*|*Criterion*|*Title*|*Link*|
|------|--------|--------|---------|-----------|-------|------|
|[Table top](#majorfail-assertions-summary)|<div id="summary-MajorFail-1">1/1</div>|:boom:*MajorFail*|`manufacturing-environments-safety-rules`|[syntax](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#syntax)|Test subject has syntax errors|[Jump](#majorfail-assertion-number-1)|

***

## MajorFail Assertion Details

This subchapter gives more details to the :boom:MajorFail assertions

### MajorFail Assertion number 1

[Jump to summary definition](#summary-MajorFail-1)

:boom:MajorFail assertion
#### Subject detail
|Name|manufacturing-environments-safety-rules|
|----|----|
|Title|Standalone dataset domains/manufacturing-environments/safety-rules/dataset.ttl from branch 182-uc-manufacturing|
|Composition|- [Dataset manufacturing-environments/safety-rules/dataset.ttl](https://github.com/HyperAgents/hmas/blob/182-uc-manufacturing/domains/manufacturing-environments/safety-rules/dataset.ttl)|

#### Criterion detail
|Identifier|[syntax](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#syntax)|
|----|----|
|Title|Syntax test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:boom:MajorFail|
|----|----|
|Title|Test subject has syntax errors|
|Description|Encountered "." at line 21, column 112.|

***

</details>

***


# MinorFail Assertions

Here is the chapter related to the MinorFail assertion

:exclamation:4 MinorFail assertions

<details>
<summary>Fold/Unfold the 4 summary and details</summary>

## MinorFail Assertions Summary

[Jump to statistic summary](#statistic-summary)

:exclamation:4 MinorFail assertions

|*Jump*|*Number*|*Status*|*Subject*|*Criterion*|*Title*|*Link*|
|------|--------|--------|---------|-----------|-------|------|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-1">1/4</div>|:exclamation:*MinorFail*|`manufacturing-environments-discover-platforms`|[term-recognition](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#term-recognition)|Unknown ontology term|[Jump](#minorfail-assertion-number-1)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-2">2/4</div>|:exclamation:*MinorFail*|`manufacturing`|[term-recognition](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#term-recognition)|Unknown ontology term|[Jump](#minorfail-assertion-number-2)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-3">3/4</div>|:exclamation:*MinorFail*|`manufacturing`|[term-recognition](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#term-recognition)|Unknown ontology term|[Jump](#minorfail-assertion-number-3)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-4">4/4</div>|:exclamation:*MinorFail*|`logistics-structure-organization`|[term-recognition](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#term-recognition)|Unknown ontology term|[Jump](#minorfail-assertion-number-4)|

***

## MinorFail Assertion Details

This subchapter gives more details to the :exclamation:MinorFail assertions

### MinorFail Assertion number 1

[Jump to summary definition](#summary-MinorFail-1)

:exclamation:MinorFail assertion
#### Subject detail
|Name|manufacturing-environments-discover-platforms|
|----|----|
|Title|Standalone dataset domains/manufacturing-environments/discover-platforms/dataset.ttl from branch 182-uc-manufacturing|
|Composition|- [Dataset manufacturing-environments/discover-platforms/dataset.ttl](https://github.com/HyperAgents/hmas/blob/182-uc-manufacturing/domains/manufacturing-environments/discover-platforms/dataset.ttl)|

#### Criterion detail
|Identifier|[term-recognition](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#term-recognition)|
|----|----|
|Title|Term recognition test|
|Description|A test meant to detect if all the terms from the subject that are from the ontology namespace are indeed defined in the ontology|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|Unknown ontology term|
|Description|The term "hasResourceProfile" was used in the fragment but not defined in the ontology|
|Pointer|<pre lang="Turtle"><code>&#60;http://example.org/platformSaintEtienne> ns1:hasResourceProfile &#60;http://example.org/platformSaintEtienneProfile> .</code></pre>|

***
### MinorFail Assertion number 2

[Jump to summary definition](#summary-MinorFail-2)

:exclamation:MinorFail assertion
#### Subject detail
|Name|manufacturing|
|----|----|
|Title|Standalone use case use-cases/manufacturing/dataset-v1.ttl from branch 182-uc-manufacturing|
|Composition|- [Use case manufacturing/dataset-v1.ttl](https://github.com/HyperAgents/hmas/blob/182-uc-manufacturing/use-cases/manufacturing/dataset-v1.ttl)|

#### Criterion detail
|Identifier|[term-recognition](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#term-recognition)|
|----|----|
|Title|Term recognition test|
|Description|A test meant to detect if all the terms from the subject that are from the ontology namespace are indeed defined in the ontology|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|Unknown ontology term|
|Description|The term "Platform" was used in the fragment but not defined in the ontology|
|Pointer|<pre lang="Turtle"><code>&#60;https://ns.inria.fr/hmas/#platform> rdf:type &#60;https://purl.org/hmas/Platform> .</code></pre>|

***
### MinorFail Assertion number 3

[Jump to summary definition](#summary-MinorFail-3)

:exclamation:MinorFail assertion
#### Subject detail
|Name|manufacturing|
|----|----|
|Title|Standalone use case use-cases/manufacturing/dataset-v1.ttl from branch 182-uc-manufacturing|
|Composition|- [Use case manufacturing/dataset-v1.ttl](https://github.com/HyperAgents/hmas/blob/182-uc-manufacturing/use-cases/manufacturing/dataset-v1.ttl)|

#### Criterion detail
|Identifier|[term-recognition](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#term-recognition)|
|----|----|
|Title|Term recognition test|
|Description|A test meant to detect if all the terms from the subject that are from the ontology namespace are indeed defined in the ontology|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|Unknown ontology term|
|Description|The term "hasOutput" was used in the fragment but not defined in the ontology|
|Pointer|<pre lang="Turtle"><code>&lowbar;:b4218 owl:hasValue &#60;https://purl.org/hmas/hasOutput> .&#10;&lowbar;:b4266 sh:path &#60;https://purl.org/hmas/hasOutput> .&#10;&lowbar;:b4307 sh:path &#60;https://purl.org/hmas/hasOutput> .</code></pre>|

***
### MinorFail Assertion number 4

[Jump to summary definition](#summary-MinorFail-4)

:exclamation:MinorFail assertion
#### Subject detail
|Name|logistics-structure-organization|
|----|----|
|Title|Standalone dataset domains/logistics/structure-organization/dataset.ttl from branch 182-uc-manufacturing|
|Composition|- [Dataset logistics/structure-organization/dataset.ttl](https://github.com/HyperAgents/hmas/blob/182-uc-manufacturing/domains/logistics/structure-organization/dataset.ttl)|

#### Criterion detail
|Identifier|[term-recognition](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#term-recognition)|
|----|----|
|Title|Term recognition test|
|Description|A test meant to detect if all the terms from the subject that are from the ontology namespace are indeed defined in the ontology|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|Unknown ontology term|
|Description|The term "hasResourceProfile" was used in the fragment but not defined in the ontology|
|Pointer|<pre lang="Turtle"><code>&#60;http://example.org/FL&lowbar;Logistics> ns1:hasResourceProfile &#60;http://example.org/FL&lowbar;LogisticsProfile> .</code></pre>|

***

</details>

***


# CannotTell Assertions

Here is the chapter related to the CannotTell assertion

:warning:9 CannotTell assertions

<details>
<summary>Fold/Unfold the 9 summary and details</summary>

## CannotTell Assertions Summary

[Jump to statistic summary](#statistic-summary)

:warning:9 CannotTell assertions

|*Jump*|*Number*|*Status*|*Subject*|*Criterion*|*Title*|*Link*|
|------|--------|--------|---------|-----------|-------|------|
|[Table top](#cannottell-assertions-summary)|<div id="summary-CannotTell-1">1/9</div>|:warning:*CannotTell*|`manufacturing-environments-discover-behavior-specifications`|[prefix-validity](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#prefix-validity)|Possible prefix typo|[Jump](#cannottell-assertion-number-1)|
|[Table top](#cannottell-assertions-summary)|<div id="summary-CannotTell-2">2/9</div>|:warning:*CannotTell*|`manufacturing`|[prefix-validity](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#prefix-validity)|Possible prefix typo|[Jump](#cannottell-assertion-number-2)|
|[Table top](#cannottell-assertions-summary)|<div id="summary-CannotTell-3">3/9</div>|:warning:*CannotTell*|`manufacturing`|[prefix-validity](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#prefix-validity)|Possible prefix typo|[Jump](#cannottell-assertion-number-3)|
|[Table top](#cannottell-assertions-summary)|<div id="summary-CannotTell-4">4/9</div>|:warning:*CannotTell*|`manufacturing`|[prefix-validity](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#prefix-validity)|Possible prefix typo|[Jump](#cannottell-assertion-number-4)|
|[Table top](#cannottell-assertions-summary)|<div id="summary-CannotTell-5">5/9</div>|:warning:*CannotTell*|`manufacturing`|[prefix-validity](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#prefix-validity)|Possible prefix typo|[Jump](#cannottell-assertion-number-5)|
|[Table top](#cannottell-assertions-summary)|<div id="summary-CannotTell-6">6/9</div>|:warning:*CannotTell*|`manufacturing`|[prefix-validity](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#prefix-validity)|Possible prefix typo|[Jump](#cannottell-assertion-number-6)|
|[Table top](#cannottell-assertions-summary)|<div id="summary-CannotTell-7">7/9</div>|:warning:*CannotTell*|`manufacturing`|[prefix-validity](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#prefix-validity)|Possible prefix typo|[Jump](#cannottell-assertion-number-7)|
|[Table top](#cannottell-assertions-summary)|<div id="summary-CannotTell-8">8/9</div>|:warning:*CannotTell*|`manufacturing`|[prefix-validity](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#prefix-validity)|Possible prefix typo|[Jump](#cannottell-assertion-number-8)|
|[Table top](#cannottell-assertions-summary)|<div id="summary-CannotTell-9">9/9</div>|:warning:*CannotTell*|`manufacturing`|[prefix-validity](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#prefix-validity)|Possible prefix typo|[Jump](#cannottell-assertion-number-9)|

***

## CannotTell Assertion Details

This subchapter gives more details to the :warning:CannotTell assertions

### CannotTell Assertion number 1

[Jump to summary definition](#summary-CannotTell-1)

:warning:CannotTell assertion
#### Subject detail
|Name|manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Standalone dataset domains/manufacturing-environments/discover-behavior-specifications/dataset.ttl from branch 182-uc-manufacturing|
|Composition|- [Dataset manufacturing-environments/discover-behavior-specifications/dataset.ttl](https://github.com/HyperAgents/hmas/blob/182-uc-manufacturing/domains/manufacturing-environments/discover-behavior-specifications/dataset.ttl)|

#### Criterion detail
|Identifier|[prefix-validity](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#prefix-validity)|
|----|----|
|Title|Term validity test|
|Description|A test case checking if all the prefixes are not too close from the most used existing namespaces (according to prefix cc)|

#### Outcome Detail
|Type|:warning:CannotTell|
|----|----|
|Title|Possible prefix typo|
|Description|The prefix http://www.w3.org/2011/http# seems suspicious. Did you mean one of these prefixes?|
|Pointer|<pre lang="Turtle"><code>Prefix usage in the subject file:&#10;@prefix owl: &#60;http://www.w3.org/2002/07/owl#> .&#10;@prefix ns1: &#60;http://www.w3.org/2011/http#> . &#10; &#60;http://example.org/coapForm> ns1:methodName "PUT" . &#10; &#60;http://example.org/httpForm> ns1:methodName "PUT" .</code></pre>|
|Pointer|<pre lang="Turtle"><code>Common prefix found&#10;@prefix httpvoc: &#60;http://www.w3.org/2006/http#> .</code></pre>|

***
### CannotTell Assertion number 2

[Jump to summary definition](#summary-CannotTell-2)

:warning:CannotTell assertion
#### Subject detail
|Name|manufacturing|
|----|----|
|Title|Standalone use case use-cases/manufacturing/dataset-v1.ttl from branch 182-uc-manufacturing|
|Composition|- [Use case manufacturing/dataset-v1.ttl](https://github.com/HyperAgents/hmas/blob/182-uc-manufacturing/use-cases/manufacturing/dataset-v1.ttl)|

#### Criterion detail
|Identifier|[prefix-validity](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#prefix-validity)|
|----|----|
|Title|Term validity test|
|Description|A test case checking if all the prefixes are not too close from the most used existing namespaces (according to prefix cc)|

#### Outcome Detail
|Type|:warning:CannotTell|
|----|----|
|Title|Possible prefix typo|
|Description|The prefix https://ns.inria.fr/hmas/ seems suspicious. Did you mean one of these prefixes?|
|Pointer|<pre lang="Turtle"><code>Prefix usage in the subject file:&#10;@prefix owl: &#60;http://www.w3.org/2002/07/owl#> .&#10;@prefix xsh: &#60;http://www.w3.org/ns/shacl#> .&#10;@prefix ns2: &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site#> .&#10;@prefix ns1: &#60;https://purl.org/hmas/> .&#10;@prefix sh: &#60;http://www.w3.org/ns/shacl#> .&#10;@prefix rdf: &#60;http://www.w3.org/1999/02/22-rdf-syntax-ns#> . &#10; &#60;https://ns.inria.fr/hmas/#platform> rdf:type &#60;https://purl.org/hmas/Platform> ;&#10;ns1:hasProfile &#60;https://ns.inria.fr/hmas/> . &#10; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site#> rdf:type ns1:ResourceProfile ;&#10;ns1:exposesSignifier &lowbar;:b4369 ;&#10;ns1:isProfileOf &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site#workspace> . &#10; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/artifacts/robotic-arm-1#artifact> rdf:type ns1:Artifact ;&#10;ns1:isHostedOn &#60;https://ns.inria.fr/hmas/#platformplatform> . &#10; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/agents/agent-d#agent> rdf:type ns1:Agent ;&#10;ns1:hasProfile &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/agents/agent-d#> ;&#10;ns1:isContainedIn &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site#Workspace> ;&#10;ns1:isHostedOn &#60;https://ns.inria.fr/hmas/#platformplatform> . &#10; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/agents/agent-c#agent> rdf:type ns1:Agent ;&#10;ns1:hasProfile &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/agents/agent-c#> ;&#10;ns1:isContainedIn &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site#Workspace> ;&#10;ns1:isHostedOn &#60;https://ns.inria.fr/hmas/#platformplatform> . &#10; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/agents/agent-b#agent> rdf:type ns1:Agent ;&#10;ns1:hasProfile &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/agents/agent-b#> ;&#10;ns1:isContainedIn &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site#Workspace> ;&#10;ns1:isHostedOn &#60;https://ns.inria.fr/hmas/#platformplatform> . &#10; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/artifacts/robotic-arm-1#> rdf:type ns1:ResourceProfile ;&#10;ns1:exposesSignifier &lowbar;:b4348 ;&#10;ns1:exposesSignifier &lowbar;:b4349 ;&#10;ns1:exposesSignifier &lowbar;:b4350 ;&#10;ns1:exposesSignifier &lowbar;:b4351 ;&#10;ns1:exposesSignifier &lowbar;:b4352 ;&#10;ns1:exposesSignifier &lowbar;:b4353 ;&#10;ns1:exposesSignifier &lowbar;:b4354 ;&#10;ns1:exposesSignifier &lowbar;:b4355 ;&#10;ns1:exposesSignifier &lowbar;:b4356 ;&#10;ns1:isProfileOf &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/artifacts/robotic-arm-1#artifact> . &#10; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/artifacts/robotic-arm-2#artifact> rdf:type ns1:Artifact ;&#10;ns1:isHostedOn &#60;https://ns.inria.fr/hmas/#platformplatform> . &#10; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/artifacts/truck#artifact> rdf:type ns1:Artifact ;&#10;ns1:isHostedOn &#60;https://ns.inria.fr/hmas/#platformplatform> . &#10; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/artifacts/truck#> rdf:type ns1:ResourceProfile ;&#10;ns1:exposesSignifier &lowbar;:b4366 ;&#10;ns1:exposesSignifier &lowbar;:b4367 ;&#10;ns1:exposesSignifier &lowbar;:b4368 ;&#10;ns1:isProfileOf &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/artifacts/truck#artifact> . &#10; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/artifacts/robotic-arm-2#> rdf:type ns1:ResourceProfile ;&#10;ns1:exposesSignifier &lowbar;:b4357 ;&#10;ns1:exposesSignifier &lowbar;:b4358 ;&#10;ns1:exposesSignifier &lowbar;:b4359 ;&#10;ns1:exposesSignifier &lowbar;:b4360 ;&#10;ns1:exposesSignifier &lowbar;:b4361 ;&#10;ns1:exposesSignifier &lowbar;:b4362 ;&#10;ns1:exposesSignifier &lowbar;:b4363 ;&#10;ns1:exposesSignifier &lowbar;:b4364 ;&#10;ns1:exposesSignifier &lowbar;:b4365 ;&#10;ns1:isProfileOf &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/artifacts/robotic-arm-2#artifact> . &#10; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site#workspace> rdf:type ns1:Workspace ;&#10;ns2:hasProfile &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site#> ;&#10;ns1:contains &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/artifacts/robotic-arm-1#artifact> ;&#10;ns1:contains &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/artifacts/robotic-arm-2#artifact> ;&#10;ns1:contains &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/artifacts/truck#artifact> ;&#10;ns1:isHostedOn &#60;https://ns.inria.fr/hmas/#platformplatform> .&#10;&lowbar;:b4346 sh:hasValue &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site> .</code></pre>|
|Pointer|<pre lang="Turtle"><code>Similar prefix found in file .\use-cases\manufacturing\dataset-v1.ttl&#10;Prefix found: https://ns.inria.fr/hmas/#&#10;@prefix owl: &#60;http://www.w3.org/2002/07/owl#> .&#10;@prefix ns1: &#60;https://purl.org/hmas/> .&#10;@prefix rdf: &#60;http://www.w3.org/1999/02/22-rdf-syntax-ns#> . &#10; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/artifacts/robotic-arm-2#artifact> ns1:isHostedOn &#60;https://ns.inria.fr/hmas/#platformplatform> . &#10; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/artifacts/truck#artifact> ns1:isHostedOn &#60;https://ns.inria.fr/hmas/#platformplatform> . &#10; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/agents/agent-c#agent> ns1:isHostedOn &#60;https://ns.inria.fr/hmas/#platformplatform> . &#10; &#60;https://ns.inria.fr/hmas/#platform> rdf:type ns1:Platform ;&#10;ns1:hasProfile &#60;https://ns.inria.fr/hmas/> . &#10; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site#workspace> ns1:isHostedOn &#60;https://ns.inria.fr/hmas/#platformplatform> . &#10; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/artifacts/robotic-arm-1#artifact> ns1:isHostedOn &#60;https://ns.inria.fr/hmas/#platformplatform> . &#10; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/agents/agent-d#agent> ns1:isHostedOn &#60;https://ns.inria.fr/hmas/#platformplatform> . &#10; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/agents/agent-b#agent> ns1:isHostedOn &#60;https://ns.inria.fr/hmas/#platformplatform> .</code></pre>|

***
### CannotTell Assertion number 3

[Jump to summary definition](#summary-CannotTell-3)

:warning:CannotTell assertion
#### Subject detail
|Name|manufacturing|
|----|----|
|Title|Standalone use case use-cases/manufacturing/dataset-v1.ttl from branch 182-uc-manufacturing|
|Composition|- [Use case manufacturing/dataset-v1.ttl](https://github.com/HyperAgents/hmas/blob/182-uc-manufacturing/use-cases/manufacturing/dataset-v1.ttl)|

#### Criterion detail
|Identifier|[prefix-validity](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#prefix-validity)|
|----|----|
|Title|Term validity test|
|Description|A test case checking if all the prefixes are not too close from the most used existing namespaces (according to prefix cc)|

#### Outcome Detail
|Type|:warning:CannotTell|
|----|----|
|Title|Possible prefix typo|
|Description|The prefix https://api.interactions.ics.unisg.ch/cherrybot1/ seems suspicious. Did you mean one of these prefixes?|
|Pointer|<pre lang="Turtle"><code>Prefix usage in the subject file:&#10;@prefix owl: &#60;http://www.w3.org/2002/07/owl#> .&#10;@prefix xsh: &#60;http://www.w3.org/ns/shacl#> .&#10;@prefix sh: &#60;http://www.w3.org/ns/shacl#> .&#10;&lowbar;:b4265 sh:hasValue &#60;https://api.interactions.ics.unisg.ch/cherrybot1/gripper> .&#10;&lowbar;:b4287 sh:hasValue &#60;https://api.interactions.ics.unisg.ch/cherrybot1/operator/%7Btoken%7D> .&#10;&lowbar;:b4260 sh:hasValue &#60;https://api.interactions.ics.unisg.ch/cherrybot1/tcp/target> .&#10;&lowbar;:b4255 sh:hasValue &#60;https://api.interactions.ics.unisg.ch/cherrybot1/tcp> .&#10;&lowbar;:b4283 sh:hasValue &#60;https://api.interactions.ics.unisg.ch/cherrybot1/gripper> .&#10;&lowbar;:b4278 sh:hasValue &#60;https://api.interactions.ics.unisg.ch/cherrybot1/tcp/target> .&#10;&lowbar;:b4250 sh:hasValue &#60;https://api.interactions.ics.unisg.ch/cherrybot1/operator> .&#10;&lowbar;:b4273 sh:hasValue &#60;https://api.interactions.ics.unisg.ch/cherrybot1/operator> .&#10;&lowbar;:b4269 sh:hasValue &#60;https://api.interactions.ics.unisg.ch/cherrybot1/initialize> .</code></pre>|
|Pointer|<pre lang="Turtle"><code>Similar prefix found in file .\use-cases\manufacturing\dataset-v1.ttl&#10;Prefix found: https://api.interactions.ics.unisg.ch/cherrybot2/&#10;@prefix owl: &#60;http://www.w3.org/2002/07/owl#> .&#10;@prefix xsh: &#60;http://www.w3.org/ns/shacl#> .&#10;@prefix sh: &#60;http://www.w3.org/ns/shacl#> .&#10;&lowbar;:b5202 sh:hasValue &#60;https://api.interactions.ics.unisg.ch/cherrybot2/operator/%7Btoken%7D> .&#10;&lowbar;:b5179 sh:hasValue &#60;https://api.interactions.ics.unisg.ch/cherrybot2/gripper> .&#10;&lowbar;:b5174 sh:hasValue &#60;https://api.interactions.ics.unisg.ch/cherrybot2/tcp/target> .&#10;&lowbar;:b5169 sh:hasValue &#60;https://api.interactions.ics.unisg.ch/cherrybot2/tcp> .&#10;&lowbar;:b5197 sh:hasValue &#60;https://api.interactions.ics.unisg.ch/cherrybot2/gripper> .&#10;&lowbar;:b5164 sh:hasValue &#60;https://api.interactions.ics.unisg.ch/cherrybot2/operator> .&#10;&lowbar;:b5192 sh:hasValue &#60;https://api.interactions.ics.unisg.ch/cherrybot2/tcp/target> .&#10;&lowbar;:b5187 sh:hasValue &#60;https://api.interactions.ics.unisg.ch/cherrybot2/operator> .&#10;&lowbar;:b5183 sh:hasValue &#60;https://api.interactions.ics.unisg.ch/cherrybot2/initialize> .</code></pre>|

***
### CannotTell Assertion number 4

[Jump to summary definition](#summary-CannotTell-4)

:warning:CannotTell assertion
#### Subject detail
|Name|manufacturing|
|----|----|
|Title|Standalone use case use-cases/manufacturing/dataset-v1.ttl from branch 182-uc-manufacturing|
|Composition|- [Use case manufacturing/dataset-v1.ttl](https://github.com/HyperAgents/hmas/blob/182-uc-manufacturing/use-cases/manufacturing/dataset-v1.ttl)|

#### Criterion detail
|Identifier|[prefix-validity](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#prefix-validity)|
|----|----|
|Title|Term validity test|
|Description|A test case checking if all the prefixes are not too close from the most used existing namespaces (according to prefix cc)|

#### Outcome Detail
|Type|:warning:CannotTell|
|----|----|
|Title|Possible prefix typo|
|Description|The prefix https://ns.inria.fr/hmas/workspaces/cup-production-site/artifacts/robotic-arm-1# seems suspicious. Did you mean one of these prefixes?|
|Pointer|<pre lang="Turtle"><code>Prefix usage in the subject file:&#10;@prefix owl: &#60;http://www.w3.org/2002/07/owl#> .&#10;@prefix ns1: &#60;https://purl.org/hmas/> .&#10;@prefix rdf: &#60;http://www.w3.org/1999/02/22-rdf-syntax-ns#> . &#10; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site#workspace> ns1:contains &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/artifacts/robotic-arm-1#artifact> . &#10; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/artifacts/robotic-arm-1#artifact> rdf:type ns1:Artifact ;&#10;ns1:isHostedOn &#60;https://ns.inria.fr/hmas/#platformplatform> . &#10; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/artifacts/robotic-arm-1#> rdf:type ns1:ResourceProfile ;&#10;ns1:exposesSignifier &lowbar;:b4348 ;&#10;ns1:exposesSignifier &lowbar;:b4349 ;&#10;ns1:exposesSignifier &lowbar;:b4350 ;&#10;ns1:exposesSignifier &lowbar;:b4351 ;&#10;ns1:exposesSignifier &lowbar;:b4352 ;&#10;ns1:exposesSignifier &lowbar;:b4353 ;&#10;ns1:exposesSignifier &lowbar;:b4354 ;&#10;ns1:exposesSignifier &lowbar;:b4355 ;&#10;ns1:exposesSignifier &lowbar;:b4356 ;&#10;ns1:isProfileOf &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/artifacts/robotic-arm-1#artifact> .</code></pre>|
|Pointer|<pre lang="Turtle"><code>Similar prefix found in file .\use-cases\manufacturing\dataset-v1.ttl&#10;Prefix found: https://ns.inria.fr/hmas/workspaces/cup-production-site/artifacts/robotic-arm-2#&#10;@prefix owl: &#60;http://www.w3.org/2002/07/owl#> .&#10;@prefix ns1: &#60;https://purl.org/hmas/> .&#10;@prefix rdf: &#60;http://www.w3.org/1999/02/22-rdf-syntax-ns#> . &#10; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/artifacts/robotic-arm-2#> rdf:type &#60;https://purl.org/hmas/ResourceProfile> ;&#10;ns1:exposesSignifier &lowbar;:b5466 ;&#10;ns1:exposesSignifier &lowbar;:b5467 ;&#10;ns1:exposesSignifier &lowbar;:b5468 ;&#10;ns1:exposesSignifier &lowbar;:b5469 ;&#10;ns1:exposesSignifier &lowbar;:b5470 ;&#10;ns1:exposesSignifier &lowbar;:b5471 ;&#10;ns1:exposesSignifier &lowbar;:b5472 ;&#10;ns1:exposesSignifier &lowbar;:b5473 ;&#10;ns1:exposesSignifier &lowbar;:b5474 ;&#10;ns1:isProfileOf &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/artifacts/robotic-arm-2#artifact> . &#10; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site#workspace> ns1:contains &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/artifacts/robotic-arm-2#artifact> . &#10; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/artifacts/robotic-arm-2#artifact> rdf:type ns1:Artifact ;&#10;ns1:isHostedOn &#60;https://ns.inria.fr/hmas/#platformplatform> .</code></pre>|

***
### CannotTell Assertion number 5

[Jump to summary definition](#summary-CannotTell-5)

:warning:CannotTell assertion
#### Subject detail
|Name|manufacturing|
|----|----|
|Title|Standalone use case use-cases/manufacturing/dataset-v1.ttl from branch 182-uc-manufacturing|
|Composition|- [Use case manufacturing/dataset-v1.ttl](https://github.com/HyperAgents/hmas/blob/182-uc-manufacturing/use-cases/manufacturing/dataset-v1.ttl)|

#### Criterion detail
|Identifier|[prefix-validity](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#prefix-validity)|
|----|----|
|Title|Term validity test|
|Description|A test case checking if all the prefixes are not too close from the most used existing namespaces (according to prefix cc)|

#### Outcome Detail
|Type|:warning:CannotTell|
|----|----|
|Title|Possible prefix typo|
|Description|The prefix http://www.w3.org/2011/http# seems suspicious. Did you mean one of these prefixes?|
|Pointer|<pre lang="Turtle"><code>Prefix usage in the subject file:&#10;@prefix owl: &#60;http://www.w3.org/2002/07/owl#> .&#10;@prefix xsh: &#60;http://www.w3.org/ns/shacl#> .&#10;@prefix sh: &#60;http://www.w3.org/ns/shacl#> .&#10;@prefix rdf: &#60;http://www.w3.org/1999/02/22-rdf-syntax-ns#> .&#10;&lowbar;:b4136 rdf:first &#60;http://www.w3.org/2011/http#headers> .&#10;&lowbar;:b4141 sh:path &#60;http://www.w3.org/2011/http#fieldValue> .&#10;&lowbar;:b4140 sh:path &#60;http://www.w3.org/2011/http#fieldName> .&#10;&lowbar;:b4139 sh:class &#60;http://www.w3.org/2011/http#MessageHeader> .</code></pre>|
|Pointer|<pre lang="Turtle"><code>Common prefix found&#10;@prefix httpvoc: &#60;http://www.w3.org/2006/http#> .</code></pre>|

***
### CannotTell Assertion number 6

[Jump to summary definition](#summary-CannotTell-6)

:warning:CannotTell assertion
#### Subject detail
|Name|manufacturing|
|----|----|
|Title|Standalone use case use-cases/manufacturing/dataset-v1.ttl from branch 182-uc-manufacturing|
|Composition|- [Use case manufacturing/dataset-v1.ttl](https://github.com/HyperAgents/hmas/blob/182-uc-manufacturing/use-cases/manufacturing/dataset-v1.ttl)|

#### Criterion detail
|Identifier|[prefix-validity](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#prefix-validity)|
|----|----|
|Title|Term validity test|
|Description|A test case checking if all the prefixes are not too close from the most used existing namespaces (according to prefix cc)|

#### Outcome Detail
|Type|:warning:CannotTell|
|----|----|
|Title|Possible prefix typo|
|Description|The prefix https://api.interactions.ics.unisg.ch/cherrybot1/operator/ seems suspicious. Did you mean one of these prefixes?|
|Pointer|<pre lang="Turtle"><code>Prefix usage in the subject file:&#10;@prefix owl: &#60;http://www.w3.org/2002/07/owl#> .&#10;@prefix xsh: &#60;http://www.w3.org/ns/shacl#> .&#10;@prefix sh: &#60;http://www.w3.org/ns/shacl#> .&#10;&lowbar;:b4287 sh:hasValue &#60;https://api.interactions.ics.unisg.ch/cherrybot1/operator/%7Btoken%7D> .</code></pre>|
|Pointer|<pre lang="Turtle"><code>Similar prefix found in file .\use-cases\manufacturing\dataset-v1.ttl&#10;Prefix found: https://api.interactions.ics.unisg.ch/cherrybot2/operator/&#10;@prefix owl: &#60;http://www.w3.org/2002/07/owl#> .&#10;@prefix xsh: &#60;http://www.w3.org/ns/shacl#> .&#10;@prefix sh: &#60;http://www.w3.org/ns/shacl#> .&#10;&lowbar;:b5674 sh:hasValue &#60;https://api.interactions.ics.unisg.ch/cherrybot2/operator/%7Btoken%7D> .</code></pre>|

***
### CannotTell Assertion number 7

[Jump to summary definition](#summary-CannotTell-7)

:warning:CannotTell assertion
#### Subject detail
|Name|manufacturing|
|----|----|
|Title|Standalone use case use-cases/manufacturing/dataset-v1.ttl from branch 182-uc-manufacturing|
|Composition|- [Use case manufacturing/dataset-v1.ttl](https://github.com/HyperAgents/hmas/blob/182-uc-manufacturing/use-cases/manufacturing/dataset-v1.ttl)|

#### Criterion detail
|Identifier|[prefix-validity](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#prefix-validity)|
|----|----|
|Title|Term validity test|
|Description|A test case checking if all the prefixes are not too close from the most used existing namespaces (according to prefix cc)|

#### Outcome Detail
|Type|:warning:CannotTell|
|----|----|
|Title|Possible prefix typo|
|Description|The prefix https://ns.inria.fr/hmas/workspaces/cup-production-site/agents/agent-c# seems suspicious. Did you mean one of these prefixes?|
|Pointer|<pre lang="Turtle"><code>Prefix usage in the subject file:&#10;@prefix owl: &#60;http://www.w3.org/2002/07/owl#> .&#10;@prefix ns1: &#60;https://purl.org/hmas/> .&#10;@prefix rdf: &#60;http://www.w3.org/1999/02/22-rdf-syntax-ns#> . &#10; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/agents/agent-c#agent> rdf:type &#60;https://purl.org/hmas/Agent> ;&#10;ns1:hasProfile &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/agents/agent-c#> ;&#10;ns1:isContainedIn &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site#Workspace> ;&#10;ns1:isHostedOn &#60;https://ns.inria.fr/hmas/#platformplatform> .</code></pre>|
|Pointer|<pre lang="Turtle"><code>Similar prefix found in file .\use-cases\manufacturing\dataset-v1.ttl&#10;Prefix found: https://ns.inria.fr/hmas/workspaces/cup-production-site/agents/agent-d#&#10;@prefix owl: &#60;http://www.w3.org/2002/07/owl#> .&#10;@prefix ns1: &#60;https://purl.org/hmas/> .&#10;@prefix rdf: &#60;http://www.w3.org/1999/02/22-rdf-syntax-ns#> . &#10; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/agents/agent-d#agent> rdf:type &#60;https://purl.org/hmas/Agent> ;&#10;ns1:hasProfile &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/agents/agent-d#> ;&#10;ns1:isContainedIn &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site#Workspace> ;&#10;ns1:isHostedOn &#60;https://ns.inria.fr/hmas/#platformplatform> .</code></pre>|

***
### CannotTell Assertion number 8

[Jump to summary definition](#summary-CannotTell-8)

:warning:CannotTell assertion
#### Subject detail
|Name|manufacturing|
|----|----|
|Title|Standalone use case use-cases/manufacturing/dataset-v1.ttl from branch 182-uc-manufacturing|
|Composition|- [Use case manufacturing/dataset-v1.ttl](https://github.com/HyperAgents/hmas/blob/182-uc-manufacturing/use-cases/manufacturing/dataset-v1.ttl)|

#### Criterion detail
|Identifier|[prefix-validity](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#prefix-validity)|
|----|----|
|Title|Term validity test|
|Description|A test case checking if all the prefixes are not too close from the most used existing namespaces (according to prefix cc)|

#### Outcome Detail
|Type|:warning:CannotTell|
|----|----|
|Title|Possible prefix typo|
|Description|The prefix https://ns.inria.fr/hmas/workspaces/cup-production-site/agents/agent-b# seems suspicious. Did you mean one of these prefixes?|
|Pointer|<pre lang="Turtle"><code>Prefix usage in the subject file:&#10;@prefix owl: &#60;http://www.w3.org/2002/07/owl#> .&#10;@prefix ns1: &#60;https://purl.org/hmas/> .&#10;@prefix rdf: &#60;http://www.w3.org/1999/02/22-rdf-syntax-ns#> . &#10; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/agents/agent-b#agent> rdf:type &#60;https://purl.org/hmas/Agent> ;&#10;ns1:hasProfile &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/agents/agent-b#> ;&#10;ns1:isContainedIn &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site#Workspace> ;&#10;ns1:isHostedOn &#60;https://ns.inria.fr/hmas/#platformplatform> .</code></pre>|
|Pointer|<pre lang="Turtle"><code>Similar prefix found in file .\use-cases\manufacturing\dataset-v1.ttl&#10;Prefix found: https://ns.inria.fr/hmas/workspaces/cup-production-site/agents/agent-c#&#10;@prefix owl: &#60;http://www.w3.org/2002/07/owl#> .&#10;@prefix ns1: &#60;https://purl.org/hmas/> .&#10;@prefix rdf: &#60;http://www.w3.org/1999/02/22-rdf-syntax-ns#> . &#10; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/agents/agent-c#agent> rdf:type &#60;https://purl.org/hmas/Agent> ;&#10;ns1:hasProfile &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/agents/agent-c#> ;&#10;ns1:isContainedIn &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site#Workspace> ;&#10;ns1:isHostedOn &#60;https://ns.inria.fr/hmas/#platformplatform> .</code></pre>|
|Pointer|<pre lang="Turtle"><code>Similar prefix found in file .\use-cases\manufacturing\dataset-v1.ttl&#10;Prefix found: https://ns.inria.fr/hmas/workspaces/cup-production-site/agents/agent-d#&#10;@prefix owl: &#60;http://www.w3.org/2002/07/owl#> .&#10;@prefix ns1: &#60;https://purl.org/hmas/> .&#10;@prefix rdf: &#60;http://www.w3.org/1999/02/22-rdf-syntax-ns#> . &#10; &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/agents/agent-d#agent> rdf:type &#60;https://purl.org/hmas/Agent> ;&#10;ns1:hasProfile &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site/agents/agent-d#> ;&#10;ns1:isContainedIn &#60;https://ns.inria.fr/hmas/workspaces/cup-production-site#Workspace> ;&#10;ns1:isHostedOn &#60;https://ns.inria.fr/hmas/#platformplatform> .</code></pre>|

***
### CannotTell Assertion number 9

[Jump to summary definition](#summary-CannotTell-9)

:warning:CannotTell assertion
#### Subject detail
|Name|manufacturing|
|----|----|
|Title|Standalone use case use-cases/manufacturing/dataset-v1.ttl from branch 182-uc-manufacturing|
|Composition|- [Use case manufacturing/dataset-v1.ttl](https://github.com/HyperAgents/hmas/blob/182-uc-manufacturing/use-cases/manufacturing/dataset-v1.ttl)|

#### Criterion detail
|Identifier|[prefix-validity](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#prefix-validity)|
|----|----|
|Title|Term validity test|
|Description|A test case checking if all the prefixes are not too close from the most used existing namespaces (according to prefix cc)|

#### Outcome Detail
|Type|:warning:CannotTell|
|----|----|
|Title|Possible prefix typo|
|Description|The prefix https://api.interactions.ics.unisg.ch/cherrybot1/tcp/ seems suspicious. Did you mean one of these prefixes?|
|Pointer|<pre lang="Turtle"><code>Prefix usage in the subject file:&#10;@prefix owl: &#60;http://www.w3.org/2002/07/owl#> .&#10;@prefix xsh: &#60;http://www.w3.org/ns/shacl#> .&#10;@prefix sh: &#60;http://www.w3.org/ns/shacl#> .&#10;&lowbar;:b4278 sh:hasValue &#60;https://api.interactions.ics.unisg.ch/cherrybot1/tcp/target> .&#10;&lowbar;:b4260 sh:hasValue &#60;https://api.interactions.ics.unisg.ch/cherrybot1/tcp/target> .</code></pre>|
|Pointer|<pre lang="Turtle"><code>Similar prefix found in file .\use-cases\manufacturing\dataset-v1.ttl&#10;Prefix found: https://api.interactions.ics.unisg.ch/cherrybot2/tcp/&#10;@prefix owl: &#60;http://www.w3.org/2002/07/owl#> .&#10;@prefix xsh: &#60;http://www.w3.org/ns/shacl#> .&#10;@prefix sh: &#60;http://www.w3.org/ns/shacl#> .&#10;&lowbar;:b6590 sh:hasValue &#60;https://api.interactions.ics.unisg.ch/cherrybot2/tcp/target> .&#10;&lowbar;:b6608 sh:hasValue &#60;https://api.interactions.ics.unisg.ch/cherrybot2/tcp/target> .</code></pre>|

***

</details>

***


# NotTested Assertions

Here is the chapter related to the NotTested assertion

:grey_question:2 NotTested assertions

<details>
<summary>Fold/Unfold the 2 summary and details</summary>

## NotTested Assertions Summary

[Jump to statistic summary](#statistic-summary)

:grey_question:2 NotTested assertions

|*Jump*|*Number*|*Status*|*Subject*|*Criterion*|*Title*|*Link*|
|------|--------|--------|---------|-----------|-------|------|
|[Table top](#nottested-assertions-summary)|<div id="summary-NotTested-1">1/2</div>|:grey_question:*NotTested*|`manufacturing-environments-safety-rules`|[owl-rl-constraint](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#owl-rl-constraint)|The test could not be run|[Jump](#nottested-assertion-number-1)|
|[Table top](#nottested-assertions-summary)|<div id="summary-NotTested-2">2/2</div>|:grey_question:*NotTested*|`manufacturing-environments-safety-rules`|[term-recognition](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#term-recognition)|The test could not be run|[Jump](#nottested-assertion-number-2)|

***

## NotTested Assertion Details

This subchapter gives more details to the :grey_question:NotTested assertions

### NotTested Assertion number 1

[Jump to summary definition](#summary-NotTested-1)

:grey_question:NotTested assertion
#### Subject detail
|Name|manufacturing-environments-safety-rules|
|----|----|
|Title|Standalone dataset domains/manufacturing-environments/safety-rules/dataset.ttl from branch 182-uc-manufacturing|
|Composition|- [Dataset manufacturing-environments/safety-rules/dataset.ttl](https://github.com/HyperAgents/hmas/blob/182-uc-manufacturing/domains/manufacturing-environments/safety-rules/dataset.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#owl-rl-constraint)|
|----|----|
|Title|OWL RL Constraint test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:grey_question:NotTested|
|----|----|
|Title|The test could not be run|
|Description|The subject and its recursive imports must be syntaxically correct|

***
### NotTested Assertion number 2

[Jump to summary definition](#summary-NotTested-2)

:grey_question:NotTested assertion
#### Subject detail
|Name|manufacturing-environments-safety-rules|
|----|----|
|Title|Standalone dataset domains/manufacturing-environments/safety-rules/dataset.ttl from branch 182-uc-manufacturing|
|Composition|- [Dataset manufacturing-environments/safety-rules/dataset.ttl](https://github.com/HyperAgents/hmas/blob/182-uc-manufacturing/domains/manufacturing-environments/safety-rules/dataset.ttl)|

#### Criterion detail
|Identifier|[term-recognition](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#term-recognition)|
|----|----|
|Title|Term recognition test|
|Description|A test meant to detect if all the terms from the subject that are from the ontology namespace are indeed defined in the ontology|

#### Outcome Detail
|Type|:grey_question:NotTested|
|----|----|
|Title|The test could not be run|
|Description|The subject must be syntaxically correct|

***

</details>

***


# Pass Assertions

Here is the chapter related to the Pass assertion

:white_check_mark:31 Pass assertions

<details>
<summary>Fold/Unfold the 31 summary and details</summary>

## Pass Assertions Summary

[Jump to statistic summary](#statistic-summary)

:white_check_mark:31 Pass assertions

|*Jump*|*Number*|*Status*|*Subject*|*Criterion*|*Title*|*Link*|
|------|--------|--------|---------|-----------|-------|------|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-1">1/31</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-signifiers`|[owl-rl-constraint](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-assertion-number-1)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-2">2/31</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-signifiers`|[prefix-validity](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#prefix-validity)|No prefix typo|[Jump](#pass-assertion-number-2)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-3">3/31</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-signifiers`|[syntax](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#syntax)|Correct syntax|[Jump](#pass-assertion-number-3)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-4">4/31</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-signifiers`|[term-recognition](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#term-recognition)|Every term exists|[Jump](#pass-assertion-number-4)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-5">5/31</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-platforms`|[owl-rl-constraint](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-assertion-number-5)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-6">6/31</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-platforms`|[prefix-validity](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#prefix-validity)|No prefix typo|[Jump](#pass-assertion-number-6)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-7">7/31</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-platforms`|[syntax](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#syntax)|Correct syntax|[Jump](#pass-assertion-number-7)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-8">8/31</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-organization`|[owl-rl-constraint](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-assertion-number-8)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-9">9/31</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-organization`|[prefix-validity](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#prefix-validity)|No prefix typo|[Jump](#pass-assertion-number-9)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-10">10/31</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-organization`|[syntax](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#syntax)|Correct syntax|[Jump](#pass-assertion-number-10)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-11">11/31</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-organization`|[term-recognition](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#term-recognition)|Every term exists|[Jump](#pass-assertion-number-11)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-12">12/31</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-core`|[owl-rl-constraint](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-assertion-number-12)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-13">13/31</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-core`|[prefix-validity](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#prefix-validity)|No prefix typo|[Jump](#pass-assertion-number-13)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-14">14/31</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-core`|[syntax](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#syntax)|Correct syntax|[Jump](#pass-assertion-number-14)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-15">15/31</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-core`|[term-recognition](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#term-recognition)|Every term exists|[Jump](#pass-assertion-number-15)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-16">16/31</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-behavior-specifications`|[owl-rl-constraint](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-assertion-number-16)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-17">17/31</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-behavior-specifications`|[syntax](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#syntax)|Correct syntax|[Jump](#pass-assertion-number-17)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-18">18/31</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-behavior-specifications`|[term-recognition](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#term-recognition)|Every term exists|[Jump](#pass-assertion-number-18)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-19">19/31</div>|:white_check_mark:*Pass*|`manufacturing`|[owl-rl-constraint](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-assertion-number-19)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-20">20/31</div>|:white_check_mark:*Pass*|`manufacturing`|[syntax](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#syntax)|Correct syntax|[Jump](#pass-assertion-number-20)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-21">21/31</div>|:white_check_mark:*Pass*|`logistics-structure-organization`|[owl-rl-constraint](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-assertion-number-21)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-22">22/31</div>|:white_check_mark:*Pass*|`logistics-structure-organization`|[prefix-validity](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#prefix-validity)|No prefix typo|[Jump](#pass-assertion-number-22)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-23">23/31</div>|:white_check_mark:*Pass*|`logistics-structure-organization`|[syntax](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#syntax)|Correct syntax|[Jump](#pass-assertion-number-23)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-24">24/31</div>|:white_check_mark:*Pass*|`logistics-create-organization`|[owl-rl-constraint](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-assertion-number-24)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-25">25/31</div>|:white_check_mark:*Pass*|`logistics-create-organization`|[prefix-validity](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#prefix-validity)|No prefix typo|[Jump](#pass-assertion-number-25)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-26">26/31</div>|:white_check_mark:*Pass*|`logistics-create-organization`|[syntax](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#syntax)|Correct syntax|[Jump](#pass-assertion-number-26)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-27">27/31</div>|:white_check_mark:*Pass*|`logistics-create-organization`|[term-recognition](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#term-recognition)|Every term exists|[Jump](#pass-assertion-number-27)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-28">28/31</div>|:white_check_mark:*Pass*|`domain-template-scenario-template`|[owl-rl-constraint](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-assertion-number-28)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-29">29/31</div>|:white_check_mark:*Pass*|`domain-template-scenario-template`|[prefix-validity](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#prefix-validity)|No prefix typo|[Jump](#pass-assertion-number-29)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-30">30/31</div>|:white_check_mark:*Pass*|`domain-template-scenario-template`|[syntax](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#syntax)|Correct syntax|[Jump](#pass-assertion-number-30)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-31">31/31</div>|:white_check_mark:*Pass*|`domain-template-scenario-template`|[term-recognition](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#term-recognition)|Every term exists|[Jump](#pass-assertion-number-31)|

***

## Pass Assertion Details

This subchapter gives more details to the :white_check_mark:Pass assertions

### Pass Assertion number 1

[Jump to summary definition](#summary-Pass-1)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-signifiers|
|----|----|
|Title|Standalone dataset domains/manufacturing-environments/discover-signifiers/dataset.ttl from branch 182-uc-manufacturing|
|Composition|- [Dataset manufacturing-environments/discover-signifiers/dataset.ttl](https://github.com/HyperAgents/hmas/blob/182-uc-manufacturing/domains/manufacturing-environments/discover-signifiers/dataset.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#owl-rl-constraint)|
|----|----|
|Title|OWL RL Constraint test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL RL consistent|
|Description|The provided graph is consistent for any OWL RL constraint|

***
### Pass Assertion number 2

[Jump to summary definition](#summary-Pass-2)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-signifiers|
|----|----|
|Title|Standalone dataset domains/manufacturing-environments/discover-signifiers/dataset.ttl from branch 182-uc-manufacturing|
|Composition|- [Dataset manufacturing-environments/discover-signifiers/dataset.ttl](https://github.com/HyperAgents/hmas/blob/182-uc-manufacturing/domains/manufacturing-environments/discover-signifiers/dataset.ttl)|

#### Criterion detail
|Identifier|[prefix-validity](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#prefix-validity)|
|----|----|
|Title|Term validity test|
|Description|A test case checking if all the prefixes are not too close from the most used existing namespaces (according to prefix cc)|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|No prefix typo|
|Description|It seems that none of the subject URIs have prefixes typos|

***
### Pass Assertion number 3

[Jump to summary definition](#summary-Pass-3)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-signifiers|
|----|----|
|Title|Standalone dataset domains/manufacturing-environments/discover-signifiers/dataset.ttl from branch 182-uc-manufacturing|
|Composition|- [Dataset manufacturing-environments/discover-signifiers/dataset.ttl](https://github.com/HyperAgents/hmas/blob/182-uc-manufacturing/domains/manufacturing-environments/discover-signifiers/dataset.ttl)|

#### Criterion detail
|Identifier|[syntax](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#syntax)|
|----|----|
|Title|Syntax test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Correct syntax|
|Description|Test subject has a correct syntax|

***
### Pass Assertion number 4

[Jump to summary definition](#summary-Pass-4)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-signifiers|
|----|----|
|Title|Standalone dataset domains/manufacturing-environments/discover-signifiers/dataset.ttl from branch 182-uc-manufacturing|
|Composition|- [Dataset manufacturing-environments/discover-signifiers/dataset.ttl](https://github.com/HyperAgents/hmas/blob/182-uc-manufacturing/domains/manufacturing-environments/discover-signifiers/dataset.ttl)|

#### Criterion detail
|Identifier|[term-recognition](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#term-recognition)|
|----|----|
|Title|Term recognition test|
|Description|A test meant to detect if all the terms from the subject that are from the ontology namespace are indeed defined in the ontology|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Every term exists|
|Description|All the ontologic terms in the subject are defined in the ontology|

***
### Pass Assertion number 5

[Jump to summary definition](#summary-Pass-5)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-platforms|
|----|----|
|Title|Standalone dataset domains/manufacturing-environments/discover-platforms/dataset.ttl from branch 182-uc-manufacturing|
|Composition|- [Dataset manufacturing-environments/discover-platforms/dataset.ttl](https://github.com/HyperAgents/hmas/blob/182-uc-manufacturing/domains/manufacturing-environments/discover-platforms/dataset.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#owl-rl-constraint)|
|----|----|
|Title|OWL RL Constraint test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL RL consistent|
|Description|The provided graph is consistent for any OWL RL constraint|

***
### Pass Assertion number 6

[Jump to summary definition](#summary-Pass-6)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-platforms|
|----|----|
|Title|Standalone dataset domains/manufacturing-environments/discover-platforms/dataset.ttl from branch 182-uc-manufacturing|
|Composition|- [Dataset manufacturing-environments/discover-platforms/dataset.ttl](https://github.com/HyperAgents/hmas/blob/182-uc-manufacturing/domains/manufacturing-environments/discover-platforms/dataset.ttl)|

#### Criterion detail
|Identifier|[prefix-validity](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#prefix-validity)|
|----|----|
|Title|Term validity test|
|Description|A test case checking if all the prefixes are not too close from the most used existing namespaces (according to prefix cc)|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|No prefix typo|
|Description|It seems that none of the subject URIs have prefixes typos|

***
### Pass Assertion number 7

[Jump to summary definition](#summary-Pass-7)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-platforms|
|----|----|
|Title|Standalone dataset domains/manufacturing-environments/discover-platforms/dataset.ttl from branch 182-uc-manufacturing|
|Composition|- [Dataset manufacturing-environments/discover-platforms/dataset.ttl](https://github.com/HyperAgents/hmas/blob/182-uc-manufacturing/domains/manufacturing-environments/discover-platforms/dataset.ttl)|

#### Criterion detail
|Identifier|[syntax](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#syntax)|
|----|----|
|Title|Syntax test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Correct syntax|
|Description|Test subject has a correct syntax|

***
### Pass Assertion number 8

[Jump to summary definition](#summary-Pass-8)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-organization|
|----|----|
|Title|Standalone dataset domains/manufacturing-environments/discover-organization/dataset.ttl from branch 182-uc-manufacturing|
|Composition|- [Dataset manufacturing-environments/discover-organization/dataset.ttl](https://github.com/HyperAgents/hmas/blob/182-uc-manufacturing/domains/manufacturing-environments/discover-organization/dataset.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#owl-rl-constraint)|
|----|----|
|Title|OWL RL Constraint test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL RL consistent|
|Description|The provided graph is consistent for any OWL RL constraint|

***
### Pass Assertion number 9

[Jump to summary definition](#summary-Pass-9)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-organization|
|----|----|
|Title|Standalone dataset domains/manufacturing-environments/discover-organization/dataset.ttl from branch 182-uc-manufacturing|
|Composition|- [Dataset manufacturing-environments/discover-organization/dataset.ttl](https://github.com/HyperAgents/hmas/blob/182-uc-manufacturing/domains/manufacturing-environments/discover-organization/dataset.ttl)|

#### Criterion detail
|Identifier|[prefix-validity](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#prefix-validity)|
|----|----|
|Title|Term validity test|
|Description|A test case checking if all the prefixes are not too close from the most used existing namespaces (according to prefix cc)|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|No prefix typo|
|Description|It seems that none of the subject URIs have prefixes typos|

***
### Pass Assertion number 10

[Jump to summary definition](#summary-Pass-10)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-organization|
|----|----|
|Title|Standalone dataset domains/manufacturing-environments/discover-organization/dataset.ttl from branch 182-uc-manufacturing|
|Composition|- [Dataset manufacturing-environments/discover-organization/dataset.ttl](https://github.com/HyperAgents/hmas/blob/182-uc-manufacturing/domains/manufacturing-environments/discover-organization/dataset.ttl)|

#### Criterion detail
|Identifier|[syntax](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#syntax)|
|----|----|
|Title|Syntax test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Correct syntax|
|Description|Test subject has a correct syntax|

***
### Pass Assertion number 11

[Jump to summary definition](#summary-Pass-11)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-organization|
|----|----|
|Title|Standalone dataset domains/manufacturing-environments/discover-organization/dataset.ttl from branch 182-uc-manufacturing|
|Composition|- [Dataset manufacturing-environments/discover-organization/dataset.ttl](https://github.com/HyperAgents/hmas/blob/182-uc-manufacturing/domains/manufacturing-environments/discover-organization/dataset.ttl)|

#### Criterion detail
|Identifier|[term-recognition](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#term-recognition)|
|----|----|
|Title|Term recognition test|
|Description|A test meant to detect if all the terms from the subject that are from the ontology namespace are indeed defined in the ontology|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Every term exists|
|Description|All the ontologic terms in the subject are defined in the ontology|

***
### Pass Assertion number 12

[Jump to summary definition](#summary-Pass-12)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-core|
|----|----|
|Title|Standalone dataset domains/manufacturing-environments/discover-core/dataset.ttl from branch 182-uc-manufacturing|
|Composition|- [Dataset manufacturing-environments/discover-core/dataset.ttl](https://github.com/HyperAgents/hmas/blob/182-uc-manufacturing/domains/manufacturing-environments/discover-core/dataset.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#owl-rl-constraint)|
|----|----|
|Title|OWL RL Constraint test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL RL consistent|
|Description|The provided graph is consistent for any OWL RL constraint|

***
### Pass Assertion number 13

[Jump to summary definition](#summary-Pass-13)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-core|
|----|----|
|Title|Standalone dataset domains/manufacturing-environments/discover-core/dataset.ttl from branch 182-uc-manufacturing|
|Composition|- [Dataset manufacturing-environments/discover-core/dataset.ttl](https://github.com/HyperAgents/hmas/blob/182-uc-manufacturing/domains/manufacturing-environments/discover-core/dataset.ttl)|

#### Criterion detail
|Identifier|[prefix-validity](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#prefix-validity)|
|----|----|
|Title|Term validity test|
|Description|A test case checking if all the prefixes are not too close from the most used existing namespaces (according to prefix cc)|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|No prefix typo|
|Description|It seems that none of the subject URIs have prefixes typos|

***
### Pass Assertion number 14

[Jump to summary definition](#summary-Pass-14)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-core|
|----|----|
|Title|Standalone dataset domains/manufacturing-environments/discover-core/dataset.ttl from branch 182-uc-manufacturing|
|Composition|- [Dataset manufacturing-environments/discover-core/dataset.ttl](https://github.com/HyperAgents/hmas/blob/182-uc-manufacturing/domains/manufacturing-environments/discover-core/dataset.ttl)|

#### Criterion detail
|Identifier|[syntax](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#syntax)|
|----|----|
|Title|Syntax test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Correct syntax|
|Description|Test subject has a correct syntax|

***
### Pass Assertion number 15

[Jump to summary definition](#summary-Pass-15)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-core|
|----|----|
|Title|Standalone dataset domains/manufacturing-environments/discover-core/dataset.ttl from branch 182-uc-manufacturing|
|Composition|- [Dataset manufacturing-environments/discover-core/dataset.ttl](https://github.com/HyperAgents/hmas/blob/182-uc-manufacturing/domains/manufacturing-environments/discover-core/dataset.ttl)|

#### Criterion detail
|Identifier|[term-recognition](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#term-recognition)|
|----|----|
|Title|Term recognition test|
|Description|A test meant to detect if all the terms from the subject that are from the ontology namespace are indeed defined in the ontology|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Every term exists|
|Description|All the ontologic terms in the subject are defined in the ontology|

***
### Pass Assertion number 16

[Jump to summary definition](#summary-Pass-16)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Standalone dataset domains/manufacturing-environments/discover-behavior-specifications/dataset.ttl from branch 182-uc-manufacturing|
|Composition|- [Dataset manufacturing-environments/discover-behavior-specifications/dataset.ttl](https://github.com/HyperAgents/hmas/blob/182-uc-manufacturing/domains/manufacturing-environments/discover-behavior-specifications/dataset.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#owl-rl-constraint)|
|----|----|
|Title|OWL RL Constraint test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL RL consistent|
|Description|The provided graph is consistent for any OWL RL constraint|

***
### Pass Assertion number 17

[Jump to summary definition](#summary-Pass-17)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Standalone dataset domains/manufacturing-environments/discover-behavior-specifications/dataset.ttl from branch 182-uc-manufacturing|
|Composition|- [Dataset manufacturing-environments/discover-behavior-specifications/dataset.ttl](https://github.com/HyperAgents/hmas/blob/182-uc-manufacturing/domains/manufacturing-environments/discover-behavior-specifications/dataset.ttl)|

#### Criterion detail
|Identifier|[syntax](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#syntax)|
|----|----|
|Title|Syntax test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Correct syntax|
|Description|Test subject has a correct syntax|

***
### Pass Assertion number 18

[Jump to summary definition](#summary-Pass-18)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Standalone dataset domains/manufacturing-environments/discover-behavior-specifications/dataset.ttl from branch 182-uc-manufacturing|
|Composition|- [Dataset manufacturing-environments/discover-behavior-specifications/dataset.ttl](https://github.com/HyperAgents/hmas/blob/182-uc-manufacturing/domains/manufacturing-environments/discover-behavior-specifications/dataset.ttl)|

#### Criterion detail
|Identifier|[term-recognition](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#term-recognition)|
|----|----|
|Title|Term recognition test|
|Description|A test meant to detect if all the terms from the subject that are from the ontology namespace are indeed defined in the ontology|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Every term exists|
|Description|All the ontologic terms in the subject are defined in the ontology|

***
### Pass Assertion number 19

[Jump to summary definition](#summary-Pass-19)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing|
|----|----|
|Title|Standalone use case use-cases/manufacturing/dataset-v1.ttl from branch 182-uc-manufacturing|
|Composition|- [Use case manufacturing/dataset-v1.ttl](https://github.com/HyperAgents/hmas/blob/182-uc-manufacturing/use-cases/manufacturing/dataset-v1.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#owl-rl-constraint)|
|----|----|
|Title|OWL RL Constraint test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL RL consistent|
|Description|The provided graph is consistent for any OWL RL constraint|

***
### Pass Assertion number 20

[Jump to summary definition](#summary-Pass-20)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing|
|----|----|
|Title|Standalone use case use-cases/manufacturing/dataset-v1.ttl from branch 182-uc-manufacturing|
|Composition|- [Use case manufacturing/dataset-v1.ttl](https://github.com/HyperAgents/hmas/blob/182-uc-manufacturing/use-cases/manufacturing/dataset-v1.ttl)|

#### Criterion detail
|Identifier|[syntax](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#syntax)|
|----|----|
|Title|Syntax test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Correct syntax|
|Description|Test subject has a correct syntax|

***
### Pass Assertion number 21

[Jump to summary definition](#summary-Pass-21)

:white_check_mark:Pass assertion
#### Subject detail
|Name|logistics-structure-organization|
|----|----|
|Title|Standalone dataset domains/logistics/structure-organization/dataset.ttl from branch 182-uc-manufacturing|
|Composition|- [Dataset logistics/structure-organization/dataset.ttl](https://github.com/HyperAgents/hmas/blob/182-uc-manufacturing/domains/logistics/structure-organization/dataset.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#owl-rl-constraint)|
|----|----|
|Title|OWL RL Constraint test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL RL consistent|
|Description|The provided graph is consistent for any OWL RL constraint|

***
### Pass Assertion number 22

[Jump to summary definition](#summary-Pass-22)

:white_check_mark:Pass assertion
#### Subject detail
|Name|logistics-structure-organization|
|----|----|
|Title|Standalone dataset domains/logistics/structure-organization/dataset.ttl from branch 182-uc-manufacturing|
|Composition|- [Dataset logistics/structure-organization/dataset.ttl](https://github.com/HyperAgents/hmas/blob/182-uc-manufacturing/domains/logistics/structure-organization/dataset.ttl)|

#### Criterion detail
|Identifier|[prefix-validity](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#prefix-validity)|
|----|----|
|Title|Term validity test|
|Description|A test case checking if all the prefixes are not too close from the most used existing namespaces (according to prefix cc)|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|No prefix typo|
|Description|It seems that none of the subject URIs have prefixes typos|

***
### Pass Assertion number 23

[Jump to summary definition](#summary-Pass-23)

:white_check_mark:Pass assertion
#### Subject detail
|Name|logistics-structure-organization|
|----|----|
|Title|Standalone dataset domains/logistics/structure-organization/dataset.ttl from branch 182-uc-manufacturing|
|Composition|- [Dataset logistics/structure-organization/dataset.ttl](https://github.com/HyperAgents/hmas/blob/182-uc-manufacturing/domains/logistics/structure-organization/dataset.ttl)|

#### Criterion detail
|Identifier|[syntax](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#syntax)|
|----|----|
|Title|Syntax test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Correct syntax|
|Description|Test subject has a correct syntax|

***
### Pass Assertion number 24

[Jump to summary definition](#summary-Pass-24)

:white_check_mark:Pass assertion
#### Subject detail
|Name|logistics-create-organization|
|----|----|
|Title|Standalone dataset domains/logistics/create-organization/dataset.ttl from branch 182-uc-manufacturing|
|Composition|- [Dataset logistics/create-organization/dataset.ttl](https://github.com/HyperAgents/hmas/blob/182-uc-manufacturing/domains/logistics/create-organization/dataset.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#owl-rl-constraint)|
|----|----|
|Title|OWL RL Constraint test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL RL consistent|
|Description|The provided graph is consistent for any OWL RL constraint|

***
### Pass Assertion number 25

[Jump to summary definition](#summary-Pass-25)

:white_check_mark:Pass assertion
#### Subject detail
|Name|logistics-create-organization|
|----|----|
|Title|Standalone dataset domains/logistics/create-organization/dataset.ttl from branch 182-uc-manufacturing|
|Composition|- [Dataset logistics/create-organization/dataset.ttl](https://github.com/HyperAgents/hmas/blob/182-uc-manufacturing/domains/logistics/create-organization/dataset.ttl)|

#### Criterion detail
|Identifier|[prefix-validity](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#prefix-validity)|
|----|----|
|Title|Term validity test|
|Description|A test case checking if all the prefixes are not too close from the most used existing namespaces (according to prefix cc)|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|No prefix typo|
|Description|It seems that none of the subject URIs have prefixes typos|

***
### Pass Assertion number 26

[Jump to summary definition](#summary-Pass-26)

:white_check_mark:Pass assertion
#### Subject detail
|Name|logistics-create-organization|
|----|----|
|Title|Standalone dataset domains/logistics/create-organization/dataset.ttl from branch 182-uc-manufacturing|
|Composition|- [Dataset logistics/create-organization/dataset.ttl](https://github.com/HyperAgents/hmas/blob/182-uc-manufacturing/domains/logistics/create-organization/dataset.ttl)|

#### Criterion detail
|Identifier|[syntax](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#syntax)|
|----|----|
|Title|Syntax test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Correct syntax|
|Description|Test subject has a correct syntax|

***
### Pass Assertion number 27

[Jump to summary definition](#summary-Pass-27)

:white_check_mark:Pass assertion
#### Subject detail
|Name|logistics-create-organization|
|----|----|
|Title|Standalone dataset domains/logistics/create-organization/dataset.ttl from branch 182-uc-manufacturing|
|Composition|- [Dataset logistics/create-organization/dataset.ttl](https://github.com/HyperAgents/hmas/blob/182-uc-manufacturing/domains/logistics/create-organization/dataset.ttl)|

#### Criterion detail
|Identifier|[term-recognition](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#term-recognition)|
|----|----|
|Title|Term recognition test|
|Description|A test meant to detect if all the terms from the subject that are from the ontology namespace are indeed defined in the ontology|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Every term exists|
|Description|All the ontologic terms in the subject are defined in the ontology|

***
### Pass Assertion number 28

[Jump to summary definition](#summary-Pass-28)

:white_check_mark:Pass assertion
#### Subject detail
|Name|domain-template-scenario-template|
|----|----|
|Title|Standalone dataset domains/domain-template/scenario-template/dataset.ttl from branch 182-uc-manufacturing|
|Composition|- [Dataset domain-template/scenario-template/dataset.ttl](https://github.com/HyperAgents/hmas/blob/182-uc-manufacturing/domains/domain-template/scenario-template/dataset.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#owl-rl-constraint)|
|----|----|
|Title|OWL RL Constraint test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL RL consistent|
|Description|The provided graph is consistent for any OWL RL constraint|

***
### Pass Assertion number 29

[Jump to summary definition](#summary-Pass-29)

:white_check_mark:Pass assertion
#### Subject detail
|Name|domain-template-scenario-template|
|----|----|
|Title|Standalone dataset domains/domain-template/scenario-template/dataset.ttl from branch 182-uc-manufacturing|
|Composition|- [Dataset domain-template/scenario-template/dataset.ttl](https://github.com/HyperAgents/hmas/blob/182-uc-manufacturing/domains/domain-template/scenario-template/dataset.ttl)|

#### Criterion detail
|Identifier|[prefix-validity](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#prefix-validity)|
|----|----|
|Title|Term validity test|
|Description|A test case checking if all the prefixes are not too close from the most used existing namespaces (according to prefix cc)|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|No prefix typo|
|Description|It seems that none of the subject URIs have prefixes typos|

***
### Pass Assertion number 30

[Jump to summary definition](#summary-Pass-30)

:white_check_mark:Pass assertion
#### Subject detail
|Name|domain-template-scenario-template|
|----|----|
|Title|Standalone dataset domains/domain-template/scenario-template/dataset.ttl from branch 182-uc-manufacturing|
|Composition|- [Dataset domain-template/scenario-template/dataset.ttl](https://github.com/HyperAgents/hmas/blob/182-uc-manufacturing/domains/domain-template/scenario-template/dataset.ttl)|

#### Criterion detail
|Identifier|[syntax](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#syntax)|
|----|----|
|Title|Syntax test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Correct syntax|
|Description|Test subject has a correct syntax|

***
### Pass Assertion number 31

[Jump to summary definition](#summary-Pass-31)

:white_check_mark:Pass assertion
#### Subject detail
|Name|domain-template-scenario-template|
|----|----|
|Title|Standalone dataset domains/domain-template/scenario-template/dataset.ttl from branch 182-uc-manufacturing|
|Composition|- [Dataset domain-template/scenario-template/dataset.ttl](https://github.com/HyperAgents/hmas/blob/182-uc-manufacturing/domains/domain-template/scenario-template/dataset.ttl)|

#### Criterion detail
|Identifier|[term-recognition](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/test-onto.ttl#term-recognition)|
|----|----|
|Title|Term recognition test|
|Description|A test meant to detect if all the terms from the subject that are from the ontology namespace are indeed defined in the ontology|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Every term exists|
|Description|All the ontologic terms in the subject are defined in the ontology|

***

</details>

***

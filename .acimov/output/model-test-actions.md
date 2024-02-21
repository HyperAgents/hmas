# Test Report Markdown export

This file is an export of the RDF test report made out of [EARL vocabulary](https://www.w3.org/TR/EARL10/)

This test is powered by Corese, check the [website](https://project.inria.fr/corese/) and the [repository](https://github.com/Wimmics/corese)

The original test report is available in turtle syntax [here](./actions.ttl).

# Test Context

Here is some context about under which context this test was made

|Assertor|[danaivach](https://github.com/danaivach)|
|----|-----|
|Title|danaivach using actions script|
|Description|Test triggered by [@danaivach](https://github.com/danaivach) by actions trigger|
|Script|[complete-test.py](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/complete-test.py)
|Date|2024-02-14 11:17:05|

***


# Statistic summary

Here is a short overview for this test report

290 Assertions

:boom:18 MajorFail, :exclamation:109 MinorFail, :warning:0 CannotTell, :grey_question:30 NotTested, :white_check_mark:133 Pass

<div  style="border-radius: 12px; height: 25px; overflow: hidden"><img src="../assets/red.png" width="6%" height="25px"/><img src="../assets/orange.png" width="37%" height="25px"/><img src="../assets/grey.png" width="0%" height="25px"/><img src="../assets/white.png" width="10%" height="25px"/><img src="../assets/green.png" width="47%" height="25px"/></div>

<br/>

According to the [EARL](https://www.w3.org/TR/EARL10-Schema/) vocabulary, each outcome type means:
* :x: Fail: The subject failed the test. 
* :warning: CannotTell: It is unclear if the subject passed or failed the test. This happens when an automated test requires human judgement to make a definite decision.
* :grey_question: NotTested:  The test has not been carried out. Here this is because a previous test that was mandatory to be passed did not end up as Pass.
* :white_check_mark: Pass: The subject passed the test.

***


# MajorFail Assertions

Here is the chapter related to the MajorFail assertion

:boom:18 MajorFail assertions

<details>
<summary>Fold/Unfold the 18 summary and details</summary>

## MajorFail Assertions Summary

[Jump to statistic summary](#statistic-summary)

:boom:18 MajorFail assertions

|*Jump*|*Number*|*Status*|*Subject*|*Criterion*|*Title*|*Link*|
|------|--------|--------|---------|-----------|-------|------|
|[Table top](#majorfail-assertions-summary)|<div id="summary-MajorFail-1">1/18</div>|:boom:*MajorFail*|`meta`|[syntax](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#syntax)|Test subject has syntax errors|[Jump](#majorfail-assertion-number-1)|
|[Table top](#majorfail-assertions-summary)|<div id="summary-MajorFail-2">2/18</div>|:boom:*MajorFail*|`meta`|[syntax](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#syntax)|Test subject has syntax errors|[Jump](#majorfail-assertion-number-2)|
|[Table top](#majorfail-assertions-summary)|<div id="summary-MajorFail-3">3/18</div>|:boom:*MajorFail*|`manufacturing-environments-safety-rules`|[syntax](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#syntax)|Test subject has syntax errors|[Jump](#majorfail-assertion-number-3)|
|[Table top](#majorfail-assertions-summary)|<div id="summary-MajorFail-4">4/18</div>|:boom:*MajorFail*|`fipa`|[syntax](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#syntax)|Test subject has syntax errors|[Jump](#majorfail-assertion-number-4)|
|[Table top](#majorfail-assertions-summary)|<div id="summary-MajorFail-5">5/18</div>|:boom:*MajorFail*|`fipa`|[syntax](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#syntax)|Test subject has syntax errors|[Jump](#majorfail-assertion-number-5)|
|[Table top](#majorfail-assertions-summary)|<div id="summary-MajorFail-6">6/18</div>|:boom:*MajorFail*|`fipa`|[syntax](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#syntax)|Test subject has syntax errors|[Jump](#majorfail-assertion-number-6)|
|[Table top](#majorfail-assertions-summary)|<div id="summary-MajorFail-7">7/18</div>|:boom:*MajorFail*|`fipa`|[syntax](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#syntax)|Test subject has syntax errors|[Jump](#majorfail-assertion-number-7)|
|[Table top](#majorfail-assertions-summary)|<div id="summary-MajorFail-8">8/18</div>|:boom:*MajorFail*|`fipa`|[syntax](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#syntax)|Test subject has syntax errors|[Jump](#majorfail-assertion-number-8)|
|[Table top](#majorfail-assertions-summary)|<div id="summary-MajorFail-9">9/18</div>|:boom:*MajorFail*|`fipa`|[syntax](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#syntax)|Test subject has syntax errors|[Jump](#majorfail-assertion-number-9)|
|[Table top](#majorfail-assertions-summary)|<div id="summary-MajorFail-10">10/18</div>|:boom:*MajorFail*|`fipa`|[syntax](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#syntax)|Test subject has syntax errors|[Jump](#majorfail-assertion-number-10)|
|[Table top](#majorfail-assertions-summary)|<div id="summary-MajorFail-11">11/18</div>|:boom:*MajorFail*|`fipa`|[syntax](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#syntax)|Test subject has syntax errors|[Jump](#majorfail-assertion-number-11)|
|[Table top](#majorfail-assertions-summary)|<div id="summary-MajorFail-12">12/18</div>|:boom:*MajorFail*|`fipa`|[syntax](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#syntax)|Test subject has syntax errors|[Jump](#majorfail-assertion-number-12)|
|[Table top](#majorfail-assertions-summary)|<div id="summary-MajorFail-13">13/18</div>|:boom:*MajorFail*|`fipa`|[syntax](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#syntax)|Test subject has syntax errors|[Jump](#majorfail-assertion-number-13)|
|[Table top](#majorfail-assertions-summary)|<div id="summary-MajorFail-14">14/18</div>|:boom:*MajorFail*|`fipa`|[syntax](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#syntax)|Test subject has syntax errors|[Jump](#majorfail-assertion-number-14)|
|[Table top](#majorfail-assertions-summary)|<div id="summary-MajorFail-15">15/18</div>|:boom:*MajorFail*|`fipa`|[syntax](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#syntax)|Test subject has syntax errors|[Jump](#majorfail-assertion-number-15)|
|[Table top](#majorfail-assertions-summary)|<div id="summary-MajorFail-16">16/18</div>|:boom:*MajorFail*|`fipa`|[syntax](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#syntax)|Test subject has syntax errors|[Jump](#majorfail-assertion-number-16)|
|[Table top](#majorfail-assertions-summary)|<div id="summary-MajorFail-17">17/18</div>|:boom:*MajorFail*|`fipa`|[syntax](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#syntax)|Test subject has syntax errors|[Jump](#majorfail-assertion-number-17)|
|[Table top](#majorfail-assertions-summary)|<div id="summary-MajorFail-18">18/18</div>|:boom:*MajorFail*|`fipa`|[syntax](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#syntax)|Test subject has syntax errors|[Jump](#majorfail-assertion-number-18)|

***

## MajorFail Assertion Details

This subchapter gives more details to the :boom:MajorFail assertions

### MajorFail Assertion number 1

[Jump to summary definition](#summary-MajorFail-1)

:boom:MajorFail assertion
#### Subject detail
|Name|meta|
|----|----|
|Title|Standalone module src/meta.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module meta.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/meta.ttl)|

#### Criterion detail
|Identifier|[syntax](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#syntax)|
|----|----|
|Title|Syntax test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:boom:MajorFail|
|----|----|
|Title|Test subject has syntax errors|
|Description|Undefined prefix: dcterms:source|

***
### MajorFail Assertion number 2

[Jump to summary definition](#summary-MajorFail-2)

:boom:MajorFail assertion
#### Subject detail
|Name|meta|
|----|----|
|Title|Standalone module src/meta.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module meta.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/meta.ttl)|

#### Criterion detail
|Identifier|[syntax](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#syntax)|
|----|----|
|Title|Syntax test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:boom:MajorFail|
|----|----|
|Title|Test subject has syntax errors|
|Description|Undefined prefix: doco:Glossary|

***
### MajorFail Assertion number 3

[Jump to summary definition](#summary-MajorFail-3)

:boom:MajorFail assertion
#### Subject detail
|Name|manufacturing-environments-safety-rules|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/safety-rules/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/safety-rules/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/safety-rules/onto.ttl)|

#### Criterion detail
|Identifier|[syntax](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#syntax)|
|----|----|
|Title|Syntax test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:boom:MajorFail|
|----|----|
|Title|Test subject has syntax errors|
|Description|Encountered "\"Associates exceptions to a context of application of a norm\"" at line 82, column 30.|

***
### MajorFail Assertion number 4

[Jump to summary definition](#summary-MajorFail-4)

:boom:MajorFail assertion
#### Subject detail
|Name|fipa|
|----|----|
|Title|Standalone module src/fipa.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module fipa.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/fipa.ttl)|

#### Criterion detail
|Identifier|[syntax](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#syntax)|
|----|----|
|Title|Syntax test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:boom:MajorFail|
|----|----|
|Title|Test subject has syntax errors|
|Description|Undefined prefix: hmas:ACLMessageStructure|

***
### MajorFail Assertion number 5

[Jump to summary definition](#summary-MajorFail-5)

:boom:MajorFail assertion
#### Subject detail
|Name|fipa|
|----|----|
|Title|Standalone module src/fipa.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module fipa.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/fipa.ttl)|

#### Criterion detail
|Identifier|[syntax](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#syntax)|
|----|----|
|Title|Syntax test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:boom:MajorFail|
|----|----|
|Title|Test subject has syntax errors|
|Description|Undefined prefix: hmas:ACLMessage|

***
### MajorFail Assertion number 6

[Jump to summary definition](#summary-MajorFail-6)

:boom:MajorFail assertion
#### Subject detail
|Name|fipa|
|----|----|
|Title|Standalone module src/fipa.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module fipa.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/fipa.ttl)|

#### Criterion detail
|Identifier|[syntax](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#syntax)|
|----|----|
|Title|Syntax test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:boom:MajorFail|
|----|----|
|Title|Test subject has syntax errors|
|Description|Undefined prefix: hmas:hasPerformative|

***
### MajorFail Assertion number 7

[Jump to summary definition](#summary-MajorFail-7)

:boom:MajorFail assertion
#### Subject detail
|Name|fipa|
|----|----|
|Title|Standalone module src/fipa.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module fipa.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/fipa.ttl)|

#### Criterion detail
|Identifier|[syntax](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#syntax)|
|----|----|
|Title|Syntax test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:boom:MajorFail|
|----|----|
|Title|Test subject has syntax errors|
|Description|Undefined prefix: hmas:hasSender|

***
### MajorFail Assertion number 8

[Jump to summary definition](#summary-MajorFail-8)

:boom:MajorFail assertion
#### Subject detail
|Name|fipa|
|----|----|
|Title|Standalone module src/fipa.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module fipa.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/fipa.ttl)|

#### Criterion detail
|Identifier|[syntax](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#syntax)|
|----|----|
|Title|Syntax test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:boom:MajorFail|
|----|----|
|Title|Test subject has syntax errors|
|Description|Undefined prefix: hmas:hasReceiver|

***
### MajorFail Assertion number 9

[Jump to summary definition](#summary-MajorFail-9)

:boom:MajorFail assertion
#### Subject detail
|Name|fipa|
|----|----|
|Title|Standalone module src/fipa.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module fipa.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/fipa.ttl)|

#### Criterion detail
|Identifier|[syntax](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#syntax)|
|----|----|
|Title|Syntax test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:boom:MajorFail|
|----|----|
|Title|Test subject has syntax errors|
|Description|Undefined prefix: hmas:isReplyTo|

***
### MajorFail Assertion number 10

[Jump to summary definition](#summary-MajorFail-10)

:boom:MajorFail assertion
#### Subject detail
|Name|fipa|
|----|----|
|Title|Standalone module src/fipa.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module fipa.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/fipa.ttl)|

#### Criterion detail
|Identifier|[syntax](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#syntax)|
|----|----|
|Title|Syntax test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:boom:MajorFail|
|----|----|
|Title|Test subject has syntax errors|
|Description|Undefined prefix: hmas:hasContent|

***
### MajorFail Assertion number 11

[Jump to summary definition](#summary-MajorFail-11)

:boom:MajorFail assertion
#### Subject detail
|Name|fipa|
|----|----|
|Title|Standalone module src/fipa.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module fipa.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/fipa.ttl)|

#### Criterion detail
|Identifier|[syntax](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#syntax)|
|----|----|
|Title|Syntax test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:boom:MajorFail|
|----|----|
|Title|Test subject has syntax errors|
|Description|Undefined prefix: hmas:hasLanguage|

***
### MajorFail Assertion number 12

[Jump to summary definition](#summary-MajorFail-12)

:boom:MajorFail assertion
#### Subject detail
|Name|fipa|
|----|----|
|Title|Standalone module src/fipa.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module fipa.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/fipa.ttl)|

#### Criterion detail
|Identifier|[syntax](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#syntax)|
|----|----|
|Title|Syntax test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:boom:MajorFail|
|----|----|
|Title|Test subject has syntax errors|
|Description|Undefined prefix: hmas:hasEncoding|

***
### MajorFail Assertion number 13

[Jump to summary definition](#summary-MajorFail-13)

:boom:MajorFail assertion
#### Subject detail
|Name|fipa|
|----|----|
|Title|Standalone module src/fipa.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module fipa.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/fipa.ttl)|

#### Criterion detail
|Identifier|[syntax](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#syntax)|
|----|----|
|Title|Syntax test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:boom:MajorFail|
|----|----|
|Title|Test subject has syntax errors|
|Description|Undefined prefix: hmas:hasOntology|

***
### MajorFail Assertion number 14

[Jump to summary definition](#summary-MajorFail-14)

:boom:MajorFail assertion
#### Subject detail
|Name|fipa|
|----|----|
|Title|Standalone module src/fipa.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module fipa.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/fipa.ttl)|

#### Criterion detail
|Identifier|[syntax](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#syntax)|
|----|----|
|Title|Syntax test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:boom:MajorFail|
|----|----|
|Title|Test subject has syntax errors|
|Description|Undefined prefix: hmas:hasProtocol|

***
### MajorFail Assertion number 15

[Jump to summary definition](#summary-MajorFail-15)

:boom:MajorFail assertion
#### Subject detail
|Name|fipa|
|----|----|
|Title|Standalone module src/fipa.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module fipa.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/fipa.ttl)|

#### Criterion detail
|Identifier|[syntax](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#syntax)|
|----|----|
|Title|Syntax test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:boom:MajorFail|
|----|----|
|Title|Test subject has syntax errors|
|Description|Undefined prefix: hmas:hasConversation|

***
### MajorFail Assertion number 16

[Jump to summary definition](#summary-MajorFail-16)

:boom:MajorFail assertion
#### Subject detail
|Name|fipa|
|----|----|
|Title|Standalone module src/fipa.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module fipa.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/fipa.ttl)|

#### Criterion detail
|Identifier|[syntax](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#syntax)|
|----|----|
|Title|Syntax test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:boom:MajorFail|
|----|----|
|Title|Test subject has syntax errors|
|Description|Undefined prefix: hmas:replyWith|

***
### MajorFail Assertion number 17

[Jump to summary definition](#summary-MajorFail-17)

:boom:MajorFail assertion
#### Subject detail
|Name|fipa|
|----|----|
|Title|Standalone module src/fipa.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module fipa.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/fipa.ttl)|

#### Criterion detail
|Identifier|[syntax](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#syntax)|
|----|----|
|Title|Syntax test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:boom:MajorFail|
|----|----|
|Title|Test subject has syntax errors|
|Description|Undefined prefix: hmas:isInReplyTo|

***
### MajorFail Assertion number 18

[Jump to summary definition](#summary-MajorFail-18)

:boom:MajorFail assertion
#### Subject detail
|Name|fipa|
|----|----|
|Title|Standalone module src/fipa.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module fipa.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/fipa.ttl)|

#### Criterion detail
|Identifier|[syntax](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#syntax)|
|----|----|
|Title|Syntax test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:boom:MajorFail|
|----|----|
|Title|Test subject has syntax errors|
|Description|Undefined prefix: hmas:replyBy|

***

</details>

***


# MinorFail Assertions

Here is the chapter related to the MinorFail assertion

:exclamation:109 MinorFail assertions

<details>
<summary>Fold/Unfold the 109 summary and details</summary>

## MinorFail Assertions Summary

[Jump to statistic summary](#statistic-summary)

:exclamation:109 MinorFail assertions

|*Jump*|*Number*|*Status*|*Subject*|*Criterion*|*Title*|*Link*|
|------|--------|--------|---------|-----------|-------|------|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-1">1/109</div>|:exclamation:*MinorFail*|`regulation-logistics-structure-organization`|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|Terms not labeled|[Jump](#minorfail-assertion-number-1)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-2">2/109</div>|:exclamation:*MinorFail*|`regulation-logistics-structure-organization`|[terms-differenciation](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#terms-differenciation)|Too close terms|[Jump](#minorfail-assertion-number-2)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-3">3/109</div>|:exclamation:*MinorFail*|`regulation-logistics-create-organization`|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|Terms not labeled|[Jump](#minorfail-assertion-number-3)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-4">4/109</div>|:exclamation:*MinorFail*|`regulation-logistics-create-organization`|[terms-differenciation](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#terms-differenciation)|Too close terms|[Jump](#minorfail-assertion-number-4)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-5">5/109</div>|:exclamation:*MinorFail*|`regulation`|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|Terms not labeled|[Jump](#minorfail-assertion-number-5)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-6">6/109</div>|:exclamation:*MinorFail*|`regulation`|[terms-differenciation](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#terms-differenciation)|Too close terms|[Jump](#minorfail-assertion-number-6)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-7">7/109</div>|:exclamation:*MinorFail*|`manufacturing-environments-discover-signifiers`|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|Terms not labeled|[Jump](#minorfail-assertion-number-7)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-8">8/109</div>|:exclamation:*MinorFail*|`manufacturing-environments-discover-signifiers`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-assertion-number-8)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-9">9/109</div>|:exclamation:*MinorFail*|`manufacturing-environments-discover-signifiers`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-assertion-number-9)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-10">10/109</div>|:exclamation:*MinorFail*|`manufacturing-environments-discover-signifiers`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-assertion-number-10)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-11">11/109</div>|:exclamation:*MinorFail*|`manufacturing-environments-discover-signifiers`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-assertion-number-11)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-12">12/109</div>|:exclamation:*MinorFail*|`manufacturing-environments-discover-signifiers`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-assertion-number-12)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-13">13/109</div>|:exclamation:*MinorFail*|`manufacturing-environments-discover-signifiers`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-assertion-number-13)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-14">14/109</div>|:exclamation:*MinorFail*|`manufacturing-environments-discover-platforms`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-assertion-number-14)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-15">15/109</div>|:exclamation:*MinorFail*|`manufacturing-environments-discover-core`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-assertion-number-15)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-16">16/109</div>|:exclamation:*MinorFail*|`manufacturing-environments-discover-core`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-assertion-number-16)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-17">17/109</div>|:exclamation:*MinorFail*|`logistics-structure-organization`|[terms-differenciation](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#terms-differenciation)|Too close terms|[Jump](#minorfail-assertion-number-17)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-18">18/109</div>|:exclamation:*MinorFail*|`logistics-create-organization`|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|Terms not labeled|[Jump](#minorfail-assertion-number-18)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-19">19/109</div>|:exclamation:*MinorFail*|`interaction-manufacturing-environments-discover-behavior-specifications`|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|Terms not labeled|[Jump](#minorfail-assertion-number-19)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-20">20/109</div>|:exclamation:*MinorFail*|`interaction`|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|Terms not labeled|[Jump](#minorfail-assertion-number-20)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-21">21/109</div>|:exclamation:*MinorFail*|`core-manufacturing-environments-discover-signifiers`|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|Terms not labeled|[Jump](#minorfail-assertion-number-21)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-22">22/109</div>|:exclamation:*MinorFail*|`core-manufacturing-environments-discover-signifiers`|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|Terms not labeled|[Jump](#minorfail-assertion-number-22)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-23">23/109</div>|:exclamation:*MinorFail*|`core-manufacturing-environments-discover-signifiers`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-assertion-number-23)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-24">24/109</div>|:exclamation:*MinorFail*|`core-manufacturing-environments-discover-signifiers`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-assertion-number-24)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-25">25/109</div>|:exclamation:*MinorFail*|`core-manufacturing-environments-discover-signifiers`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-assertion-number-25)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-26">26/109</div>|:exclamation:*MinorFail*|`core-manufacturing-environments-discover-signifiers`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-assertion-number-26)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-27">27/109</div>|:exclamation:*MinorFail*|`core-manufacturing-environments-discover-signifiers`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-assertion-number-27)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-28">28/109</div>|:exclamation:*MinorFail*|`core-manufacturing-environments-discover-signifiers`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-assertion-number-28)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-29">29/109</div>|:exclamation:*MinorFail*|`core-manufacturing-environments-discover-signifiers`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-assertion-number-29)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-30">30/109</div>|:exclamation:*MinorFail*|`core-manufacturing-environments-discover-signifiers`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-assertion-number-30)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-31">31/109</div>|:exclamation:*MinorFail*|`core-manufacturing-environments-discover-platforms`|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|Domain out of vocabulary|[Jump](#minorfail-assertion-number-31)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-32">32/109</div>|:exclamation:*MinorFail*|`core-manufacturing-environments-discover-platforms`|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|Range out of vocabulary|[Jump](#minorfail-assertion-number-32)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-33">33/109</div>|:exclamation:*MinorFail*|`core-manufacturing-environments-discover-platforms`|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|Terms not labeled|[Jump](#minorfail-assertion-number-33)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-34">34/109</div>|:exclamation:*MinorFail*|`core-manufacturing-environments-discover-platforms`|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|Terms not labeled|[Jump](#minorfail-assertion-number-34)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-35">35/109</div>|:exclamation:*MinorFail*|`core-manufacturing-environments-discover-platforms`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-assertion-number-35)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-36">36/109</div>|:exclamation:*MinorFail*|`core-manufacturing-environments-discover-platforms`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-assertion-number-36)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-37">37/109</div>|:exclamation:*MinorFail*|`core-manufacturing-environments-discover-platforms`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-assertion-number-37)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-38">38/109</div>|:exclamation:*MinorFail*|`core-manufacturing-environments-discover-platforms`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-assertion-number-38)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-39">39/109</div>|:exclamation:*MinorFail*|`core-manufacturing-environments-discover-platforms`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-assertion-number-39)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-40">40/109</div>|:exclamation:*MinorFail*|`core-manufacturing-environments-discover-platforms`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-assertion-number-40)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-41">41/109</div>|:exclamation:*MinorFail*|`core-manufacturing-environments-discover-platforms`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-assertion-number-41)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-42">42/109</div>|:exclamation:*MinorFail*|`core-manufacturing-environments-discover-platforms`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-assertion-number-42)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-43">43/109</div>|:exclamation:*MinorFail*|`core-manufacturing-environments-discover-organization`|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|Terms not labeled|[Jump](#minorfail-assertion-number-43)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-44">44/109</div>|:exclamation:*MinorFail*|`core-manufacturing-environments-discover-organization`|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|Terms not labeled|[Jump](#minorfail-assertion-number-44)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-45">45/109</div>|:exclamation:*MinorFail*|`core-manufacturing-environments-discover-organization`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-assertion-number-45)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-46">46/109</div>|:exclamation:*MinorFail*|`core-manufacturing-environments-discover-organization`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-assertion-number-46)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-47">47/109</div>|:exclamation:*MinorFail*|`core-manufacturing-environments-discover-organization`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-assertion-number-47)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-48">48/109</div>|:exclamation:*MinorFail*|`core-manufacturing-environments-discover-organization`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-assertion-number-48)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-49">49/109</div>|:exclamation:*MinorFail*|`core-manufacturing-environments-discover-organization`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-assertion-number-49)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-50">50/109</div>|:exclamation:*MinorFail*|`core-manufacturing-environments-discover-organization`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-assertion-number-50)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-51">51/109</div>|:exclamation:*MinorFail*|`core-manufacturing-environments-discover-organization`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-assertion-number-51)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-52">52/109</div>|:exclamation:*MinorFail*|`core-manufacturing-environments-discover-organization`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-assertion-number-52)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-53">53/109</div>|:exclamation:*MinorFail*|`core-manufacturing-environments-discover-core`|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|Terms not labeled|[Jump](#minorfail-assertion-number-53)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-54">54/109</div>|:exclamation:*MinorFail*|`core-manufacturing-environments-discover-core`|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|Terms not labeled|[Jump](#minorfail-assertion-number-54)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-55">55/109</div>|:exclamation:*MinorFail*|`core-manufacturing-environments-discover-core`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-assertion-number-55)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-56">56/109</div>|:exclamation:*MinorFail*|`core-manufacturing-environments-discover-core`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-assertion-number-56)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-57">57/109</div>|:exclamation:*MinorFail*|`core-manufacturing-environments-discover-core`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-assertion-number-57)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-58">58/109</div>|:exclamation:*MinorFail*|`core-manufacturing-environments-discover-core`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-assertion-number-58)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-59">59/109</div>|:exclamation:*MinorFail*|`core-manufacturing-environments-discover-core`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-assertion-number-59)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-60">60/109</div>|:exclamation:*MinorFail*|`core-manufacturing-environments-discover-core`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-assertion-number-60)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-61">61/109</div>|:exclamation:*MinorFail*|`core-manufacturing-environments-discover-core`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-assertion-number-61)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-62">62/109</div>|:exclamation:*MinorFail*|`core-manufacturing-environments-discover-core`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-assertion-number-62)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-63">63/109</div>|:exclamation:*MinorFail*|`core`|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|Terms not labeled|[Jump](#minorfail-assertion-number-63)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-64">64/109</div>|:exclamation:*MinorFail*|`core`|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|Terms not labeled|[Jump](#minorfail-assertion-number-64)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-65">65/109</div>|:exclamation:*MinorFail*|`core`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-assertion-number-65)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-66">66/109</div>|:exclamation:*MinorFail*|`core`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-assertion-number-66)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-67">67/109</div>|:exclamation:*MinorFail*|`core`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-assertion-number-67)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-68">68/109</div>|:exclamation:*MinorFail*|`core`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-assertion-number-68)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-69">69/109</div>|:exclamation:*MinorFail*|`core`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-assertion-number-69)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-70">70/109</div>|:exclamation:*MinorFail*|`core`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-assertion-number-70)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-71">71/109</div>|:exclamation:*MinorFail*|`core`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-assertion-number-71)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-72">72/109</div>|:exclamation:*MinorFail*|`core`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-assertion-number-72)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-73">73/109</div>|:exclamation:*MinorFail*|`all-modules`|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|Terms not labeled|[Jump](#minorfail-assertion-number-73)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-74">74/109</div>|:exclamation:*MinorFail*|`all-modules`|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|Terms not labeled|[Jump](#minorfail-assertion-number-74)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-75">75/109</div>|:exclamation:*MinorFail*|`all-modules`|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|Terms not labeled|[Jump](#minorfail-assertion-number-75)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-76">76/109</div>|:exclamation:*MinorFail*|`all-modules`|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|Terms not labeled|[Jump](#minorfail-assertion-number-76)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-77">77/109</div>|:exclamation:*MinorFail*|`all-modules`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-assertion-number-77)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-78">78/109</div>|:exclamation:*MinorFail*|`all-modules`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-assertion-number-78)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-79">79/109</div>|:exclamation:*MinorFail*|`all-modules`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-assertion-number-79)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-80">80/109</div>|:exclamation:*MinorFail*|`all-modules`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-assertion-number-80)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-81">81/109</div>|:exclamation:*MinorFail*|`all-modules`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-assertion-number-81)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-82">82/109</div>|:exclamation:*MinorFail*|`all-modules`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-assertion-number-82)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-83">83/109</div>|:exclamation:*MinorFail*|`all-modules`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-assertion-number-83)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-84">84/109</div>|:exclamation:*MinorFail*|`all-modules`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-assertion-number-84)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-85">85/109</div>|:exclamation:*MinorFail*|`all-modules`|[terms-differenciation](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#terms-differenciation)|Too close terms|[Jump](#minorfail-assertion-number-85)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-86">86/109</div>|:exclamation:*MinorFail*|`all-modules`|[terms-differenciation](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#terms-differenciation)|Too close terms|[Jump](#minorfail-assertion-number-86)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-87">87/109</div>|:exclamation:*MinorFail*|`all-modules`|[terms-differenciation](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#terms-differenciation)|Too close terms|[Jump](#minorfail-assertion-number-87)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-88">88/109</div>|:exclamation:*MinorFail*|`all-fragments`|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|Domain out of vocabulary|[Jump](#minorfail-assertion-number-88)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-89">89/109</div>|:exclamation:*MinorFail*|`all-fragments`|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|Range out of vocabulary|[Jump](#minorfail-assertion-number-89)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-90">90/109</div>|:exclamation:*MinorFail*|`all-fragments`|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|Terms not labeled|[Jump](#minorfail-assertion-number-90)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-91">91/109</div>|:exclamation:*MinorFail*|`all-fragments`|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|Terms not labeled|[Jump](#minorfail-assertion-number-91)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-92">92/109</div>|:exclamation:*MinorFail*|`all-fragments`|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|Terms not labeled|[Jump](#minorfail-assertion-number-92)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-93">93/109</div>|:exclamation:*MinorFail*|`all-fragments`|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|Terms not labeled|[Jump](#minorfail-assertion-number-93)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-94">94/109</div>|:exclamation:*MinorFail*|`all-fragments`|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|Terms not labeled|[Jump](#minorfail-assertion-number-94)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-95">95/109</div>|:exclamation:*MinorFail*|`all-fragments`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-assertion-number-95)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-96">96/109</div>|:exclamation:*MinorFail*|`all-fragments`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-assertion-number-96)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-97">97/109</div>|:exclamation:*MinorFail*|`all-fragments`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-assertion-number-97)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-98">98/109</div>|:exclamation:*MinorFail*|`all-fragments`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-assertion-number-98)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-99">99/109</div>|:exclamation:*MinorFail*|`all-fragments`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-assertion-number-99)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-100">100/109</div>|:exclamation:*MinorFail*|`all-fragments`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL QL Profile incompatible|[Jump](#minorfail-assertion-number-100)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-101">101/109</div>|:exclamation:*MinorFail*|`all-fragments`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-assertion-number-101)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-102">102/109</div>|:exclamation:*MinorFail*|`all-fragments`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-assertion-number-102)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-103">103/109</div>|:exclamation:*MinorFail*|`all-fragments`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-assertion-number-103)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-104">104/109</div>|:exclamation:*MinorFail*|`all-fragments`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-assertion-number-104)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-105">105/109</div>|:exclamation:*MinorFail*|`all-fragments`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-assertion-number-105)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-106">106/109</div>|:exclamation:*MinorFail*|`all-fragments`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL EL Profile incompatible|[Jump](#minorfail-assertion-number-106)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-107">107/109</div>|:exclamation:*MinorFail*|`all-fragments`|[terms-differenciation](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#terms-differenciation)|Too close terms|[Jump](#minorfail-assertion-number-107)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-108">108/109</div>|:exclamation:*MinorFail*|`all-fragments`|[terms-differenciation](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#terms-differenciation)|Too close terms|[Jump](#minorfail-assertion-number-108)|
|[Table top](#minorfail-assertions-summary)|<div id="summary-MinorFail-109">109/109</div>|:exclamation:*MinorFail*|`all-fragments`|[terms-differenciation](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#terms-differenciation)|Too close terms|[Jump](#minorfail-assertion-number-109)|

***

## MinorFail Assertion Details

This subchapter gives more details to the :exclamation:MinorFail assertions

### MinorFail Assertion number 1

[Jump to summary definition](#summary-MinorFail-1)

:exclamation:MinorFail assertion
#### Subject detail
|Name|regulation-logistics-structure-organization|
|----|----|
|Title|Merged module src/regulation.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/logistics/structure-organization/onto.ttl|
|Composition|- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)<br/>- [Modelet logistics/structure-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|
|----|----|
|Title|Term labeling test|
|Description|A test case from the Best Practices tests checking if all the terms of the subject have a rdfs:label property pointing to a literal in English|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|Terms not labeled|
|Description|The term :regulation has no rdfs:label to define it in natural language|
|Pointer|<pre lang="Turtle"><code>:regulation a owl:Ontology ;&#10;cc:license &#60;https://creativecommons.org/licenses/by/4.0/> ;&#10;dct:contributor &#60;http://maxime-lefrancois.info/me#>, &#10; &#60;http://ns.inria.fr/fabien.gandon#me>, &#10; &#60;https://danaivach.inrupt.net/profile/card#me>, &#10; &#60;https://orcid.org/0000-0002-2956-0533>, &#10; &#60;https://orcid.org/0000-0002-3497-8758>, &#10; &#60;https://orcid.org/0000-0003-0821-6095>, &#10; &#60;https://orcid.org/0000-0003-4509-9537> ;&#10;dct:creator &#60;https://orcid.org/0000-0002-4506-2745> ;&#10;dct:description "An ontology to describe the regulation of Hypermedia Multi-A..."@en,&#10;"L'ontologie pour décrire la régulation des systèmes multi-ag..."@fr ;&#10;dct:issued "2022-05-01"^^xsd:date ;&#10;dct:title "Hypermedia MAS Regulation Ontology"@en,&#10;"Ontologie de Régulation des SMA Hypermédias"@fr ;&#10;vann:preferredNamespacePrefix "hmas" ;&#10;vann:preferredNamespaceUri : ;&#10;owl:imports :core .</code></pre>|

***
### MinorFail Assertion number 2

[Jump to summary definition](#summary-MinorFail-2)

:exclamation:MinorFail assertion
#### Subject detail
|Name|regulation-logistics-structure-organization|
|----|----|
|Title|Merged module src/regulation.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/logistics/structure-organization/onto.ttl|
|Composition|- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)<br/>- [Modelet logistics/structure-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#terms-differenciation)|
|----|----|
|Title|Terms differenciation test|
|Description|A test case from the Best Practices tests checking if all the terms are different enough from each other according to the Levenshtein distance metric.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|Too close terms|
|Description|The following terms are too similar: :isMembershipOf and :isMembershipIn|
|Pointer|<pre lang="Turtle"><code>:isMembershipOf a owl:ObjectProperty ;&#10;rdfs:label "is membership of"@en,&#10;"est l'appartenance à"@fr ;&#10;rdfs:comment "A relation that refers to the Agent involved in a Membership..."@en ;&#10;rdfs:domain :Membership ;&#10;rdfs:isDefinedBy :regulation ;&#10;rdfs:range :Agent .</code></pre>|
|Pointer|<pre lang="Turtle"><code>:isMembershipIn a owl:ObjectProperty ;&#10;rdfs:label "is membership in"@en,&#10;"est l'appartenance à"@fr ;&#10;rdfs:comment "A relation that refers to the Group involved in a Membership..."@en ;&#10;rdfs:domain :Membership ;&#10;rdfs:isDefinedBy :regulation ;&#10;rdfs:range :Group .</code></pre>|

***
### MinorFail Assertion number 3

[Jump to summary definition](#summary-MinorFail-3)

:exclamation:MinorFail assertion
#### Subject detail
|Name|regulation-logistics-create-organization|
|----|----|
|Title|Merged module src/regulation.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/logistics/create-organization/onto.ttl|
|Composition|- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)<br/>- [Modelet logistics/create-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/create-organization/onto.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|
|----|----|
|Title|Term labeling test|
|Description|A test case from the Best Practices tests checking if all the terms of the subject have a rdfs:label property pointing to a literal in English|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|Terms not labeled|
|Description|The term :regulation has no rdfs:label to define it in natural language|
|Pointer|<pre lang="Turtle"><code>:regulation a owl:Ontology ;&#10;cc:license &#60;https://creativecommons.org/licenses/by/4.0/> ;&#10;dct:contributor &#60;http://maxime-lefrancois.info/me#>, &#10; &#60;http://ns.inria.fr/fabien.gandon#me>, &#10; &#60;https://danaivach.inrupt.net/profile/card#me>, &#10; &#60;https://orcid.org/0000-0002-2956-0533>, &#10; &#60;https://orcid.org/0000-0002-3497-8758>, &#10; &#60;https://orcid.org/0000-0003-0821-6095>, &#10; &#60;https://orcid.org/0000-0003-4509-9537> ;&#10;dct:creator &#60;https://orcid.org/0000-0002-4506-2745> ;&#10;dct:description "An ontology to describe the regulation of Hypermedia Multi-A..."@en,&#10;"L'ontologie pour décrire la régulation des systèmes multi-ag..."@fr ;&#10;dct:issued "2022-05-01"^^xsd:date ;&#10;dct:title "Hypermedia MAS Regulation Ontology"@en,&#10;"Ontologie de Régulation des SMA Hypermédias"@fr ;&#10;vann:preferredNamespacePrefix "hmas" ;&#10;vann:preferredNamespaceUri : ;&#10;owl:imports :core .</code></pre>|

***
### MinorFail Assertion number 4

[Jump to summary definition](#summary-MinorFail-4)

:exclamation:MinorFail assertion
#### Subject detail
|Name|regulation-logistics-create-organization|
|----|----|
|Title|Merged module src/regulation.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/logistics/create-organization/onto.ttl|
|Composition|- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)<br/>- [Modelet logistics/create-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/create-organization/onto.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#terms-differenciation)|
|----|----|
|Title|Terms differenciation test|
|Description|A test case from the Best Practices tests checking if all the terms are different enough from each other according to the Levenshtein distance metric.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|Too close terms|
|Description|The following terms are too similar: :isMembershipOf and :isMembershipIn|
|Pointer|<pre lang="Turtle"><code>:isMembershipOf a owl:ObjectProperty ;&#10;rdfs:label "is membership of"@en,&#10;"est l'appartenance à"@fr ;&#10;rdfs:comment "A relation that refers to the Agent involved in a Membership..."@en ;&#10;rdfs:domain :Membership ;&#10;rdfs:isDefinedBy :regulation ;&#10;rdfs:range :Agent .</code></pre>|
|Pointer|<pre lang="Turtle"><code>:isMembershipIn a owl:ObjectProperty ;&#10;rdfs:label "is membership in"@en,&#10;"est l'appartenance à"@fr ;&#10;rdfs:comment "A relation that refers to the Group involved in a Membership..."@en ;&#10;rdfs:domain :Membership ;&#10;rdfs:isDefinedBy :regulation ;&#10;rdfs:range :Group .</code></pre>|

***
### MinorFail Assertion number 5

[Jump to summary definition](#summary-MinorFail-5)

:exclamation:MinorFail assertion
#### Subject detail
|Name|regulation|
|----|----|
|Title|Standalone module src/regulation.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|
|----|----|
|Title|Term labeling test|
|Description|A test case from the Best Practices tests checking if all the terms of the subject have a rdfs:label property pointing to a literal in English|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|Terms not labeled|
|Description|The term :regulation has no rdfs:label to define it in natural language|
|Pointer|<pre lang="Turtle"><code>:regulation a owl:Ontology ;&#10;cc:license &#60;https://creativecommons.org/licenses/by/4.0/> ;&#10;dct:contributor &#60;http://maxime-lefrancois.info/me#>, &#10; &#60;http://ns.inria.fr/fabien.gandon#me>, &#10; &#60;https://danaivach.inrupt.net/profile/card#me>, &#10; &#60;https://orcid.org/0000-0002-2956-0533>, &#10; &#60;https://orcid.org/0000-0002-3497-8758>, &#10; &#60;https://orcid.org/0000-0003-0821-6095>, &#10; &#60;https://orcid.org/0000-0003-4509-9537> ;&#10;dct:creator &#60;https://orcid.org/0000-0002-4506-2745> ;&#10;dct:description "An ontology to describe the regulation of Hypermedia Multi-A..."@en,&#10;"L'ontologie pour décrire la régulation des systèmes multi-ag..."@fr ;&#10;dct:issued "2022-05-01"^^xsd:date ;&#10;dct:title "Hypermedia MAS Regulation Ontology"@en,&#10;"Ontologie de Régulation des SMA Hypermédias"@fr ;&#10;vann:preferredNamespacePrefix "hmas" ;&#10;vann:preferredNamespaceUri : ;&#10;owl:imports :core .</code></pre>|

***
### MinorFail Assertion number 6

[Jump to summary definition](#summary-MinorFail-6)

:exclamation:MinorFail assertion
#### Subject detail
|Name|regulation|
|----|----|
|Title|Standalone module src/regulation.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#terms-differenciation)|
|----|----|
|Title|Terms differenciation test|
|Description|A test case from the Best Practices tests checking if all the terms are different enough from each other according to the Levenshtein distance metric.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|Too close terms|
|Description|The following terms are too similar: :isMembershipOf and :isMembershipIn|
|Pointer|<pre lang="Turtle"><code>:isMembershipOf a owl:ObjectProperty ;&#10;rdfs:label "is membership of"@en,&#10;"est l'appartenance à"@fr ;&#10;rdfs:comment "A relation that refers to the Agent involved in a Membership..."@en ;&#10;rdfs:domain :Membership ;&#10;rdfs:isDefinedBy :regulation ;&#10;rdfs:range :Agent .</code></pre>|
|Pointer|<pre lang="Turtle"><code>:isMembershipIn a owl:ObjectProperty ;&#10;rdfs:label "is membership in"@en,&#10;"est l'appartenance à"@fr ;&#10;rdfs:comment "A relation that refers to the Group involved in a Membership..."@en ;&#10;rdfs:domain :Membership ;&#10;rdfs:isDefinedBy :regulation ;&#10;rdfs:range :Group .</code></pre>|

***
### MinorFail Assertion number 7

[Jump to summary definition](#summary-MinorFail-7)

:exclamation:MinorFail assertion
#### Subject detail
|Name|manufacturing-environments-discover-signifiers|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/discover-signifiers/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|
|----|----|
|Title|Term labeling test|
|Description|A test case from the Best Practices tests checking if all the terms of the subject have a rdfs:label property pointing to a literal in English|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|Terms not labeled|
|Description|The term :Affordance has no rdfs:label to define it in natural language|
|Pointer|<pre lang="Turtle"><code>:Affordance a skos:Concept ;&#10;dct:references [ rdfs:label "Chemero and Turvey, 2007"@en ;&#10;dct:bibliographicCitation "Chemero, A., & Turvey, M. T. (2007). Complexity, hypersets, ..."@en ],&#10;[ rdfs:label "Norman, 2013"@en ;&#10;dct:bibliographicCitation "Norman, D. (2013). The design of everyday things: Revised an..."@en ] ;&#10;rdfs:isDefinedBy :core ;&#10;skos:definition "A behavior possibility that is a relationship between an abi..."@en ;&#10;skos:editorialNote "The concept has been considered as a candidate term for repr..."@en ;&#10;skos:historyNote "The definition of the concept follows affordance theorists [..."@en ;&#10;skos:prefLabel "affordance"@en ;&#10;skos:related :Signifier .</code></pre>|

***
### MinorFail Assertion number 8

[Jump to summary definition](#summary-MinorFail-8)

:exclamation:MinorFail assertion
#### Subject detail
|Name|manufacturing-environments-discover-signifiers|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/discover-signifiers/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL QL Profile incompatible|
|Description|Anonymous individuals are not supported|
|Pointer|<pre lang="Turtle"><code>[] rdfs:label "Chemero and Turvey, 2007"@en ;&#10;dc:bibliographicCitation "Chemero, A., & Turvey, M. T. (2007). Complexity, hypersets, ..."@en .</code></pre>|

***
### MinorFail Assertion number 9

[Jump to summary definition](#summary-MinorFail-9)

:exclamation:MinorFail assertion
#### Subject detail
|Name|manufacturing-environments-discover-signifiers|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/discover-signifiers/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL QL Profile incompatible|
|Description|Anonymous individuals are not supported|
|Pointer|<pre lang="Turtle"><code>[] rdfs:label "Norman, 2013"@en ;&#10;dc:bibliographicCitation "Norman, D. (2013). The design of everyday things: Revised an..."@en .</code></pre>|

***
### MinorFail Assertion number 10

[Jump to summary definition](#summary-MinorFail-10)

:exclamation:MinorFail assertion
#### Subject detail
|Name|manufacturing-environments-discover-signifiers|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/discover-signifiers/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL QL Profile incompatible|
|Description|Anonymous individuals are not supported|
|Pointer|<pre lang="Turtle"><code>&#60;https://purl.org/hmas/Affordance> a skos:Concept ;&#10;dc:references [ rdfs:label "Chemero and Turvey, 2007"@en ;&#10;dc:bibliographicCitation "Chemero, A., & Turvey, M. T. (2007). Complexity, hypersets, ..."@en ],&#10;[ rdfs:label "Norman, 2013"@en ;&#10;dc:bibliographicCitation "Norman, D. (2013). The design of everyday things: Revised an..."@en ] ;&#10;rdfs:isDefinedBy &#60;https://purl.org/hmas/core> ;&#10;skos:definition "A behavior possibility that is a relationship between an abi..."@en ;&#10;skos:editorialNote "The concept has been considered as a candidate term for repr..."@en ;&#10;skos:historyNote "The definition of the concept follows affordance theorists [..."@en ;&#10;skos:prefLabel "affordance"@en ;&#10;skos:related &#60;https://purl.org/hmas/Signifier> .</code></pre>|

***
### MinorFail Assertion number 11

[Jump to summary definition](#summary-MinorFail-11)

:exclamation:MinorFail assertion
#### Subject detail
|Name|manufacturing-environments-discover-signifiers|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/discover-signifiers/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL EL Profile incompatible|
|Description|Anonymous individuals are not supported|
|Pointer|<pre lang="Turtle"><code>[] rdfs:label "Chemero and Turvey, 2007"@en ;&#10;dc:bibliographicCitation "Chemero, A., & Turvey, M. T. (2007). Complexity, hypersets, ..."@en .</code></pre>|

***
### MinorFail Assertion number 12

[Jump to summary definition](#summary-MinorFail-12)

:exclamation:MinorFail assertion
#### Subject detail
|Name|manufacturing-environments-discover-signifiers|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/discover-signifiers/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL EL Profile incompatible|
|Description|Anonymous individuals are not supported|
|Pointer|<pre lang="Turtle"><code>[] rdfs:label "Norman, 2013"@en ;&#10;dc:bibliographicCitation "Norman, D. (2013). The design of everyday things: Revised an..."@en .</code></pre>|

***
### MinorFail Assertion number 13

[Jump to summary definition](#summary-MinorFail-13)

:exclamation:MinorFail assertion
#### Subject detail
|Name|manufacturing-environments-discover-signifiers|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/discover-signifiers/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL EL Profile incompatible|
|Description|Anonymous individuals are not supported|
|Pointer|<pre lang="Turtle"><code>&#60;https://purl.org/hmas/Affordance> a skos:Concept ;&#10;dc:references [ rdfs:label "Chemero and Turvey, 2007"@en ;&#10;dc:bibliographicCitation "Chemero, A., & Turvey, M. T. (2007). Complexity, hypersets, ..."@en ],&#10;[ rdfs:label "Norman, 2013"@en ;&#10;dc:bibliographicCitation "Norman, D. (2013). The design of everyday things: Revised an..."@en ] ;&#10;rdfs:isDefinedBy &#60;https://purl.org/hmas/core> ;&#10;skos:definition "A behavior possibility that is a relationship between an abi..."@en ;&#10;skos:editorialNote "The concept has been considered as a candidate term for repr..."@en ;&#10;skos:historyNote "The definition of the concept follows affordance theorists [..."@en ;&#10;skos:prefLabel "affordance"@en ;&#10;skos:related &#60;https://purl.org/hmas/Signifier> .</code></pre>|

***
### MinorFail Assertion number 14

[Jump to summary definition](#summary-MinorFail-14)

:exclamation:MinorFail assertion
#### Subject detail
|Name|manufacturing-environments-discover-platforms|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/discover-platforms/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/discover-platforms/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-platforms/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL EL Profile incompatible|
|Description|Statement not supported|
|Pointer|<pre lang="Turtle"><code>&#60;https://purl.org/hmas/hosts> a owl:AsymmetricProperty,&#10;owl:ObjectProperty ;&#10;rdfs:label "hosts"@en ;&#10;dc:source &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/8#issuecomment-1025991719> ;&#10;rdfs:comment "A relation that refers to an information resource or a proce..."@en ;&#10;rdfs:domain &#60;https://purl.org/hmas/HypermediaMASPlatform> ;&#10;rdfs:isDefinedBy &#60;https://purl.org/hmas/core> ;&#10;rdfs:range &#60;https://purl.org/hmas/Hostable> ;&#10;rdfs:seeAlso &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/18>, &#10; &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/49> .</code></pre>|

***
### MinorFail Assertion number 15

[Jump to summary definition](#summary-MinorFail-15)

:exclamation:MinorFail assertion
#### Subject detail
|Name|manufacturing-environments-discover-core|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/discover-core/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/discover-core/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-core/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL QL Profile incompatible|
|Description|Statement not supported|
|Pointer|<pre lang="Turtle"><code>&#60;https://purl.org/hmas/transitivelyContains> a owl:ObjectProperty,&#10;owl:TransitiveProperty ;&#10;rdfs:label "transitivelyContains"@en ;&#10;rdfs:comment "Links all the resources that are logically contained in a wo..."@en ;&#10;rdfs:domain &#60;https://purl.org/hmas/Workspace> ;&#10;rdfs:isDefinedBy &#60;https://purl.org/hmas/core> ;&#10;owl:inverseOf &#60;https://purl.org/hmas/isTransitivelyContainedIn> .</code></pre>|

***
### MinorFail Assertion number 16

[Jump to summary definition](#summary-MinorFail-16)

:exclamation:MinorFail assertion
#### Subject detail
|Name|manufacturing-environments-discover-core|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/discover-core/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/discover-core/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-core/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL EL Profile incompatible|
|Description|Statement not supported|
|Pointer|<pre lang="Turtle"><code>&#60;https://purl.org/hmas/hasProfile> a owl:AsymmetricProperty,&#10;owl:ObjectProperty ;&#10;rdfs:label "has profile"@en ;&#10;rdfs:comment "A relation that links a resource to its profile."@en ;&#10;rdfs:isDefinedBy &#60;https://purl.org/hmas/core> ;&#10;rdfs:range &#60;https://purl.org/hmas/ResourceProfile> ;&#10;owl:inverseOf &#60;https://purl.org/hmas/isProfileOf> .</code></pre>|

***
### MinorFail Assertion number 17

[Jump to summary definition](#summary-MinorFail-17)

:exclamation:MinorFail assertion
#### Subject detail
|Name|logistics-structure-organization|
|----|----|
|Title|Standalone modelet domains/logistics/structure-organization/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet logistics/structure-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#terms-differenciation)|
|----|----|
|Title|Terms differenciation test|
|Description|A test case from the Best Practices tests checking if all the terms are different enough from each other according to the Levenshtein distance metric.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|Too close terms|
|Description|The following terms are too similar: :isMembershipOf and :isMembershipIn|
|Pointer|<pre lang="Turtle"><code>:isMembershipOf a owl:ObjectProperty ;&#10;rdfs:label "is membership of"@en,&#10;"est l'appartenance à"@fr ;&#10;rdfs:comment "A relation that refers to the Agent involved in a Membership..."@en ;&#10;rdfs:domain :Membership ;&#10;rdfs:isDefinedBy :regulation .</code></pre>|
|Pointer|<pre lang="Turtle"><code>:isMembershipIn a owl:ObjectProperty ;&#10;rdfs:label "is membership in"@en,&#10;"est l'appartenance à"@fr ;&#10;rdfs:comment "A relation that refers to the Group involved in a Membership..."@en ;&#10;rdfs:domain :Membership ;&#10;rdfs:isDefinedBy :regulation .</code></pre>|

***
### MinorFail Assertion number 18

[Jump to summary definition](#summary-MinorFail-18)

:exclamation:MinorFail assertion
#### Subject detail
|Name|logistics-create-organization|
|----|----|
|Title|Standalone modelet domains/logistics/create-organization/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet logistics/create-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/create-organization/onto.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|
|----|----|
|Title|Term labeling test|
|Description|A test case from the Best Practices tests checking if all the terms of the subject have a rdfs:label property pointing to a literal in English|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|Terms not labeled|
|Description|The term :OrganizationModel has no rdfs:label to define it in natural language|
|Pointer|<pre lang="Turtle"><code>:OrganizationModel a skos:Concept ;&#10;skos:definition "An Organization Model is the combination of Roles, Missions,..."@en ;&#10;skos:editorialNote "The Organization Model is represented as SHACL Shapes."@en ;&#10;skos:prefLabel "organization model"@en ;&#10;skos:related :Organization .</code></pre>|

***
### MinorFail Assertion number 19

[Jump to summary definition](#summary-MinorFail-19)

:exclamation:MinorFail assertion
#### Subject detail
|Name|interaction-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Merged module src/interaction.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-behavior-specifications/onto.ttl|
|Composition|- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Modelet manufacturing-environments/discover-behavior-specifications/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|
|----|----|
|Title|Term labeling test|
|Description|A test case from the Best Practices tests checking if all the terms of the subject have a rdfs:label property pointing to a literal in English|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|Terms not labeled|
|Description|The term :interaction has no rdfs:label to define it in natural language|
|Pointer|<pre lang="Turtle"><code>:interaction a owl:Ontology ;&#10;cc:license &#60;https://creativecommons.org/licenses/by/4.0/> ;&#10;dct:contributor &#60;http://ns.inria.fr/fabien.gandon#me>, &#10; &#60;https://pod.inrupt.com/andreiciortea/profile/card#me>, &#10; &#60;https://pod.inrupt.com/smnmyr/profile/card#me> ;&#10;dct:creator &#60;https://danaivach.inrupt.net/profile/card#me> ;&#10;dct:description "An ontology to describe interaction in Hypermedia Multi-Agen..."@en,&#10;"L'ontologie pour décrire l'interaction dans les systèmes mul..."@fr ;&#10;dct:issued "2023-01-13"^^xsd:date ;&#10;dct:title "Hypermedia MAS Interaction Ontology"@en,&#10;"Ontologie d'Interaction des SMA Hypermédias"@fr ;&#10;vann:preferredNamespacePrefix "hmas" ;&#10;vann:preferredNamespaceUri : ;&#10;owl:imports :core .</code></pre>|

***
### MinorFail Assertion number 20

[Jump to summary definition](#summary-MinorFail-20)

:exclamation:MinorFail assertion
#### Subject detail
|Name|interaction|
|----|----|
|Title|Standalone module src/interaction.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|
|----|----|
|Title|Term labeling test|
|Description|A test case from the Best Practices tests checking if all the terms of the subject have a rdfs:label property pointing to a literal in English|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|Terms not labeled|
|Description|The term :interaction has no rdfs:label to define it in natural language|
|Pointer|<pre lang="Turtle"><code>:interaction a owl:Ontology ;&#10;cc:license &#60;https://creativecommons.org/licenses/by/4.0/> ;&#10;dct:contributor &#60;http://ns.inria.fr/fabien.gandon#me>, &#10; &#60;https://pod.inrupt.com/andreiciortea/profile/card#me>, &#10; &#60;https://pod.inrupt.com/smnmyr/profile/card#me> ;&#10;dct:creator &#60;https://danaivach.inrupt.net/profile/card#me> ;&#10;dct:description "An ontology to describe interaction in Hypermedia Multi-Agen..."@en,&#10;"L'ontologie pour décrire l'interaction dans les systèmes mul..."@fr ;&#10;dct:issued "2023-01-13"^^xsd:date ;&#10;dct:title "Hypermedia MAS Interaction Ontology"@en,&#10;"Ontologie d'Interaction des SMA Hypermédias"@fr ;&#10;vann:preferredNamespacePrefix "hmas" ;&#10;vann:preferredNamespaceUri : ;&#10;owl:imports :core .</code></pre>|

***
### MinorFail Assertion number 21

[Jump to summary definition](#summary-MinorFail-21)

:exclamation:MinorFail assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-signifiers/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|
|----|----|
|Title|Term labeling test|
|Description|A test case from the Best Practices tests checking if all the terms of the subject have a rdfs:label property pointing to a literal in English|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|Terms not labeled|
|Description|The term :core has no rdfs:label to define it in natural language|
|Pointer|<pre lang="Turtle"><code>:core a owl:Ontology ;&#10;cc:license &#60;https://creativecommons.org/licenses/by/4.0/> ;&#10;dct:contributor &#60;http://maxime-lefrancois.info/me#>, &#10; &#60;http://ns.inria.fr/fabien.gandon#me>, &#10; &#60;http://w3id.org/people/az/me>, &#10; &#60;https://danaivach.inrupt.net/profile/card#me>, &#10; &#60;https://id.inrupt.com/smnmyr>, &#10; &#60;https://orcid.org/0000-0002-2956-0533>, &#10; &#60;https://orcid.org/0000-0002-4506-2745>, &#10; &#60;https://orcid.org/0000-0003-0821-6095>, &#10; &#60;https://www.vcharpenay.link/#me> ;&#10;dct:creator &#60;https://id.inrupt.com/andreiciortea> ;&#10;dct:description "An ontology to describe Hypermedia Multi-Agent Systems."@en,&#10;"Une ontologie pour la description de systèmes multi-agents h..."@fr ;&#10;dct:issued "2021-11-21"^^xsd:date ;&#10;dct:title "Hypermedia MAS Core Ontology"@en,&#10;"Ontologie Centrale des SMA Hypermédias"@fr ;&#10;vann:preferredNamespacePrefix "hmas" ;&#10;vann:preferredNamespaceUri : .</code></pre>|

***
### MinorFail Assertion number 22

[Jump to summary definition](#summary-MinorFail-22)

:exclamation:MinorFail assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-signifiers/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|
|----|----|
|Title|Term labeling test|
|Description|A test case from the Best Practices tests checking if all the terms of the subject have a rdfs:label property pointing to a literal in English|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|Terms not labeled|
|Description|The term :Affordance has no rdfs:label to define it in natural language|
|Pointer|<pre lang="Turtle"><code>:Affordance a skos:Concept ;&#10;dct:references [ a owl:NamedIndividual ;&#10;rdfs:label "Chemero and Turvey, 2007"@en ;&#10;dct:bibliographicCitation "Chemero, A., & Turvey, M. T. (2007). Complexity, hypersets, ..."@en ;&#10;dct:identifier &#60;https://doi.org/10.1162/biot.2007.2.1.23> ],&#10;[ a owl:NamedIndividual ;&#10;rdfs:label "Norman, 2013"@en ;&#10;dct:bibliographicCitation "Norman, D. (2013). The design of everyday things: Revised an..."@en ;&#10;dct:identifier &#60;https://mitpress.mit.edu/9780262640374/> ],&#10;[ rdfs:label "Chemero and Turvey, 2007"@en ;&#10;dct:bibliographicCitation "Chemero, A., & Turvey, M. T. (2007). Complexity, hypersets, ..."@en ],&#10;[ rdfs:label "Norman, 2013"@en ;&#10;dct:bibliographicCitation "Norman, D. (2013). The design of everyday things: Revised an..."@en ] ;&#10;rdfs:isDefinedBy :core ;&#10;skos:definition "A behavior possibility that is a relationship between an abi..."@en ;&#10;skos:editorialNote "The concept has been considered as a candidate term for repr..."@en ;&#10;skos:historyNote "The definition of the concept follows affordance theorists [..."@en ;&#10;skos:prefLabel "affordance"@en ;&#10;skos:related :Signifier .</code></pre>|

***
### MinorFail Assertion number 23

[Jump to summary definition](#summary-MinorFail-23)

:exclamation:MinorFail assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-signifiers/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL QL Profile incompatible|
|Description|Anonymous individuals are not supported|
|Pointer|<pre lang="Turtle"><code>[] a owl:NamedIndividual ;&#10;rdfs:label "Chemero and Turvey, 2007"@en ;&#10;dc:bibliographicCitation "Chemero, A., & Turvey, M. T. (2007). Complexity, hypersets, ..."@en ;&#10;dc:identifier &#60;https://doi.org/10.1162/biot.2007.2.1.23> .</code></pre>|

***
### MinorFail Assertion number 24

[Jump to summary definition](#summary-MinorFail-24)

:exclamation:MinorFail assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-signifiers/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL QL Profile incompatible|
|Description|Anonymous individuals are not supported|
|Pointer|<pre lang="Turtle"><code>[] a owl:NamedIndividual ;&#10;rdfs:label "Norman, 2013"@en ;&#10;dc:bibliographicCitation "Norman, D. (2013). The design of everyday things: Revised an..."@en ;&#10;dc:identifier &#60;https://mitpress.mit.edu/9780262640374/> .</code></pre>|

***
### MinorFail Assertion number 25

[Jump to summary definition](#summary-MinorFail-25)

:exclamation:MinorFail assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-signifiers/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL QL Profile incompatible|
|Description|Anonymous individuals are not supported|
|Pointer|<pre lang="Turtle"><code>&#60;https://purl.org/hmas/Affordance> a skos:Concept ;&#10;dc:references [ a owl:NamedIndividual ;&#10;rdfs:label "Chemero and Turvey, 2007"@en ;&#10;dc:bibliographicCitation "Chemero, A., & Turvey, M. T. (2007). Complexity, hypersets, ..."@en ;&#10;dc:identifier &#60;https://doi.org/10.1162/biot.2007.2.1.23> ],&#10;[ a owl:NamedIndividual ;&#10;rdfs:label "Norman, 2013"@en ;&#10;dc:bibliographicCitation "Norman, D. (2013). The design of everyday things: Revised an..."@en ;&#10;dc:identifier &#60;https://mitpress.mit.edu/9780262640374/> ], &#10; &#60;https://www.example.org/Noneb8129>, &#10; &#60;https://www.example.org/Noneb8130> ;&#10;rdfs:isDefinedBy &#60;https://purl.org/hmas/core> ;&#10;skos:definition "A behavior possibility that is a relationship between an abi..."@en ;&#10;skos:editorialNote "The concept has been considered as a candidate term for repr..."@en ;&#10;skos:historyNote "The definition of the concept follows affordance theorists [..."@en ;&#10;skos:prefLabel "affordance"@en ;&#10;skos:related &#60;https://purl.org/hmas/Signifier> .</code></pre>|

***
### MinorFail Assertion number 26

[Jump to summary definition](#summary-MinorFail-26)

:exclamation:MinorFail assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-signifiers/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL QL Profile incompatible|
|Description|Statement not supported|
|Pointer|<pre lang="Turtle"><code>&#60;https://purl.org/hmas/transitivelyContains> a owl:ObjectProperty,&#10;owl:TransitiveProperty ;&#10;rdfs:label "transitively contains"@en,&#10;"contient transitivement"@fr ;&#10;dc:source &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/8#issuecomment-1025991719> ;&#10;rdfs:comment "Links all the resources that are logically contained in a wo..."@en ;&#10;rdfs:domain &#60;https://purl.org/hmas/Workspace> ;&#10;rdfs:isDefinedBy &#60;https://purl.org/hmas/core> ;&#10;rdfs:seeAlso &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/18>, &#10; &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/39> ;&#10;owl:inverseOf &#60;https://purl.org/hmas/isTransitivelyContainedIn> .</code></pre>|

***
### MinorFail Assertion number 27

[Jump to summary definition](#summary-MinorFail-27)

:exclamation:MinorFail assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-signifiers/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL EL Profile incompatible|
|Description|Anonymous individuals are not supported|
|Pointer|<pre lang="Turtle"><code>[] a owl:NamedIndividual ;&#10;rdfs:label "Chemero and Turvey, 2007"@en ;&#10;dc:bibliographicCitation "Chemero, A., & Turvey, M. T. (2007). Complexity, hypersets, ..."@en ;&#10;dc:identifier &#60;https://doi.org/10.1162/biot.2007.2.1.23> .</code></pre>|

***
### MinorFail Assertion number 28

[Jump to summary definition](#summary-MinorFail-28)

:exclamation:MinorFail assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-signifiers/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL EL Profile incompatible|
|Description|Anonymous individuals are not supported|
|Pointer|<pre lang="Turtle"><code>[] a owl:NamedIndividual ;&#10;rdfs:label "Norman, 2013"@en ;&#10;dc:bibliographicCitation "Norman, D. (2013). The design of everyday things: Revised an..."@en ;&#10;dc:identifier &#60;https://mitpress.mit.edu/9780262640374/> .</code></pre>|

***
### MinorFail Assertion number 29

[Jump to summary definition](#summary-MinorFail-29)

:exclamation:MinorFail assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-signifiers/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL EL Profile incompatible|
|Description|Anonymous individuals are not supported|
|Pointer|<pre lang="Turtle"><code>&#60;https://purl.org/hmas/Affordance> a skos:Concept ;&#10;dc:references [ a owl:NamedIndividual ;&#10;rdfs:label "Chemero and Turvey, 2007"@en ;&#10;dc:bibliographicCitation "Chemero, A., & Turvey, M. T. (2007). Complexity, hypersets, ..."@en ;&#10;dc:identifier &#60;https://doi.org/10.1162/biot.2007.2.1.23> ],&#10;[ a owl:NamedIndividual ;&#10;rdfs:label "Norman, 2013"@en ;&#10;dc:bibliographicCitation "Norman, D. (2013). The design of everyday things: Revised an..."@en ;&#10;dc:identifier &#60;https://mitpress.mit.edu/9780262640374/> ], &#10; &#60;https://www.example.org/Noneb8129>, &#10; &#60;https://www.example.org/Noneb8130> ;&#10;rdfs:isDefinedBy &#60;https://purl.org/hmas/core> ;&#10;skos:definition "A behavior possibility that is a relationship between an abi..."@en ;&#10;skos:editorialNote "The concept has been considered as a candidate term for repr..."@en ;&#10;skos:historyNote "The definition of the concept follows affordance theorists [..."@en ;&#10;skos:prefLabel "affordance"@en ;&#10;skos:related &#60;https://purl.org/hmas/Signifier> .</code></pre>|

***
### MinorFail Assertion number 30

[Jump to summary definition](#summary-MinorFail-30)

:exclamation:MinorFail assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-signifiers/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL EL Profile incompatible|
|Description|Statement not supported|
|Pointer|<pre lang="Turtle"><code>&#60;https://purl.org/hmas/hasProfile> a owl:AsymmetricProperty,&#10;owl:ObjectProperty ;&#10;rdfs:label "has for profile"@en,&#10;"a pour profil"@fr ;&#10;rdfs:comment "A relation that links a resource to its profile."@en ;&#10;rdfs:isDefinedBy &#60;https://purl.org/hmas/core> ;&#10;rdfs:range &#60;https://purl.org/hmas/ResourceProfile> ;&#10;owl:inverseOf &#60;https://purl.org/hmas/isProfileOf> .</code></pre>|

***
### MinorFail Assertion number 31

[Jump to summary definition](#summary-MinorFail-31)

:exclamation:MinorFail assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-platforms|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-platforms/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-platforms/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|Domain out of vocabulary|
|Description|The property :isHostedOn has a domain out of the ontology: <https://purl.org/hmas/Hostable>|
|Pointer|<pre lang="Turtle"><code>:isHostedOn a owl:AsymmetricProperty,&#10;owl:ObjectProperty ;&#10;rdfs:label "is hosted on"@en,&#10;"est hébergé sur"@fr ;&#10;rdfs:comment "A relation that refers to the platform that hosts an informa..."@en,&#10;"A relation that refers to the platform that hosts the inform..."@en ;&#10;rdfs:domain :Hostable ;&#10;rdfs:isDefinedBy :core ;&#10;rdfs:range :HypermediaMASPlatform ;&#10;owl:inverseOf :hosts .</code></pre>|
|Pointer|https://purl.org/hmas/Hostable|

***
### MinorFail Assertion number 32

[Jump to summary definition](#summary-MinorFail-32)

:exclamation:MinorFail assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-platforms|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-platforms/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-platforms/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|Range out of vocabulary|
|Description|The property :hosts has a range out of the ontology: <https://purl.org/hmas/Hostable>|
|Pointer|<pre lang="Turtle"><code>:hosts a owl:AsymmetricProperty,&#10;owl:ObjectProperty ;&#10;rdfs:label "hosts"@en,&#10;"héberge"@fr ;&#10;dct:source &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/8#issuecomment-1025991719> ;&#10;rdfs:comment "A relation that refers to an information resource or a proce..."@en ;&#10;rdfs:domain :HypermediaMASPlatform ;&#10;rdfs:isDefinedBy :core ;&#10;rdfs:range :Hostable ;&#10;rdfs:seeAlso &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/18>, &#10; &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/49> ;&#10;owl:inverseOf :isHostedOn .</code></pre>|
|Pointer|https://purl.org/hmas/Hostable|

***
### MinorFail Assertion number 33

[Jump to summary definition](#summary-MinorFail-33)

:exclamation:MinorFail assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-platforms|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-platforms/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-platforms/onto.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|
|----|----|
|Title|Term labeling test|
|Description|A test case from the Best Practices tests checking if all the terms of the subject have a rdfs:label property pointing to a literal in English|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|Terms not labeled|
|Description|The term :core has no rdfs:label to define it in natural language|
|Pointer|<pre lang="Turtle"><code>:core a owl:Ontology ;&#10;cc:license &#60;https://creativecommons.org/licenses/by/4.0/> ;&#10;dct:contributor &#60;http://maxime-lefrancois.info/me#>, &#10; &#60;http://ns.inria.fr/fabien.gandon#me>, &#10; &#60;http://w3id.org/people/az/me>, &#10; &#60;https://danaivach.inrupt.net/profile/card#me>, &#10; &#60;https://id.inrupt.com/smnmyr>, &#10; &#60;https://orcid.org/0000-0002-2956-0533>, &#10; &#60;https://orcid.org/0000-0002-4506-2745>, &#10; &#60;https://orcid.org/0000-0003-0821-6095>, &#10; &#60;https://www.vcharpenay.link/#me> ;&#10;dct:creator &#60;https://id.inrupt.com/andreiciortea> ;&#10;dct:description "An ontology to describe Hypermedia Multi-Agent Systems."@en,&#10;"Une ontologie pour la description de systèmes multi-agents h..."@fr ;&#10;dct:issued "2021-11-21"^^xsd:date ;&#10;dct:title "Hypermedia MAS Core Ontology"@en,&#10;"Ontologie Centrale des SMA Hypermédias"@fr ;&#10;vann:preferredNamespacePrefix "hmas" ;&#10;vann:preferredNamespaceUri : .</code></pre>|

***
### MinorFail Assertion number 34

[Jump to summary definition](#summary-MinorFail-34)

:exclamation:MinorFail assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-platforms|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-platforms/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-platforms/onto.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|
|----|----|
|Title|Term labeling test|
|Description|A test case from the Best Practices tests checking if all the terms of the subject have a rdfs:label property pointing to a literal in English|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|Terms not labeled|
|Description|The term :Affordance has no rdfs:label to define it in natural language|
|Pointer|<pre lang="Turtle"><code>:Affordance a skos:Concept ;&#10;dct:references [ a owl:NamedIndividual ;&#10;rdfs:label "Chemero and Turvey, 2007"@en ;&#10;dct:bibliographicCitation "Chemero, A., & Turvey, M. T. (2007). Complexity, hypersets, ..."@en ;&#10;dct:identifier &#60;https://doi.org/10.1162/biot.2007.2.1.23> ],&#10;[ a owl:NamedIndividual ;&#10;rdfs:label "Norman, 2013"@en ;&#10;dct:bibliographicCitation "Norman, D. (2013). The design of everyday things: Revised an..."@en ;&#10;dct:identifier &#60;https://mitpress.mit.edu/9780262640374/> ] ;&#10;rdfs:isDefinedBy :core ;&#10;skos:definition "A behavior possibility that is a relationship between an abi..."@en ;&#10;skos:editorialNote "The concept has been considered as a candidate term for repr..."@en ;&#10;skos:historyNote "The definition of the concept follows affordance theorists [..."@en ;&#10;skos:prefLabel "affordance"@en ;&#10;skos:related :Signifier .</code></pre>|

***
### MinorFail Assertion number 35

[Jump to summary definition](#summary-MinorFail-35)

:exclamation:MinorFail assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-platforms|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-platforms/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-platforms/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL QL Profile incompatible|
|Description|Anonymous individuals are not supported|
|Pointer|<pre lang="Turtle"><code>[] a owl:NamedIndividual ;&#10;rdfs:label "Chemero and Turvey, 2007"@en ;&#10;dc:bibliographicCitation "Chemero, A., & Turvey, M. T. (2007). Complexity, hypersets, ..."@en ;&#10;dc:identifier &#60;https://doi.org/10.1162/biot.2007.2.1.23> .</code></pre>|

***
### MinorFail Assertion number 36

[Jump to summary definition](#summary-MinorFail-36)

:exclamation:MinorFail assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-platforms|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-platforms/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-platforms/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL QL Profile incompatible|
|Description|Anonymous individuals are not supported|
|Pointer|<pre lang="Turtle"><code>[] a owl:NamedIndividual ;&#10;rdfs:label "Norman, 2013"@en ;&#10;dc:bibliographicCitation "Norman, D. (2013). The design of everyday things: Revised an..."@en ;&#10;dc:identifier &#60;https://mitpress.mit.edu/9780262640374/> .</code></pre>|

***
### MinorFail Assertion number 37

[Jump to summary definition](#summary-MinorFail-37)

:exclamation:MinorFail assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-platforms|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-platforms/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-platforms/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL QL Profile incompatible|
|Description|Anonymous individuals are not supported|
|Pointer|<pre lang="Turtle"><code>&#60;https://purl.org/hmas/Affordance> a skos:Concept ;&#10;dc:references [ a owl:NamedIndividual ;&#10;rdfs:label "Chemero and Turvey, 2007"@en ;&#10;dc:bibliographicCitation "Chemero, A., & Turvey, M. T. (2007). Complexity, hypersets, ..."@en ;&#10;dc:identifier &#60;https://doi.org/10.1162/biot.2007.2.1.23> ],&#10;[ a owl:NamedIndividual ;&#10;rdfs:label "Norman, 2013"@en ;&#10;dc:bibliographicCitation "Norman, D. (2013). The design of everyday things: Revised an..."@en ;&#10;dc:identifier &#60;https://mitpress.mit.edu/9780262640374/> ] ;&#10;rdfs:isDefinedBy &#60;https://purl.org/hmas/core> ;&#10;skos:definition "A behavior possibility that is a relationship between an abi..."@en ;&#10;skos:editorialNote "The concept has been considered as a candidate term for repr..."@en ;&#10;skos:historyNote "The definition of the concept follows affordance theorists [..."@en ;&#10;skos:prefLabel "affordance"@en ;&#10;skos:related &#60;https://purl.org/hmas/Signifier> .</code></pre>|

***
### MinorFail Assertion number 38

[Jump to summary definition](#summary-MinorFail-38)

:exclamation:MinorFail assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-platforms|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-platforms/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-platforms/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL QL Profile incompatible|
|Description|Statement not supported|
|Pointer|<pre lang="Turtle"><code>&#60;https://purl.org/hmas/transitivelyContains> a owl:ObjectProperty,&#10;owl:TransitiveProperty ;&#10;rdfs:label "transitively contains"@en,&#10;"contient transitivement"@fr ;&#10;dc:source &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/8#issuecomment-1025991719> ;&#10;rdfs:comment "Links all the resources that are logically contained in a wo..."@en ;&#10;rdfs:domain &#60;https://purl.org/hmas/Workspace> ;&#10;rdfs:isDefinedBy &#60;https://purl.org/hmas/core> ;&#10;rdfs:seeAlso &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/18>, &#10; &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/39> ;&#10;owl:inverseOf &#60;https://purl.org/hmas/isTransitivelyContainedIn> .</code></pre>|

***
### MinorFail Assertion number 39

[Jump to summary definition](#summary-MinorFail-39)

:exclamation:MinorFail assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-platforms|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-platforms/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-platforms/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL EL Profile incompatible|
|Description|Anonymous individuals are not supported|
|Pointer|<pre lang="Turtle"><code>[] a owl:NamedIndividual ;&#10;rdfs:label "Chemero and Turvey, 2007"@en ;&#10;dc:bibliographicCitation "Chemero, A., & Turvey, M. T. (2007). Complexity, hypersets, ..."@en ;&#10;dc:identifier &#60;https://doi.org/10.1162/biot.2007.2.1.23> .</code></pre>|

***
### MinorFail Assertion number 40

[Jump to summary definition](#summary-MinorFail-40)

:exclamation:MinorFail assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-platforms|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-platforms/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-platforms/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL EL Profile incompatible|
|Description|Anonymous individuals are not supported|
|Pointer|<pre lang="Turtle"><code>[] a owl:NamedIndividual ;&#10;rdfs:label "Norman, 2013"@en ;&#10;dc:bibliographicCitation "Norman, D. (2013). The design of everyday things: Revised an..."@en ;&#10;dc:identifier &#60;https://mitpress.mit.edu/9780262640374/> .</code></pre>|

***
### MinorFail Assertion number 41

[Jump to summary definition](#summary-MinorFail-41)

:exclamation:MinorFail assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-platforms|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-platforms/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-platforms/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL EL Profile incompatible|
|Description|Anonymous individuals are not supported|
|Pointer|<pre lang="Turtle"><code>&#60;https://purl.org/hmas/Affordance> a skos:Concept ;&#10;dc:references [ a owl:NamedIndividual ;&#10;rdfs:label "Chemero and Turvey, 2007"@en ;&#10;dc:bibliographicCitation "Chemero, A., & Turvey, M. T. (2007). Complexity, hypersets, ..."@en ;&#10;dc:identifier &#60;https://doi.org/10.1162/biot.2007.2.1.23> ],&#10;[ a owl:NamedIndividual ;&#10;rdfs:label "Norman, 2013"@en ;&#10;dc:bibliographicCitation "Norman, D. (2013). The design of everyday things: Revised an..."@en ;&#10;dc:identifier &#60;https://mitpress.mit.edu/9780262640374/> ] ;&#10;rdfs:isDefinedBy &#60;https://purl.org/hmas/core> ;&#10;skos:definition "A behavior possibility that is a relationship between an abi..."@en ;&#10;skos:editorialNote "The concept has been considered as a candidate term for repr..."@en ;&#10;skos:historyNote "The definition of the concept follows affordance theorists [..."@en ;&#10;skos:prefLabel "affordance"@en ;&#10;skos:related &#60;https://purl.org/hmas/Signifier> .</code></pre>|

***
### MinorFail Assertion number 42

[Jump to summary definition](#summary-MinorFail-42)

:exclamation:MinorFail assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-platforms|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-platforms/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-platforms/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL EL Profile incompatible|
|Description|Statement not supported|
|Pointer|<pre lang="Turtle"><code>&#60;https://purl.org/hmas/hasProfile> a owl:AsymmetricProperty,&#10;owl:ObjectProperty ;&#10;rdfs:label "has for profile"@en,&#10;"a pour profil"@fr ;&#10;rdfs:comment "A relation that links a resource to its profile."@en ;&#10;rdfs:isDefinedBy &#60;https://purl.org/hmas/core> ;&#10;rdfs:range &#60;https://purl.org/hmas/ResourceProfile> ;&#10;owl:inverseOf &#60;https://purl.org/hmas/isProfileOf> .</code></pre>|

***
### MinorFail Assertion number 43

[Jump to summary definition](#summary-MinorFail-43)

:exclamation:MinorFail assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-organization|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-organization/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-organization/onto.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|
|----|----|
|Title|Term labeling test|
|Description|A test case from the Best Practices tests checking if all the terms of the subject have a rdfs:label property pointing to a literal in English|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|Terms not labeled|
|Description|The term :core has no rdfs:label to define it in natural language|
|Pointer|<pre lang="Turtle"><code>:core a owl:Ontology ;&#10;cc:license &#60;https://creativecommons.org/licenses/by/4.0/> ;&#10;dct:contributor &#60;http://maxime-lefrancois.info/me#>, &#10; &#60;http://ns.inria.fr/fabien.gandon#me>, &#10; &#60;http://w3id.org/people/az/me>, &#10; &#60;https://danaivach.inrupt.net/profile/card#me>, &#10; &#60;https://id.inrupt.com/smnmyr>, &#10; &#60;https://orcid.org/0000-0002-2956-0533>, &#10; &#60;https://orcid.org/0000-0002-4506-2745>, &#10; &#60;https://orcid.org/0000-0003-0821-6095>, &#10; &#60;https://www.vcharpenay.link/#me> ;&#10;dct:creator &#60;https://id.inrupt.com/andreiciortea> ;&#10;dct:description "An ontology to describe Hypermedia Multi-Agent Systems."@en,&#10;"Une ontologie pour la description de systèmes multi-agents h..."@fr ;&#10;dct:issued "2021-11-21"^^xsd:date ;&#10;dct:title "Hypermedia MAS Core Ontology"@en,&#10;"Ontologie Centrale des SMA Hypermédias"@fr ;&#10;vann:preferredNamespacePrefix "hmas" ;&#10;vann:preferredNamespaceUri : .</code></pre>|

***
### MinorFail Assertion number 44

[Jump to summary definition](#summary-MinorFail-44)

:exclamation:MinorFail assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-organization|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-organization/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-organization/onto.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|
|----|----|
|Title|Term labeling test|
|Description|A test case from the Best Practices tests checking if all the terms of the subject have a rdfs:label property pointing to a literal in English|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|Terms not labeled|
|Description|The term :Affordance has no rdfs:label to define it in natural language|
|Pointer|<pre lang="Turtle"><code>:Affordance a skos:Concept ;&#10;dct:references [ a owl:NamedIndividual ;&#10;rdfs:label "Chemero and Turvey, 2007"@en ;&#10;dct:bibliographicCitation "Chemero, A., & Turvey, M. T. (2007). Complexity, hypersets, ..."@en ;&#10;dct:identifier &#60;https://doi.org/10.1162/biot.2007.2.1.23> ],&#10;[ a owl:NamedIndividual ;&#10;rdfs:label "Norman, 2013"@en ;&#10;dct:bibliographicCitation "Norman, D. (2013). The design of everyday things: Revised an..."@en ;&#10;dct:identifier &#60;https://mitpress.mit.edu/9780262640374/> ] ;&#10;rdfs:isDefinedBy :core ;&#10;skos:definition "A behavior possibility that is a relationship between an abi..."@en ;&#10;skos:editorialNote "The concept has been considered as a candidate term for repr..."@en ;&#10;skos:historyNote "The definition of the concept follows affordance theorists [..."@en ;&#10;skos:prefLabel "affordance"@en ;&#10;skos:related :Signifier .</code></pre>|

***
### MinorFail Assertion number 45

[Jump to summary definition](#summary-MinorFail-45)

:exclamation:MinorFail assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-organization|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-organization/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL QL Profile incompatible|
|Description|Anonymous individuals are not supported|
|Pointer|<pre lang="Turtle"><code>[] a owl:NamedIndividual ;&#10;rdfs:label "Chemero and Turvey, 2007"@en ;&#10;dc:bibliographicCitation "Chemero, A., & Turvey, M. T. (2007). Complexity, hypersets, ..."@en ;&#10;dc:identifier &#60;https://doi.org/10.1162/biot.2007.2.1.23> .</code></pre>|

***
### MinorFail Assertion number 46

[Jump to summary definition](#summary-MinorFail-46)

:exclamation:MinorFail assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-organization|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-organization/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL QL Profile incompatible|
|Description|Anonymous individuals are not supported|
|Pointer|<pre lang="Turtle"><code>[] a owl:NamedIndividual ;&#10;rdfs:label "Norman, 2013"@en ;&#10;dc:bibliographicCitation "Norman, D. (2013). The design of everyday things: Revised an..."@en ;&#10;dc:identifier &#60;https://mitpress.mit.edu/9780262640374/> .</code></pre>|

***
### MinorFail Assertion number 47

[Jump to summary definition](#summary-MinorFail-47)

:exclamation:MinorFail assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-organization|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-organization/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL QL Profile incompatible|
|Description|Anonymous individuals are not supported|
|Pointer|<pre lang="Turtle"><code>&#60;https://purl.org/hmas/Affordance> a skos:Concept ;&#10;dc:references [ a owl:NamedIndividual ;&#10;rdfs:label "Chemero and Turvey, 2007"@en ;&#10;dc:bibliographicCitation "Chemero, A., & Turvey, M. T. (2007). Complexity, hypersets, ..."@en ;&#10;dc:identifier &#60;https://doi.org/10.1162/biot.2007.2.1.23> ],&#10;[ a owl:NamedIndividual ;&#10;rdfs:label "Norman, 2013"@en ;&#10;dc:bibliographicCitation "Norman, D. (2013). The design of everyday things: Revised an..."@en ;&#10;dc:identifier &#60;https://mitpress.mit.edu/9780262640374/> ] ;&#10;rdfs:isDefinedBy &#60;https://purl.org/hmas/core> ;&#10;skos:definition "A behavior possibility that is a relationship between an abi..."@en ;&#10;skos:editorialNote "The concept has been considered as a candidate term for repr..."@en ;&#10;skos:historyNote "The definition of the concept follows affordance theorists [..."@en ;&#10;skos:prefLabel "affordance"@en ;&#10;skos:related &#60;https://purl.org/hmas/Signifier> .</code></pre>|

***
### MinorFail Assertion number 48

[Jump to summary definition](#summary-MinorFail-48)

:exclamation:MinorFail assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-organization|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-organization/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL QL Profile incompatible|
|Description|Statement not supported|
|Pointer|<pre lang="Turtle"><code>&#60;https://purl.org/hmas/transitivelyContains> a owl:ObjectProperty,&#10;owl:TransitiveProperty ;&#10;rdfs:label "transitively contains"@en,&#10;"contient transitivement"@fr ;&#10;dc:source &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/8#issuecomment-1025991719> ;&#10;rdfs:comment "Links all the resources that are logically contained in a wo..."@en ;&#10;rdfs:domain &#60;https://purl.org/hmas/Workspace> ;&#10;rdfs:isDefinedBy &#60;https://purl.org/hmas/core> ;&#10;rdfs:seeAlso &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/18>, &#10; &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/39> ;&#10;owl:inverseOf &#60;https://purl.org/hmas/isTransitivelyContainedIn> .</code></pre>|

***
### MinorFail Assertion number 49

[Jump to summary definition](#summary-MinorFail-49)

:exclamation:MinorFail assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-organization|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-organization/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL EL Profile incompatible|
|Description|Anonymous individuals are not supported|
|Pointer|<pre lang="Turtle"><code>[] a owl:NamedIndividual ;&#10;rdfs:label "Chemero and Turvey, 2007"@en ;&#10;dc:bibliographicCitation "Chemero, A., & Turvey, M. T. (2007). Complexity, hypersets, ..."@en ;&#10;dc:identifier &#60;https://doi.org/10.1162/biot.2007.2.1.23> .</code></pre>|

***
### MinorFail Assertion number 50

[Jump to summary definition](#summary-MinorFail-50)

:exclamation:MinorFail assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-organization|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-organization/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL EL Profile incompatible|
|Description|Anonymous individuals are not supported|
|Pointer|<pre lang="Turtle"><code>[] a owl:NamedIndividual ;&#10;rdfs:label "Norman, 2013"@en ;&#10;dc:bibliographicCitation "Norman, D. (2013). The design of everyday things: Revised an..."@en ;&#10;dc:identifier &#60;https://mitpress.mit.edu/9780262640374/> .</code></pre>|

***
### MinorFail Assertion number 51

[Jump to summary definition](#summary-MinorFail-51)

:exclamation:MinorFail assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-organization|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-organization/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL EL Profile incompatible|
|Description|Anonymous individuals are not supported|
|Pointer|<pre lang="Turtle"><code>&#60;https://purl.org/hmas/Affordance> a skos:Concept ;&#10;dc:references [ a owl:NamedIndividual ;&#10;rdfs:label "Chemero and Turvey, 2007"@en ;&#10;dc:bibliographicCitation "Chemero, A., & Turvey, M. T. (2007). Complexity, hypersets, ..."@en ;&#10;dc:identifier &#60;https://doi.org/10.1162/biot.2007.2.1.23> ],&#10;[ a owl:NamedIndividual ;&#10;rdfs:label "Norman, 2013"@en ;&#10;dc:bibliographicCitation "Norman, D. (2013). The design of everyday things: Revised an..."@en ;&#10;dc:identifier &#60;https://mitpress.mit.edu/9780262640374/> ] ;&#10;rdfs:isDefinedBy &#60;https://purl.org/hmas/core> ;&#10;skos:definition "A behavior possibility that is a relationship between an abi..."@en ;&#10;skos:editorialNote "The concept has been considered as a candidate term for repr..."@en ;&#10;skos:historyNote "The definition of the concept follows affordance theorists [..."@en ;&#10;skos:prefLabel "affordance"@en ;&#10;skos:related &#60;https://purl.org/hmas/Signifier> .</code></pre>|

***
### MinorFail Assertion number 52

[Jump to summary definition](#summary-MinorFail-52)

:exclamation:MinorFail assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-organization|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-organization/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL EL Profile incompatible|
|Description|Statement not supported|
|Pointer|<pre lang="Turtle"><code>&#60;https://purl.org/hmas/hasProfile> a owl:AsymmetricProperty,&#10;owl:ObjectProperty ;&#10;rdfs:label "has for profile"@en,&#10;"a pour profil"@fr ;&#10;rdfs:comment "A relation that links a resource to its profile."@en ;&#10;rdfs:isDefinedBy &#60;https://purl.org/hmas/core> ;&#10;rdfs:range &#60;https://purl.org/hmas/ResourceProfile> ;&#10;owl:inverseOf &#60;https://purl.org/hmas/isProfileOf> .</code></pre>|

***
### MinorFail Assertion number 53

[Jump to summary definition](#summary-MinorFail-53)

:exclamation:MinorFail assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-core|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-core/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-core/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-core/onto.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|
|----|----|
|Title|Term labeling test|
|Description|A test case from the Best Practices tests checking if all the terms of the subject have a rdfs:label property pointing to a literal in English|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|Terms not labeled|
|Description|The term :core has no rdfs:label to define it in natural language|
|Pointer|<pre lang="Turtle"><code>:core a owl:Ontology ;&#10;cc:license &#60;https://creativecommons.org/licenses/by/4.0/> ;&#10;dct:contributor &#60;http://maxime-lefrancois.info/me#>, &#10; &#60;http://ns.inria.fr/fabien.gandon#me>, &#10; &#60;http://w3id.org/people/az/me>, &#10; &#60;https://danaivach.inrupt.net/profile/card#me>, &#10; &#60;https://id.inrupt.com/smnmyr>, &#10; &#60;https://orcid.org/0000-0002-2956-0533>, &#10; &#60;https://orcid.org/0000-0002-4506-2745>, &#10; &#60;https://orcid.org/0000-0003-0821-6095>, &#10; &#60;https://www.vcharpenay.link/#me> ;&#10;dct:creator &#60;https://id.inrupt.com/andreiciortea> ;&#10;dct:description "An ontology to describe Hypermedia Multi-Agent Systems."@en,&#10;"Une ontologie pour la description de systèmes multi-agents h..."@fr ;&#10;dct:issued "2021-11-21"^^xsd:date ;&#10;dct:title "Hypermedia MAS Core Ontology"@en,&#10;"Ontologie Centrale des SMA Hypermédias"@fr ;&#10;vann:preferredNamespacePrefix "hmas" ;&#10;vann:preferredNamespaceUri : .</code></pre>|

***
### MinorFail Assertion number 54

[Jump to summary definition](#summary-MinorFail-54)

:exclamation:MinorFail assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-core|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-core/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-core/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-core/onto.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|
|----|----|
|Title|Term labeling test|
|Description|A test case from the Best Practices tests checking if all the terms of the subject have a rdfs:label property pointing to a literal in English|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|Terms not labeled|
|Description|The term :Affordance has no rdfs:label to define it in natural language|
|Pointer|<pre lang="Turtle"><code>:Affordance a skos:Concept ;&#10;dct:references [ a owl:NamedIndividual ;&#10;rdfs:label "Chemero and Turvey, 2007"@en ;&#10;dct:bibliographicCitation "Chemero, A., & Turvey, M. T. (2007). Complexity, hypersets, ..."@en ;&#10;dct:identifier &#60;https://doi.org/10.1162/biot.2007.2.1.23> ],&#10;[ a owl:NamedIndividual ;&#10;rdfs:label "Norman, 2013"@en ;&#10;dct:bibliographicCitation "Norman, D. (2013). The design of everyday things: Revised an..."@en ;&#10;dct:identifier &#60;https://mitpress.mit.edu/9780262640374/> ] ;&#10;rdfs:isDefinedBy :core ;&#10;skos:definition "A behavior possibility that is a relationship between an abi..."@en ;&#10;skos:editorialNote "The concept has been considered as a candidate term for repr..."@en ;&#10;skos:historyNote "The definition of the concept follows affordance theorists [..."@en ;&#10;skos:prefLabel "affordance"@en ;&#10;skos:related :Signifier .</code></pre>|

***
### MinorFail Assertion number 55

[Jump to summary definition](#summary-MinorFail-55)

:exclamation:MinorFail assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-core|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-core/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-core/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-core/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL QL Profile incompatible|
|Description|Anonymous individuals are not supported|
|Pointer|<pre lang="Turtle"><code>[] a owl:NamedIndividual ;&#10;rdfs:label "Chemero and Turvey, 2007"@en ;&#10;dc:bibliographicCitation "Chemero, A., & Turvey, M. T. (2007). Complexity, hypersets, ..."@en ;&#10;dc:identifier &#60;https://doi.org/10.1162/biot.2007.2.1.23> .</code></pre>|

***
### MinorFail Assertion number 56

[Jump to summary definition](#summary-MinorFail-56)

:exclamation:MinorFail assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-core|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-core/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-core/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-core/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL QL Profile incompatible|
|Description|Anonymous individuals are not supported|
|Pointer|<pre lang="Turtle"><code>[] a owl:NamedIndividual ;&#10;rdfs:label "Norman, 2013"@en ;&#10;dc:bibliographicCitation "Norman, D. (2013). The design of everyday things: Revised an..."@en ;&#10;dc:identifier &#60;https://mitpress.mit.edu/9780262640374/> .</code></pre>|

***
### MinorFail Assertion number 57

[Jump to summary definition](#summary-MinorFail-57)

:exclamation:MinorFail assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-core|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-core/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-core/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-core/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL QL Profile incompatible|
|Description|Anonymous individuals are not supported|
|Pointer|<pre lang="Turtle"><code>&#60;https://purl.org/hmas/Affordance> a skos:Concept ;&#10;dc:references [ a owl:NamedIndividual ;&#10;rdfs:label "Chemero and Turvey, 2007"@en ;&#10;dc:bibliographicCitation "Chemero, A., & Turvey, M. T. (2007). Complexity, hypersets, ..."@en ;&#10;dc:identifier &#60;https://doi.org/10.1162/biot.2007.2.1.23> ],&#10;[ a owl:NamedIndividual ;&#10;rdfs:label "Norman, 2013"@en ;&#10;dc:bibliographicCitation "Norman, D. (2013). The design of everyday things: Revised an..."@en ;&#10;dc:identifier &#60;https://mitpress.mit.edu/9780262640374/> ] ;&#10;rdfs:isDefinedBy &#60;https://purl.org/hmas/core> ;&#10;skos:definition "A behavior possibility that is a relationship between an abi..."@en ;&#10;skos:editorialNote "The concept has been considered as a candidate term for repr..."@en ;&#10;skos:historyNote "The definition of the concept follows affordance theorists [..."@en ;&#10;skos:prefLabel "affordance"@en ;&#10;skos:related &#60;https://purl.org/hmas/Signifier> .</code></pre>|

***
### MinorFail Assertion number 58

[Jump to summary definition](#summary-MinorFail-58)

:exclamation:MinorFail assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-core|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-core/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-core/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-core/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL QL Profile incompatible|
|Description|Statement not supported|
|Pointer|<pre lang="Turtle"><code>&#60;https://purl.org/hmas/transitivelyContains> a owl:ObjectProperty,&#10;owl:TransitiveProperty ;&#10;rdfs:label "transitively contains"@en,&#10;"transitivelyContains"@en,&#10;"contient transitivement"@fr ;&#10;dc:source &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/8#issuecomment-1025991719> ;&#10;rdfs:comment "Links all the resources that are logically contained in a wo..."@en ;&#10;rdfs:domain &#60;https://purl.org/hmas/Workspace> ;&#10;rdfs:isDefinedBy &#60;https://purl.org/hmas/core> ;&#10;rdfs:seeAlso &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/18>, &#10; &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/39> ;&#10;owl:inverseOf &#60;https://purl.org/hmas/isTransitivelyContainedIn> .</code></pre>|

***
### MinorFail Assertion number 59

[Jump to summary definition](#summary-MinorFail-59)

:exclamation:MinorFail assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-core|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-core/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-core/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-core/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL EL Profile incompatible|
|Description|Anonymous individuals are not supported|
|Pointer|<pre lang="Turtle"><code>[] a owl:NamedIndividual ;&#10;rdfs:label "Chemero and Turvey, 2007"@en ;&#10;dc:bibliographicCitation "Chemero, A., & Turvey, M. T. (2007). Complexity, hypersets, ..."@en ;&#10;dc:identifier &#60;https://doi.org/10.1162/biot.2007.2.1.23> .</code></pre>|

***
### MinorFail Assertion number 60

[Jump to summary definition](#summary-MinorFail-60)

:exclamation:MinorFail assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-core|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-core/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-core/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-core/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL EL Profile incompatible|
|Description|Anonymous individuals are not supported|
|Pointer|<pre lang="Turtle"><code>[] a owl:NamedIndividual ;&#10;rdfs:label "Norman, 2013"@en ;&#10;dc:bibliographicCitation "Norman, D. (2013). The design of everyday things: Revised an..."@en ;&#10;dc:identifier &#60;https://mitpress.mit.edu/9780262640374/> .</code></pre>|

***
### MinorFail Assertion number 61

[Jump to summary definition](#summary-MinorFail-61)

:exclamation:MinorFail assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-core|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-core/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-core/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-core/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL EL Profile incompatible|
|Description|Anonymous individuals are not supported|
|Pointer|<pre lang="Turtle"><code>&#60;https://purl.org/hmas/Affordance> a skos:Concept ;&#10;dc:references [ a owl:NamedIndividual ;&#10;rdfs:label "Chemero and Turvey, 2007"@en ;&#10;dc:bibliographicCitation "Chemero, A., & Turvey, M. T. (2007). Complexity, hypersets, ..."@en ;&#10;dc:identifier &#60;https://doi.org/10.1162/biot.2007.2.1.23> ],&#10;[ a owl:NamedIndividual ;&#10;rdfs:label "Norman, 2013"@en ;&#10;dc:bibliographicCitation "Norman, D. (2013). The design of everyday things: Revised an..."@en ;&#10;dc:identifier &#60;https://mitpress.mit.edu/9780262640374/> ] ;&#10;rdfs:isDefinedBy &#60;https://purl.org/hmas/core> ;&#10;skos:definition "A behavior possibility that is a relationship between an abi..."@en ;&#10;skos:editorialNote "The concept has been considered as a candidate term for repr..."@en ;&#10;skos:historyNote "The definition of the concept follows affordance theorists [..."@en ;&#10;skos:prefLabel "affordance"@en ;&#10;skos:related &#60;https://purl.org/hmas/Signifier> .</code></pre>|

***
### MinorFail Assertion number 62

[Jump to summary definition](#summary-MinorFail-62)

:exclamation:MinorFail assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-core|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-core/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-core/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-core/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL EL Profile incompatible|
|Description|Statement not supported|
|Pointer|<pre lang="Turtle"><code>&#60;https://purl.org/hmas/hasProfile> a owl:AsymmetricProperty,&#10;owl:ObjectProperty ;&#10;rdfs:label "has for profile"@en,&#10;"has profile"@en,&#10;"a pour profil"@fr ;&#10;rdfs:comment "A relation that links a resource to its profile."@en ;&#10;rdfs:isDefinedBy &#60;https://purl.org/hmas/core> ;&#10;rdfs:range &#60;https://purl.org/hmas/ResourceProfile> ;&#10;owl:inverseOf &#60;https://purl.org/hmas/isProfileOf> .</code></pre>|

***
### MinorFail Assertion number 63

[Jump to summary definition](#summary-MinorFail-63)

:exclamation:MinorFail assertion
#### Subject detail
|Name|core|
|----|----|
|Title|Standalone module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|
|----|----|
|Title|Term labeling test|
|Description|A test case from the Best Practices tests checking if all the terms of the subject have a rdfs:label property pointing to a literal in English|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|Terms not labeled|
|Description|The term :core has no rdfs:label to define it in natural language|
|Pointer|<pre lang="Turtle"><code>:core a owl:Ontology ;&#10;cc:license &#60;https://creativecommons.org/licenses/by/4.0/> ;&#10;dct:contributor &#60;http://maxime-lefrancois.info/me#>, &#10; &#60;http://ns.inria.fr/fabien.gandon#me>, &#10; &#60;http://w3id.org/people/az/me>, &#10; &#60;https://danaivach.inrupt.net/profile/card#me>, &#10; &#60;https://id.inrupt.com/smnmyr>, &#10; &#60;https://orcid.org/0000-0002-2956-0533>, &#10; &#60;https://orcid.org/0000-0002-4506-2745>, &#10; &#60;https://orcid.org/0000-0003-0821-6095>, &#10; &#60;https://www.vcharpenay.link/#me> ;&#10;dct:creator &#60;https://id.inrupt.com/andreiciortea> ;&#10;dct:description "An ontology to describe Hypermedia Multi-Agent Systems."@en,&#10;"Une ontologie pour la description de systèmes multi-agents h..."@fr ;&#10;dct:issued "2021-11-21"^^xsd:date ;&#10;dct:title "Hypermedia MAS Core Ontology"@en,&#10;"Ontologie Centrale des SMA Hypermédias"@fr ;&#10;vann:preferredNamespacePrefix "hmas" ;&#10;vann:preferredNamespaceUri : .</code></pre>|

***
### MinorFail Assertion number 64

[Jump to summary definition](#summary-MinorFail-64)

:exclamation:MinorFail assertion
#### Subject detail
|Name|core|
|----|----|
|Title|Standalone module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|
|----|----|
|Title|Term labeling test|
|Description|A test case from the Best Practices tests checking if all the terms of the subject have a rdfs:label property pointing to a literal in English|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|Terms not labeled|
|Description|The term :Affordance has no rdfs:label to define it in natural language|
|Pointer|<pre lang="Turtle"><code>:Affordance a skos:Concept ;&#10;dct:references [ a owl:NamedIndividual ;&#10;rdfs:label "Chemero and Turvey, 2007"@en ;&#10;dct:bibliographicCitation "Chemero, A., & Turvey, M. T. (2007). Complexity, hypersets, ..."@en ;&#10;dct:identifier &#60;https://doi.org/10.1162/biot.2007.2.1.23> ],&#10;[ a owl:NamedIndividual ;&#10;rdfs:label "Norman, 2013"@en ;&#10;dct:bibliographicCitation "Norman, D. (2013). The design of everyday things: Revised an..."@en ;&#10;dct:identifier &#60;https://mitpress.mit.edu/9780262640374/> ] ;&#10;rdfs:isDefinedBy :core ;&#10;skos:definition "A behavior possibility that is a relationship between an abi..."@en ;&#10;skos:editorialNote "The concept has been considered as a candidate term for repr..."@en ;&#10;skos:historyNote "The definition of the concept follows affordance theorists [..."@en ;&#10;skos:prefLabel "affordance"@en ;&#10;skos:related :Signifier .</code></pre>|

***
### MinorFail Assertion number 65

[Jump to summary definition](#summary-MinorFail-65)

:exclamation:MinorFail assertion
#### Subject detail
|Name|core|
|----|----|
|Title|Standalone module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL QL Profile incompatible|
|Description|Anonymous individuals are not supported|
|Pointer|<pre lang="Turtle"><code>[] a owl:NamedIndividual ;&#10;rdfs:label "Chemero and Turvey, 2007"@en ;&#10;dc:bibliographicCitation "Chemero, A., & Turvey, M. T. (2007). Complexity, hypersets, ..."@en ;&#10;dc:identifier &#60;https://doi.org/10.1162/biot.2007.2.1.23> .</code></pre>|

***
### MinorFail Assertion number 66

[Jump to summary definition](#summary-MinorFail-66)

:exclamation:MinorFail assertion
#### Subject detail
|Name|core|
|----|----|
|Title|Standalone module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL QL Profile incompatible|
|Description|Anonymous individuals are not supported|
|Pointer|<pre lang="Turtle"><code>[] a owl:NamedIndividual ;&#10;rdfs:label "Norman, 2013"@en ;&#10;dc:bibliographicCitation "Norman, D. (2013). The design of everyday things: Revised an..."@en ;&#10;dc:identifier &#60;https://mitpress.mit.edu/9780262640374/> .</code></pre>|

***
### MinorFail Assertion number 67

[Jump to summary definition](#summary-MinorFail-67)

:exclamation:MinorFail assertion
#### Subject detail
|Name|core|
|----|----|
|Title|Standalone module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL QL Profile incompatible|
|Description|Anonymous individuals are not supported|
|Pointer|<pre lang="Turtle"><code>&#60;https://purl.org/hmas/Affordance> a skos:Concept ;&#10;dc:references [ a owl:NamedIndividual ;&#10;rdfs:label "Chemero and Turvey, 2007"@en ;&#10;dc:bibliographicCitation "Chemero, A., & Turvey, M. T. (2007). Complexity, hypersets, ..."@en ;&#10;dc:identifier &#60;https://doi.org/10.1162/biot.2007.2.1.23> ],&#10;[ a owl:NamedIndividual ;&#10;rdfs:label "Norman, 2013"@en ;&#10;dc:bibliographicCitation "Norman, D. (2013). The design of everyday things: Revised an..."@en ;&#10;dc:identifier &#60;https://mitpress.mit.edu/9780262640374/> ] ;&#10;rdfs:isDefinedBy &#60;https://purl.org/hmas/core> ;&#10;skos:definition "A behavior possibility that is a relationship between an abi..."@en ;&#10;skos:editorialNote "The concept has been considered as a candidate term for repr..."@en ;&#10;skos:historyNote "The definition of the concept follows affordance theorists [..."@en ;&#10;skos:prefLabel "affordance"@en ;&#10;skos:related &#60;https://purl.org/hmas/Signifier> .</code></pre>|

***
### MinorFail Assertion number 68

[Jump to summary definition](#summary-MinorFail-68)

:exclamation:MinorFail assertion
#### Subject detail
|Name|core|
|----|----|
|Title|Standalone module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL QL Profile incompatible|
|Description|Statement not supported|
|Pointer|<pre lang="Turtle"><code>&#60;https://purl.org/hmas/transitivelyContains> a owl:ObjectProperty,&#10;owl:TransitiveProperty ;&#10;rdfs:label "transitively contains"@en,&#10;"contient transitivement"@fr ;&#10;dc:source &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/8#issuecomment-1025991719> ;&#10;rdfs:comment "Links all the resources that are logically contained in a wo..."@en ;&#10;rdfs:domain &#60;https://purl.org/hmas/Workspace> ;&#10;rdfs:isDefinedBy &#60;https://purl.org/hmas/core> ;&#10;rdfs:seeAlso &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/18>, &#10; &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/39> ;&#10;owl:inverseOf &#60;https://purl.org/hmas/isTransitivelyContainedIn> .</code></pre>|

***
### MinorFail Assertion number 69

[Jump to summary definition](#summary-MinorFail-69)

:exclamation:MinorFail assertion
#### Subject detail
|Name|core|
|----|----|
|Title|Standalone module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL EL Profile incompatible|
|Description|Anonymous individuals are not supported|
|Pointer|<pre lang="Turtle"><code>[] a owl:NamedIndividual ;&#10;rdfs:label "Chemero and Turvey, 2007"@en ;&#10;dc:bibliographicCitation "Chemero, A., & Turvey, M. T. (2007). Complexity, hypersets, ..."@en ;&#10;dc:identifier &#60;https://doi.org/10.1162/biot.2007.2.1.23> .</code></pre>|

***
### MinorFail Assertion number 70

[Jump to summary definition](#summary-MinorFail-70)

:exclamation:MinorFail assertion
#### Subject detail
|Name|core|
|----|----|
|Title|Standalone module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL EL Profile incompatible|
|Description|Anonymous individuals are not supported|
|Pointer|<pre lang="Turtle"><code>[] a owl:NamedIndividual ;&#10;rdfs:label "Norman, 2013"@en ;&#10;dc:bibliographicCitation "Norman, D. (2013). The design of everyday things: Revised an..."@en ;&#10;dc:identifier &#60;https://mitpress.mit.edu/9780262640374/> .</code></pre>|

***
### MinorFail Assertion number 71

[Jump to summary definition](#summary-MinorFail-71)

:exclamation:MinorFail assertion
#### Subject detail
|Name|core|
|----|----|
|Title|Standalone module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL EL Profile incompatible|
|Description|Anonymous individuals are not supported|
|Pointer|<pre lang="Turtle"><code>&#60;https://purl.org/hmas/Affordance> a skos:Concept ;&#10;dc:references [ a owl:NamedIndividual ;&#10;rdfs:label "Chemero and Turvey, 2007"@en ;&#10;dc:bibliographicCitation "Chemero, A., & Turvey, M. T. (2007). Complexity, hypersets, ..."@en ;&#10;dc:identifier &#60;https://doi.org/10.1162/biot.2007.2.1.23> ],&#10;[ a owl:NamedIndividual ;&#10;rdfs:label "Norman, 2013"@en ;&#10;dc:bibliographicCitation "Norman, D. (2013). The design of everyday things: Revised an..."@en ;&#10;dc:identifier &#60;https://mitpress.mit.edu/9780262640374/> ] ;&#10;rdfs:isDefinedBy &#60;https://purl.org/hmas/core> ;&#10;skos:definition "A behavior possibility that is a relationship between an abi..."@en ;&#10;skos:editorialNote "The concept has been considered as a candidate term for repr..."@en ;&#10;skos:historyNote "The definition of the concept follows affordance theorists [..."@en ;&#10;skos:prefLabel "affordance"@en ;&#10;skos:related &#60;https://purl.org/hmas/Signifier> .</code></pre>|

***
### MinorFail Assertion number 72

[Jump to summary definition](#summary-MinorFail-72)

:exclamation:MinorFail assertion
#### Subject detail
|Name|core|
|----|----|
|Title|Standalone module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL EL Profile incompatible|
|Description|Statement not supported|
|Pointer|<pre lang="Turtle"><code>&#60;https://purl.org/hmas/hasProfile> a owl:AsymmetricProperty,&#10;owl:ObjectProperty ;&#10;rdfs:label "has for profile"@en,&#10;"a pour profil"@fr ;&#10;rdfs:comment "A relation that links a resource to its profile."@en ;&#10;rdfs:isDefinedBy &#60;https://purl.org/hmas/core> ;&#10;rdfs:range &#60;https://purl.org/hmas/ResourceProfile> ;&#10;owl:inverseOf &#60;https://purl.org/hmas/isProfileOf> .</code></pre>|

***
### MinorFail Assertion number 73

[Jump to summary definition](#summary-MinorFail-73)

:exclamation:MinorFail assertion
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All the modules from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages that are syntaxically correct as well as their recursive imports|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|
|----|----|
|Title|Term labeling test|
|Description|A test case from the Best Practices tests checking if all the terms of the subject have a rdfs:label property pointing to a literal in English|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|Terms not labeled|
|Description|The term :core has no rdfs:label to define it in natural language|
|Pointer|<pre lang="Turtle"><code>:core a owl:Ontology ;&#10;cc:license &#60;https://creativecommons.org/licenses/by/4.0/> ;&#10;dct:contributor &#60;http://maxime-lefrancois.info/me#>, &#10; &#60;http://ns.inria.fr/fabien.gandon#me>, &#10; &#60;http://w3id.org/people/az/me>, &#10; &#60;https://danaivach.inrupt.net/profile/card#me>, &#10; &#60;https://id.inrupt.com/smnmyr>, &#10; &#60;https://orcid.org/0000-0002-2956-0533>, &#10; &#60;https://orcid.org/0000-0002-4506-2745>, &#10; &#60;https://orcid.org/0000-0003-0821-6095>, &#10; &#60;https://www.vcharpenay.link/#me> ;&#10;dct:creator &#60;https://id.inrupt.com/andreiciortea> ;&#10;dct:description "An ontology to describe Hypermedia Multi-Agent Systems."@en,&#10;"Une ontologie pour la description de systèmes multi-agents h..."@fr ;&#10;dct:issued "2021-11-21"^^xsd:date ;&#10;dct:title "Hypermedia MAS Core Ontology"@en,&#10;"Ontologie Centrale des SMA Hypermédias"@fr ;&#10;vann:preferredNamespacePrefix "hmas" ;&#10;vann:preferredNamespaceUri : .</code></pre>|

***
### MinorFail Assertion number 74

[Jump to summary definition](#summary-MinorFail-74)

:exclamation:MinorFail assertion
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All the modules from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages that are syntaxically correct as well as their recursive imports|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|
|----|----|
|Title|Term labeling test|
|Description|A test case from the Best Practices tests checking if all the terms of the subject have a rdfs:label property pointing to a literal in English|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|Terms not labeled|
|Description|The term :interaction has no rdfs:label to define it in natural language|
|Pointer|<pre lang="Turtle"><code>:interaction a owl:Ontology ;&#10;cc:license &#60;https://creativecommons.org/licenses/by/4.0/> ;&#10;dct:contributor &#60;http://ns.inria.fr/fabien.gandon#me>, &#10; &#60;https://pod.inrupt.com/andreiciortea/profile/card#me>, &#10; &#60;https://pod.inrupt.com/smnmyr/profile/card#me> ;&#10;dct:creator &#60;https://danaivach.inrupt.net/profile/card#me> ;&#10;dct:description "An ontology to describe interaction in Hypermedia Multi-Agen..."@en,&#10;"L'ontologie pour décrire l'interaction dans les systèmes mul..."@fr ;&#10;dct:issued "2023-01-13"^^xsd:date ;&#10;dct:title "Hypermedia MAS Interaction Ontology"@en,&#10;"Ontologie d'Interaction des SMA Hypermédias"@fr ;&#10;vann:preferredNamespacePrefix "hmas" ;&#10;vann:preferredNamespaceUri : ;&#10;owl:imports :core .</code></pre>|

***
### MinorFail Assertion number 75

[Jump to summary definition](#summary-MinorFail-75)

:exclamation:MinorFail assertion
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All the modules from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages that are syntaxically correct as well as their recursive imports|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|
|----|----|
|Title|Term labeling test|
|Description|A test case from the Best Practices tests checking if all the terms of the subject have a rdfs:label property pointing to a literal in English|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|Terms not labeled|
|Description|The term :regulation has no rdfs:label to define it in natural language|
|Pointer|<pre lang="Turtle"><code>:regulation a owl:Ontology ;&#10;cc:license &#60;https://creativecommons.org/licenses/by/4.0/> ;&#10;dct:contributor &#60;http://maxime-lefrancois.info/me#>, &#10; &#60;http://ns.inria.fr/fabien.gandon#me>, &#10; &#60;https://danaivach.inrupt.net/profile/card#me>, &#10; &#60;https://orcid.org/0000-0002-2956-0533>, &#10; &#60;https://orcid.org/0000-0002-3497-8758>, &#10; &#60;https://orcid.org/0000-0003-0821-6095>, &#10; &#60;https://orcid.org/0000-0003-4509-9537> ;&#10;dct:creator &#60;https://orcid.org/0000-0002-4506-2745> ;&#10;dct:description "An ontology to describe the regulation of Hypermedia Multi-A..."@en,&#10;"L'ontologie pour décrire la régulation des systèmes multi-ag..."@fr ;&#10;dct:issued "2022-05-01"^^xsd:date ;&#10;dct:title "Hypermedia MAS Regulation Ontology"@en,&#10;"Ontologie de Régulation des SMA Hypermédias"@fr ;&#10;vann:preferredNamespacePrefix "hmas" ;&#10;vann:preferredNamespaceUri : ;&#10;owl:imports :core .</code></pre>|

***
### MinorFail Assertion number 76

[Jump to summary definition](#summary-MinorFail-76)

:exclamation:MinorFail assertion
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All the modules from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages that are syntaxically correct as well as their recursive imports|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|
|----|----|
|Title|Term labeling test|
|Description|A test case from the Best Practices tests checking if all the terms of the subject have a rdfs:label property pointing to a literal in English|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|Terms not labeled|
|Description|The term :Affordance has no rdfs:label to define it in natural language|
|Pointer|<pre lang="Turtle"><code>:Affordance a skos:Concept ;&#10;dct:references [ a owl:NamedIndividual ;&#10;rdfs:label "Chemero and Turvey, 2007"@en ;&#10;dct:bibliographicCitation "Chemero, A., & Turvey, M. T. (2007). Complexity, hypersets, ..."@en ;&#10;dct:identifier &#60;https://doi.org/10.1162/biot.2007.2.1.23> ],&#10;[ a owl:NamedIndividual ;&#10;rdfs:label "Norman, 2013"@en ;&#10;dct:bibliographicCitation "Norman, D. (2013). The design of everyday things: Revised an..."@en ;&#10;dct:identifier &#60;https://mitpress.mit.edu/9780262640374/> ] ;&#10;rdfs:isDefinedBy :core ;&#10;skos:definition "A behavior possibility that is a relationship between an abi..."@en ;&#10;skos:editorialNote "The concept has been considered as a candidate term for repr..."@en ;&#10;skos:historyNote "The definition of the concept follows affordance theorists [..."@en ;&#10;skos:prefLabel "affordance"@en ;&#10;skos:related :Signifier .</code></pre>|

***
### MinorFail Assertion number 77

[Jump to summary definition](#summary-MinorFail-77)

:exclamation:MinorFail assertion
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All the modules from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages that are syntaxically correct as well as their recursive imports|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL QL Profile incompatible|
|Description|Anonymous individuals are not supported|
|Pointer|<pre lang="Turtle"><code>[] a owl:NamedIndividual ;&#10;rdfs:label "Chemero and Turvey, 2007"@en ;&#10;dc:bibliographicCitation "Chemero, A., & Turvey, M. T. (2007). Complexity, hypersets, ..."@en ;&#10;dc:identifier &#60;https://doi.org/10.1162/biot.2007.2.1.23> .</code></pre>|

***
### MinorFail Assertion number 78

[Jump to summary definition](#summary-MinorFail-78)

:exclamation:MinorFail assertion
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All the modules from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages that are syntaxically correct as well as their recursive imports|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL QL Profile incompatible|
|Description|Anonymous individuals are not supported|
|Pointer|<pre lang="Turtle"><code>[] a owl:NamedIndividual ;&#10;rdfs:label "Norman, 2013"@en ;&#10;dc:bibliographicCitation "Norman, D. (2013). The design of everyday things: Revised an..."@en ;&#10;dc:identifier &#60;https://mitpress.mit.edu/9780262640374/> .</code></pre>|

***
### MinorFail Assertion number 79

[Jump to summary definition](#summary-MinorFail-79)

:exclamation:MinorFail assertion
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All the modules from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages that are syntaxically correct as well as their recursive imports|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL QL Profile incompatible|
|Description|Anonymous individuals are not supported|
|Pointer|<pre lang="Turtle"><code>&#60;https://purl.org/hmas/Affordance> a skos:Concept ;&#10;dc:references [ a owl:NamedIndividual ;&#10;rdfs:label "Chemero and Turvey, 2007"@en ;&#10;dc:bibliographicCitation "Chemero, A., & Turvey, M. T. (2007). Complexity, hypersets, ..."@en ;&#10;dc:identifier &#60;https://doi.org/10.1162/biot.2007.2.1.23> ],&#10;[ a owl:NamedIndividual ;&#10;rdfs:label "Norman, 2013"@en ;&#10;dc:bibliographicCitation "Norman, D. (2013). The design of everyday things: Revised an..."@en ;&#10;dc:identifier &#60;https://mitpress.mit.edu/9780262640374/> ] ;&#10;rdfs:isDefinedBy &#60;https://purl.org/hmas/core> ;&#10;skos:definition "A behavior possibility that is a relationship between an abi..."@en ;&#10;skos:editorialNote "The concept has been considered as a candidate term for repr..."@en ;&#10;skos:historyNote "The definition of the concept follows affordance theorists [..."@en ;&#10;skos:prefLabel "affordance"@en ;&#10;skos:related &#60;https://purl.org/hmas/Signifier> .</code></pre>|

***
### MinorFail Assertion number 80

[Jump to summary definition](#summary-MinorFail-80)

:exclamation:MinorFail assertion
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All the modules from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages that are syntaxically correct as well as their recursive imports|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL QL Profile incompatible|
|Description|Statement not supported|
|Pointer|<pre lang="Turtle"><code>&#60;https://purl.org/hmas/transitivelyContains> a owl:ObjectProperty,&#10;owl:TransitiveProperty ;&#10;rdfs:label "transitively contains"@en,&#10;"contient transitivement"@fr ;&#10;dc:source &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/8#issuecomment-1025991719> ;&#10;rdfs:comment "Links all the resources that are logically contained in a wo..."@en ;&#10;rdfs:domain &#60;https://purl.org/hmas/Workspace> ;&#10;rdfs:isDefinedBy &#60;https://purl.org/hmas/core> ;&#10;rdfs:seeAlso &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/18>, &#10; &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/39> ;&#10;owl:inverseOf &#60;https://purl.org/hmas/isTransitivelyContainedIn> .</code></pre>|

***
### MinorFail Assertion number 81

[Jump to summary definition](#summary-MinorFail-81)

:exclamation:MinorFail assertion
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All the modules from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages that are syntaxically correct as well as their recursive imports|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL EL Profile incompatible|
|Description|Anonymous individuals are not supported|
|Pointer|<pre lang="Turtle"><code>[] a owl:NamedIndividual ;&#10;rdfs:label "Chemero and Turvey, 2007"@en ;&#10;dc:bibliographicCitation "Chemero, A., & Turvey, M. T. (2007). Complexity, hypersets, ..."@en ;&#10;dc:identifier &#60;https://doi.org/10.1162/biot.2007.2.1.23> .</code></pre>|

***
### MinorFail Assertion number 82

[Jump to summary definition](#summary-MinorFail-82)

:exclamation:MinorFail assertion
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All the modules from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages that are syntaxically correct as well as their recursive imports|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL EL Profile incompatible|
|Description|Anonymous individuals are not supported|
|Pointer|<pre lang="Turtle"><code>[] a owl:NamedIndividual ;&#10;rdfs:label "Norman, 2013"@en ;&#10;dc:bibliographicCitation "Norman, D. (2013). The design of everyday things: Revised an..."@en ;&#10;dc:identifier &#60;https://mitpress.mit.edu/9780262640374/> .</code></pre>|

***
### MinorFail Assertion number 83

[Jump to summary definition](#summary-MinorFail-83)

:exclamation:MinorFail assertion
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All the modules from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages that are syntaxically correct as well as their recursive imports|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL EL Profile incompatible|
|Description|Anonymous individuals are not supported|
|Pointer|<pre lang="Turtle"><code>&#60;https://purl.org/hmas/Affordance> a skos:Concept ;&#10;dc:references [ a owl:NamedIndividual ;&#10;rdfs:label "Chemero and Turvey, 2007"@en ;&#10;dc:bibliographicCitation "Chemero, A., & Turvey, M. T. (2007). Complexity, hypersets, ..."@en ;&#10;dc:identifier &#60;https://doi.org/10.1162/biot.2007.2.1.23> ],&#10;[ a owl:NamedIndividual ;&#10;rdfs:label "Norman, 2013"@en ;&#10;dc:bibliographicCitation "Norman, D. (2013). The design of everyday things: Revised an..."@en ;&#10;dc:identifier &#60;https://mitpress.mit.edu/9780262640374/> ] ;&#10;rdfs:isDefinedBy &#60;https://purl.org/hmas/core> ;&#10;skos:definition "A behavior possibility that is a relationship between an abi..."@en ;&#10;skos:editorialNote "The concept has been considered as a candidate term for repr..."@en ;&#10;skos:historyNote "The definition of the concept follows affordance theorists [..."@en ;&#10;skos:prefLabel "affordance"@en ;&#10;skos:related &#60;https://purl.org/hmas/Signifier> .</code></pre>|

***
### MinorFail Assertion number 84

[Jump to summary definition](#summary-MinorFail-84)

:exclamation:MinorFail assertion
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All the modules from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages that are syntaxically correct as well as their recursive imports|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL EL Profile incompatible|
|Description|Statement not supported|
|Pointer|<pre lang="Turtle"><code>&#60;https://purl.org/hmas/hasProfile> a owl:AsymmetricProperty,&#10;owl:ObjectProperty ;&#10;rdfs:label "has for profile"@en,&#10;"a pour profil"@fr ;&#10;rdfs:comment "A relation that links a resource to its profile."@en ;&#10;rdfs:isDefinedBy &#60;https://purl.org/hmas/core> ;&#10;rdfs:range &#60;https://purl.org/hmas/ResourceProfile> ;&#10;owl:inverseOf &#60;https://purl.org/hmas/isProfileOf> .</code></pre>|

***
### MinorFail Assertion number 85

[Jump to summary definition](#summary-MinorFail-85)

:exclamation:MinorFail assertion
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All the modules from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages that are syntaxically correct as well as their recursive imports|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#terms-differenciation)|
|----|----|
|Title|Terms differenciation test|
|Description|A test case from the Best Practices tests checking if all the terms are different enough from each other according to the Levenshtein distance metric.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|Too close terms|
|Description|The following terms are too similar: :core and :Role|
|Pointer|<pre lang="Turtle"><code>:core a owl:Ontology ;&#10;cc:license &#60;https://creativecommons.org/licenses/by/4.0/> ;&#10;dct:contributor &#60;http://maxime-lefrancois.info/me#>, &#10; &#60;http://ns.inria.fr/fabien.gandon#me>, &#10; &#60;http://w3id.org/people/az/me>, &#10; &#60;https://danaivach.inrupt.net/profile/card#me>, &#10; &#60;https://id.inrupt.com/smnmyr>, &#10; &#60;https://orcid.org/0000-0002-2956-0533>, &#10; &#60;https://orcid.org/0000-0002-4506-2745>, &#10; &#60;https://orcid.org/0000-0003-0821-6095>, &#10; &#60;https://www.vcharpenay.link/#me> ;&#10;dct:creator &#60;https://id.inrupt.com/andreiciortea> ;&#10;dct:description "An ontology to describe Hypermedia Multi-Agent Systems."@en,&#10;"Une ontologie pour la description de systèmes multi-agents h..."@fr ;&#10;dct:issued "2021-11-21"^^xsd:date ;&#10;dct:title "Hypermedia MAS Core Ontology"@en,&#10;"Ontologie Centrale des SMA Hypermédias"@fr ;&#10;vann:preferredNamespacePrefix "hmas" ;&#10;vann:preferredNamespaceUri : .</code></pre>|
|Pointer|<pre lang="Turtle"><code>:Role a owl:Class ;&#10;rdfs:label "role"@en,&#10;"rôle"@fr ;&#10;rdfs:comment "A Role defines positions of members (i.e., Agents) in an Org..."@en ;&#10;rdfs:isDefinedBy :regulation .</code></pre>|

***
### MinorFail Assertion number 86

[Jump to summary definition](#summary-MinorFail-86)

:exclamation:MinorFail assertion
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All the modules from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages that are syntaxically correct as well as their recursive imports|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#terms-differenciation)|
|----|----|
|Title|Terms differenciation test|
|Description|A test case from the Best Practices tests checking if all the terms are different enough from each other according to the Levenshtein distance metric.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|Too close terms|
|Description|The following terms are too similar: :isMembershipOf and :isMembershipIn|
|Pointer|<pre lang="Turtle"><code>:isMembershipOf a owl:ObjectProperty ;&#10;rdfs:label "is membership of"@en,&#10;"est l'appartenance à"@fr ;&#10;rdfs:comment "A relation that refers to the Agent involved in a Membership..."@en ;&#10;rdfs:domain :Membership ;&#10;rdfs:isDefinedBy :regulation ;&#10;rdfs:range :Agent .</code></pre>|
|Pointer|<pre lang="Turtle"><code>:isMembershipIn a owl:ObjectProperty ;&#10;rdfs:label "is membership in"@en,&#10;"est l'appartenance à"@fr ;&#10;rdfs:comment "A relation that refers to the Group involved in a Membership..."@en ;&#10;rdfs:domain :Membership ;&#10;rdfs:isDefinedBy :regulation ;&#10;rdfs:range :Group .</code></pre>|

***
### MinorFail Assertion number 87

[Jump to summary definition](#summary-MinorFail-87)

:exclamation:MinorFail assertion
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All the modules from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages that are syntaxically correct as well as their recursive imports|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#terms-differenciation)|
|----|----|
|Title|Terms differenciation test|
|Description|A test case from the Best Practices tests checking if all the terms are different enough from each other according to the Levenshtein distance metric.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|Too close terms|
|Description|The following terms are too similar: :signifies and :Signifier|
|Pointer|<pre lang="Turtle"><code>:signifies a owl:ObjectProperty ;&#10;rdfs:label "signifies"@en,&#10;"signifie"@fr ;&#10;rdfs:comment "A relation between a signifier and the specification of a be..."@en ;&#10;rdfs:domain :Signifier ;&#10;rdfs:isDefinedBy :interaction .</code></pre>|
|Pointer|<pre lang="Turtle"><code>:Signifier a owl:Class ;&#10;rdfs:label "signifier"@en,&#10;"signifiant"@fr ;&#10;rdfs:comment "A perceivable sign/cue that can be interpreted meaningfully ..."@en ;&#10;rdfs:isDefinedBy :core ;&#10;rdfs:seeAlso &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/13#issuecomment-1028904491>, &#10; &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/41> ;&#10;skos:note ":Signifier works as a bridge between the Core and the Intera..."@en ;&#10;skos:related :Affordance .</code></pre>|

***
### MinorFail Assertion number 88

[Jump to summary definition](#summary-MinorFail-88)

:exclamation:MinorFail assertion
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All the fragments from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages that are syntaxically correct as well as their recursive imports|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)<br/>- [Modelet domain-template/scenario-template/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/domain-template/scenario-template/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-behavior-specifications/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-core/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Modelet logistics/create-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/create-organization/onto.ttl)<br/>- [Modelet logistics/structure-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|Domain out of vocabulary|
|Description|The property :isHostedOn has a domain out of the ontology: <https://purl.org/hmas/Hostable>|
|Pointer|<pre lang="Turtle"><code>:isHostedOn a owl:AsymmetricProperty,&#10;owl:ObjectProperty ;&#10;rdfs:label "is hosted on"@en,&#10;"est hébergé sur"@fr ;&#10;rdfs:comment "A relation that refers to the platform that hosts an informa..."@en,&#10;"A relation that refers to the platform that hosts the inform..."@en ;&#10;rdfs:domain :Hostable ;&#10;rdfs:isDefinedBy :core ;&#10;rdfs:range :HypermediaMASPlatform ;&#10;owl:inverseOf :hosts .</code></pre>|
|Pointer|https://purl.org/hmas/Hostable|

***
### MinorFail Assertion number 89

[Jump to summary definition](#summary-MinorFail-89)

:exclamation:MinorFail assertion
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All the fragments from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages that are syntaxically correct as well as their recursive imports|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)<br/>- [Modelet domain-template/scenario-template/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/domain-template/scenario-template/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-behavior-specifications/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-core/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Modelet logistics/create-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/create-organization/onto.ttl)<br/>- [Modelet logistics/structure-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|Range out of vocabulary|
|Description|The property :hosts has a range out of the ontology: <https://purl.org/hmas/Hostable>|
|Pointer|<pre lang="Turtle"><code>:hosts a owl:AsymmetricProperty,&#10;owl:ObjectProperty ;&#10;rdfs:label "hosts"@en,&#10;"héberge"@fr ;&#10;dct:source &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/8#issuecomment-1025991719> ;&#10;rdfs:comment "A relation that refers to an information resource or a proce..."@en ;&#10;rdfs:domain :HypermediaMASPlatform ;&#10;rdfs:isDefinedBy :core ;&#10;rdfs:range :Hostable ;&#10;rdfs:seeAlso &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/18>, &#10; &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/49> ;&#10;owl:inverseOf :isHostedOn .</code></pre>|
|Pointer|https://purl.org/hmas/Hostable|

***
### MinorFail Assertion number 90

[Jump to summary definition](#summary-MinorFail-90)

:exclamation:MinorFail assertion
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All the fragments from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages that are syntaxically correct as well as their recursive imports|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)<br/>- [Modelet domain-template/scenario-template/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/domain-template/scenario-template/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-behavior-specifications/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-core/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Modelet logistics/create-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/create-organization/onto.ttl)<br/>- [Modelet logistics/structure-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|
|----|----|
|Title|Term labeling test|
|Description|A test case from the Best Practices tests checking if all the terms of the subject have a rdfs:label property pointing to a literal in English|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|Terms not labeled|
|Description|The term :core has no rdfs:label to define it in natural language|
|Pointer|<pre lang="Turtle"><code>:core a owl:Ontology ;&#10;cc:license &#60;https://creativecommons.org/licenses/by/4.0/> ;&#10;dct:contributor &#60;http://maxime-lefrancois.info/me#>, &#10; &#60;http://ns.inria.fr/fabien.gandon#me>, &#10; &#60;http://w3id.org/people/az/me>, &#10; &#60;https://danaivach.inrupt.net/profile/card#me>, &#10; &#60;https://id.inrupt.com/smnmyr>, &#10; &#60;https://orcid.org/0000-0002-2956-0533>, &#10; &#60;https://orcid.org/0000-0002-4506-2745>, &#10; &#60;https://orcid.org/0000-0003-0821-6095>, &#10; &#60;https://www.vcharpenay.link/#me> ;&#10;dct:creator &#60;https://id.inrupt.com/andreiciortea> ;&#10;dct:description "An ontology to describe Hypermedia Multi-Agent Systems."@en,&#10;"Une ontologie pour la description de systèmes multi-agents h..."@fr ;&#10;dct:issued "2021-11-21"^^xsd:date ;&#10;dct:title "Hypermedia MAS Core Ontology"@en,&#10;"Ontologie Centrale des SMA Hypermédias"@fr ;&#10;vann:preferredNamespacePrefix "hmas" ;&#10;vann:preferredNamespaceUri : .</code></pre>|

***
### MinorFail Assertion number 91

[Jump to summary definition](#summary-MinorFail-91)

:exclamation:MinorFail assertion
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All the fragments from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages that are syntaxically correct as well as their recursive imports|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)<br/>- [Modelet domain-template/scenario-template/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/domain-template/scenario-template/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-behavior-specifications/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-core/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Modelet logistics/create-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/create-organization/onto.ttl)<br/>- [Modelet logistics/structure-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|
|----|----|
|Title|Term labeling test|
|Description|A test case from the Best Practices tests checking if all the terms of the subject have a rdfs:label property pointing to a literal in English|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|Terms not labeled|
|Description|The term :interaction has no rdfs:label to define it in natural language|
|Pointer|<pre lang="Turtle"><code>:interaction a owl:Ontology ;&#10;cc:license &#60;https://creativecommons.org/licenses/by/4.0/> ;&#10;dct:contributor &#60;http://ns.inria.fr/fabien.gandon#me>, &#10; &#60;https://pod.inrupt.com/andreiciortea/profile/card#me>, &#10; &#60;https://pod.inrupt.com/smnmyr/profile/card#me> ;&#10;dct:creator &#60;https://danaivach.inrupt.net/profile/card#me> ;&#10;dct:description "An ontology to describe interaction in Hypermedia Multi-Agen..."@en,&#10;"L'ontologie pour décrire l'interaction dans les systèmes mul..."@fr ;&#10;dct:issued "2023-01-13"^^xsd:date ;&#10;dct:title "Hypermedia MAS Interaction Ontology"@en,&#10;"Ontologie d'Interaction des SMA Hypermédias"@fr ;&#10;vann:preferredNamespacePrefix "hmas" ;&#10;vann:preferredNamespaceUri : ;&#10;owl:imports :core .</code></pre>|

***
### MinorFail Assertion number 92

[Jump to summary definition](#summary-MinorFail-92)

:exclamation:MinorFail assertion
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All the fragments from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages that are syntaxically correct as well as their recursive imports|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)<br/>- [Modelet domain-template/scenario-template/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/domain-template/scenario-template/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-behavior-specifications/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-core/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Modelet logistics/create-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/create-organization/onto.ttl)<br/>- [Modelet logistics/structure-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|
|----|----|
|Title|Term labeling test|
|Description|A test case from the Best Practices tests checking if all the terms of the subject have a rdfs:label property pointing to a literal in English|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|Terms not labeled|
|Description|The term :regulation has no rdfs:label to define it in natural language|
|Pointer|<pre lang="Turtle"><code>:regulation a owl:Ontology ;&#10;cc:license &#60;https://creativecommons.org/licenses/by/4.0/> ;&#10;dct:contributor &#60;http://maxime-lefrancois.info/me#>, &#10; &#60;http://ns.inria.fr/fabien.gandon#me>, &#10; &#60;https://danaivach.inrupt.net/profile/card#me>, &#10; &#60;https://orcid.org/0000-0002-2956-0533>, &#10; &#60;https://orcid.org/0000-0002-3497-8758>, &#10; &#60;https://orcid.org/0000-0003-0821-6095>, &#10; &#60;https://orcid.org/0000-0003-4509-9537> ;&#10;dct:creator &#60;https://orcid.org/0000-0002-4506-2745> ;&#10;dct:description "An ontology to describe the regulation of Hypermedia Multi-A..."@en,&#10;"L'ontologie pour décrire la régulation des systèmes multi-ag..."@fr ;&#10;dct:issued "2022-05-01"^^xsd:date ;&#10;dct:title "Hypermedia MAS Regulation Ontology"@en,&#10;"Ontologie de Régulation des SMA Hypermédias"@fr ;&#10;vann:preferredNamespacePrefix "hmas" ;&#10;vann:preferredNamespaceUri : ;&#10;owl:imports :core .</code></pre>|

***
### MinorFail Assertion number 93

[Jump to summary definition](#summary-MinorFail-93)

:exclamation:MinorFail assertion
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All the fragments from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages that are syntaxically correct as well as their recursive imports|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)<br/>- [Modelet domain-template/scenario-template/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/domain-template/scenario-template/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-behavior-specifications/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-core/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Modelet logistics/create-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/create-organization/onto.ttl)<br/>- [Modelet logistics/structure-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|
|----|----|
|Title|Term labeling test|
|Description|A test case from the Best Practices tests checking if all the terms of the subject have a rdfs:label property pointing to a literal in English|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|Terms not labeled|
|Description|The term :Affordance has no rdfs:label to define it in natural language|
|Pointer|<pre lang="Turtle"><code>:Affordance a skos:Concept ;&#10;dct:references [ rdfs:label "Chemero and Turvey, 2007"@en ;&#10;dct:bibliographicCitation "Chemero, A., & Turvey, M. T. (2007). Complexity, hypersets, ..."@en ],&#10;[ rdfs:label "Norman, 2013"@en ;&#10;dct:bibliographicCitation "Norman, D. (2013). The design of everyday things: Revised an..."@en ],&#10;[ a owl:NamedIndividual ;&#10;rdfs:label "Chemero and Turvey, 2007"@en ;&#10;dct:bibliographicCitation "Chemero, A., & Turvey, M. T. (2007). Complexity, hypersets, ..."@en ;&#10;dct:identifier &#60;https://doi.org/10.1162/biot.2007.2.1.23> ],&#10;[ a owl:NamedIndividual ;&#10;rdfs:label "Norman, 2013"@en ;&#10;dct:bibliographicCitation "Norman, D. (2013). The design of everyday things: Revised an..."@en ;&#10;dct:identifier &#60;https://mitpress.mit.edu/9780262640374/> ] ;&#10;rdfs:isDefinedBy :core ;&#10;skos:definition "A behavior possibility that is a relationship between an abi..."@en ;&#10;skos:editorialNote "The concept has been considered as a candidate term for repr..."@en ;&#10;skos:historyNote "The definition of the concept follows affordance theorists [..."@en ;&#10;skos:prefLabel "affordance"@en ;&#10;skos:related :Signifier .</code></pre>|

***
### MinorFail Assertion number 94

[Jump to summary definition](#summary-MinorFail-94)

:exclamation:MinorFail assertion
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All the fragments from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages that are syntaxically correct as well as their recursive imports|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)<br/>- [Modelet domain-template/scenario-template/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/domain-template/scenario-template/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-behavior-specifications/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-core/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Modelet logistics/create-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/create-organization/onto.ttl)<br/>- [Modelet logistics/structure-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|
|----|----|
|Title|Term labeling test|
|Description|A test case from the Best Practices tests checking if all the terms of the subject have a rdfs:label property pointing to a literal in English|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|Terms not labeled|
|Description|The term :OrganizationModel has no rdfs:label to define it in natural language|
|Pointer|<pre lang="Turtle"><code>:OrganizationModel a skos:Concept ;&#10;skos:definition "An Organization Model is the combination of Roles, Missions,..."@en ;&#10;skos:editorialNote "The Organization Model is represented as SHACL Shapes."@en ;&#10;skos:prefLabel "organization model"@en ;&#10;skos:related :Organization .</code></pre>|

***
### MinorFail Assertion number 95

[Jump to summary definition](#summary-MinorFail-95)

:exclamation:MinorFail assertion
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All the fragments from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages that are syntaxically correct as well as their recursive imports|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)<br/>- [Modelet domain-template/scenario-template/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/domain-template/scenario-template/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-behavior-specifications/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-core/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Modelet logistics/create-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/create-organization/onto.ttl)<br/>- [Modelet logistics/structure-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL QL Profile incompatible|
|Description|Anonymous individuals are not supported|
|Pointer|<pre lang="Turtle"><code>[] a owl:NamedIndividual ;&#10;rdfs:label "Chemero and Turvey, 2007"@en ;&#10;dc:bibliographicCitation "Chemero, A., & Turvey, M. T. (2007). Complexity, hypersets, ..."@en ;&#10;dc:identifier &#60;https://doi.org/10.1162/biot.2007.2.1.23> .</code></pre>|

***
### MinorFail Assertion number 96

[Jump to summary definition](#summary-MinorFail-96)

:exclamation:MinorFail assertion
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All the fragments from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages that are syntaxically correct as well as their recursive imports|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)<br/>- [Modelet domain-template/scenario-template/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/domain-template/scenario-template/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-behavior-specifications/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-core/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Modelet logistics/create-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/create-organization/onto.ttl)<br/>- [Modelet logistics/structure-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL QL Profile incompatible|
|Description|Anonymous individuals are not supported|
|Pointer|<pre lang="Turtle"><code>[] a owl:NamedIndividual ;&#10;rdfs:label "Norman, 2013"@en ;&#10;dc:bibliographicCitation "Norman, D. (2013). The design of everyday things: Revised an..."@en ;&#10;dc:identifier &#60;https://mitpress.mit.edu/9780262640374/> .</code></pre>|

***
### MinorFail Assertion number 97

[Jump to summary definition](#summary-MinorFail-97)

:exclamation:MinorFail assertion
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All the fragments from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages that are syntaxically correct as well as their recursive imports|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)<br/>- [Modelet domain-template/scenario-template/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/domain-template/scenario-template/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-behavior-specifications/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-core/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Modelet logistics/create-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/create-organization/onto.ttl)<br/>- [Modelet logistics/structure-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL QL Profile incompatible|
|Description|Anonymous individuals are not supported|
|Pointer|<pre lang="Turtle"><code>[] rdfs:label "Chemero and Turvey, 2007"@en ;&#10;dc:bibliographicCitation "Chemero, A., & Turvey, M. T. (2007). Complexity, hypersets, ..."@en .</code></pre>|

***
### MinorFail Assertion number 98

[Jump to summary definition](#summary-MinorFail-98)

:exclamation:MinorFail assertion
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All the fragments from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages that are syntaxically correct as well as their recursive imports|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)<br/>- [Modelet domain-template/scenario-template/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/domain-template/scenario-template/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-behavior-specifications/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-core/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Modelet logistics/create-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/create-organization/onto.ttl)<br/>- [Modelet logistics/structure-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL QL Profile incompatible|
|Description|Anonymous individuals are not supported|
|Pointer|<pre lang="Turtle"><code>[] rdfs:label "Norman, 2013"@en ;&#10;dc:bibliographicCitation "Norman, D. (2013). The design of everyday things: Revised an..."@en .</code></pre>|

***
### MinorFail Assertion number 99

[Jump to summary definition](#summary-MinorFail-99)

:exclamation:MinorFail assertion
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All the fragments from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages that are syntaxically correct as well as their recursive imports|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)<br/>- [Modelet domain-template/scenario-template/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/domain-template/scenario-template/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-behavior-specifications/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-core/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Modelet logistics/create-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/create-organization/onto.ttl)<br/>- [Modelet logistics/structure-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL QL Profile incompatible|
|Description|Anonymous individuals are not supported|
|Pointer|<pre lang="Turtle"><code>&#60;https://purl.org/hmas/Affordance> a skos:Concept ;&#10;dc:references [ a owl:NamedIndividual ;&#10;rdfs:label "Chemero and Turvey, 2007"@en ;&#10;dc:bibliographicCitation "Chemero, A., & Turvey, M. T. (2007). Complexity, hypersets, ..."@en ;&#10;dc:identifier &#60;https://doi.org/10.1162/biot.2007.2.1.23> ],&#10;[ a owl:NamedIndividual ;&#10;rdfs:label "Norman, 2013"@en ;&#10;dc:bibliographicCitation "Norman, D. (2013). The design of everyday things: Revised an..."@en ;&#10;dc:identifier &#60;https://mitpress.mit.edu/9780262640374/> ],&#10;[ rdfs:label "Chemero and Turvey, 2007"@en ;&#10;dc:bibliographicCitation "Chemero, A., & Turvey, M. T. (2007). Complexity, hypersets, ..."@en ],&#10;[ rdfs:label "Norman, 2013"@en ;&#10;dc:bibliographicCitation "Norman, D. (2013). The design of everyday things: Revised an..."@en ] ;&#10;rdfs:isDefinedBy &#60;https://purl.org/hmas/core> ;&#10;skos:definition "A behavior possibility that is a relationship between an abi..."@en ;&#10;skos:editorialNote "The concept has been considered as a candidate term for repr..."@en ;&#10;skos:historyNote "The definition of the concept follows affordance theorists [..."@en ;&#10;skos:prefLabel "affordance"@en ;&#10;skos:related &#60;https://purl.org/hmas/Signifier> .</code></pre>|

***
### MinorFail Assertion number 100

[Jump to summary definition](#summary-MinorFail-100)

:exclamation:MinorFail assertion
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All the fragments from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages that are syntaxically correct as well as their recursive imports|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)<br/>- [Modelet domain-template/scenario-template/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/domain-template/scenario-template/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-behavior-specifications/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-core/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Modelet logistics/create-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/create-organization/onto.ttl)<br/>- [Modelet logistics/structure-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL QL Profile incompatible|
|Description|Statement not supported|
|Pointer|<pre lang="Turtle"><code>&#60;https://purl.org/hmas/transitivelyContains> a owl:ObjectProperty,&#10;owl:TransitiveProperty ;&#10;rdfs:label "transitively contains"@en,&#10;"transitivelyContains"@en,&#10;"contient transitivement"@fr ;&#10;dc:source &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/8#issuecomment-1025991719> ;&#10;rdfs:comment "Links all the resources that are logically contained in a wo..."@en ;&#10;rdfs:domain &#60;https://purl.org/hmas/Workspace> ;&#10;rdfs:isDefinedBy &#60;https://purl.org/hmas/core> ;&#10;rdfs:seeAlso &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/18>, &#10; &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/39> ;&#10;owl:inverseOf &#60;https://purl.org/hmas/isTransitivelyContainedIn> .</code></pre>|

***
### MinorFail Assertion number 101

[Jump to summary definition](#summary-MinorFail-101)

:exclamation:MinorFail assertion
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All the fragments from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages that are syntaxically correct as well as their recursive imports|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)<br/>- [Modelet domain-template/scenario-template/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/domain-template/scenario-template/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-behavior-specifications/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-core/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Modelet logistics/create-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/create-organization/onto.ttl)<br/>- [Modelet logistics/structure-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL EL Profile incompatible|
|Description|Anonymous individuals are not supported|
|Pointer|<pre lang="Turtle"><code>[] a owl:NamedIndividual ;&#10;rdfs:label "Chemero and Turvey, 2007"@en ;&#10;dc:bibliographicCitation "Chemero, A., & Turvey, M. T. (2007). Complexity, hypersets, ..."@en ;&#10;dc:identifier &#60;https://doi.org/10.1162/biot.2007.2.1.23> .</code></pre>|

***
### MinorFail Assertion number 102

[Jump to summary definition](#summary-MinorFail-102)

:exclamation:MinorFail assertion
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All the fragments from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages that are syntaxically correct as well as their recursive imports|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)<br/>- [Modelet domain-template/scenario-template/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/domain-template/scenario-template/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-behavior-specifications/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-core/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Modelet logistics/create-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/create-organization/onto.ttl)<br/>- [Modelet logistics/structure-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL EL Profile incompatible|
|Description|Anonymous individuals are not supported|
|Pointer|<pre lang="Turtle"><code>[] a owl:NamedIndividual ;&#10;rdfs:label "Norman, 2013"@en ;&#10;dc:bibliographicCitation "Norman, D. (2013). The design of everyday things: Revised an..."@en ;&#10;dc:identifier &#60;https://mitpress.mit.edu/9780262640374/> .</code></pre>|

***
### MinorFail Assertion number 103

[Jump to summary definition](#summary-MinorFail-103)

:exclamation:MinorFail assertion
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All the fragments from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages that are syntaxically correct as well as their recursive imports|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)<br/>- [Modelet domain-template/scenario-template/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/domain-template/scenario-template/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-behavior-specifications/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-core/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Modelet logistics/create-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/create-organization/onto.ttl)<br/>- [Modelet logistics/structure-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL EL Profile incompatible|
|Description|Anonymous individuals are not supported|
|Pointer|<pre lang="Turtle"><code>[] rdfs:label "Chemero and Turvey, 2007"@en ;&#10;dc:bibliographicCitation "Chemero, A., & Turvey, M. T. (2007). Complexity, hypersets, ..."@en .</code></pre>|

***
### MinorFail Assertion number 104

[Jump to summary definition](#summary-MinorFail-104)

:exclamation:MinorFail assertion
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All the fragments from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages that are syntaxically correct as well as their recursive imports|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)<br/>- [Modelet domain-template/scenario-template/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/domain-template/scenario-template/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-behavior-specifications/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-core/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Modelet logistics/create-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/create-organization/onto.ttl)<br/>- [Modelet logistics/structure-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL EL Profile incompatible|
|Description|Anonymous individuals are not supported|
|Pointer|<pre lang="Turtle"><code>[] rdfs:label "Norman, 2013"@en ;&#10;dc:bibliographicCitation "Norman, D. (2013). The design of everyday things: Revised an..."@en .</code></pre>|

***
### MinorFail Assertion number 105

[Jump to summary definition](#summary-MinorFail-105)

:exclamation:MinorFail assertion
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All the fragments from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages that are syntaxically correct as well as their recursive imports|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)<br/>- [Modelet domain-template/scenario-template/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/domain-template/scenario-template/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-behavior-specifications/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-core/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Modelet logistics/create-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/create-organization/onto.ttl)<br/>- [Modelet logistics/structure-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL EL Profile incompatible|
|Description|Anonymous individuals are not supported|
|Pointer|<pre lang="Turtle"><code>&#60;https://purl.org/hmas/Affordance> a skos:Concept ;&#10;dc:references [ a owl:NamedIndividual ;&#10;rdfs:label "Chemero and Turvey, 2007"@en ;&#10;dc:bibliographicCitation "Chemero, A., & Turvey, M. T. (2007). Complexity, hypersets, ..."@en ;&#10;dc:identifier &#60;https://doi.org/10.1162/biot.2007.2.1.23> ],&#10;[ a owl:NamedIndividual ;&#10;rdfs:label "Norman, 2013"@en ;&#10;dc:bibliographicCitation "Norman, D. (2013). The design of everyday things: Revised an..."@en ;&#10;dc:identifier &#60;https://mitpress.mit.edu/9780262640374/> ],&#10;[ rdfs:label "Chemero and Turvey, 2007"@en ;&#10;dc:bibliographicCitation "Chemero, A., & Turvey, M. T. (2007). Complexity, hypersets, ..."@en ],&#10;[ rdfs:label "Norman, 2013"@en ;&#10;dc:bibliographicCitation "Norman, D. (2013). The design of everyday things: Revised an..."@en ] ;&#10;rdfs:isDefinedBy &#60;https://purl.org/hmas/core> ;&#10;skos:definition "A behavior possibility that is a relationship between an abi..."@en ;&#10;skos:editorialNote "The concept has been considered as a candidate term for repr..."@en ;&#10;skos:historyNote "The definition of the concept follows affordance theorists [..."@en ;&#10;skos:prefLabel "affordance"@en ;&#10;skos:related &#60;https://purl.org/hmas/Signifier> .</code></pre>|

***
### MinorFail Assertion number 106

[Jump to summary definition](#summary-MinorFail-106)

:exclamation:MinorFail assertion
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All the fragments from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages that are syntaxically correct as well as their recursive imports|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)<br/>- [Modelet domain-template/scenario-template/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/domain-template/scenario-template/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-behavior-specifications/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-core/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Modelet logistics/create-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/create-organization/onto.ttl)<br/>- [Modelet logistics/structure-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|OWL EL Profile incompatible|
|Description|Statement not supported|
|Pointer|<pre lang="Turtle"><code>&#60;https://purl.org/hmas/hasProfile> a owl:AsymmetricProperty,&#10;owl:ObjectProperty ;&#10;rdfs:label "has for profile"@en,&#10;"has profile"@en,&#10;"a pour profil"@fr ;&#10;rdfs:comment "A relation that links a resource to its profile."@en ;&#10;rdfs:isDefinedBy &#60;https://purl.org/hmas/core> ;&#10;rdfs:range &#60;https://purl.org/hmas/ResourceProfile> ;&#10;owl:inverseOf &#60;https://purl.org/hmas/isProfileOf> .</code></pre>|

***
### MinorFail Assertion number 107

[Jump to summary definition](#summary-MinorFail-107)

:exclamation:MinorFail assertion
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All the fragments from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages that are syntaxically correct as well as their recursive imports|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)<br/>- [Modelet domain-template/scenario-template/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/domain-template/scenario-template/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-behavior-specifications/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-core/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Modelet logistics/create-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/create-organization/onto.ttl)<br/>- [Modelet logistics/structure-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#terms-differenciation)|
|----|----|
|Title|Terms differenciation test|
|Description|A test case from the Best Practices tests checking if all the terms are different enough from each other according to the Levenshtein distance metric.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|Too close terms|
|Description|The following terms are too similar: :core and :Role|
|Pointer|<pre lang="Turtle"><code>:core a owl:Ontology ;&#10;cc:license &#60;https://creativecommons.org/licenses/by/4.0/> ;&#10;dct:contributor &#60;http://maxime-lefrancois.info/me#>, &#10; &#60;http://ns.inria.fr/fabien.gandon#me>, &#10; &#60;http://w3id.org/people/az/me>, &#10; &#60;https://danaivach.inrupt.net/profile/card#me>, &#10; &#60;https://id.inrupt.com/smnmyr>, &#10; &#60;https://orcid.org/0000-0002-2956-0533>, &#10; &#60;https://orcid.org/0000-0002-4506-2745>, &#10; &#60;https://orcid.org/0000-0003-0821-6095>, &#10; &#60;https://www.vcharpenay.link/#me> ;&#10;dct:creator &#60;https://id.inrupt.com/andreiciortea> ;&#10;dct:description "An ontology to describe Hypermedia Multi-Agent Systems."@en,&#10;"Une ontologie pour la description de systèmes multi-agents h..."@fr ;&#10;dct:issued "2021-11-21"^^xsd:date ;&#10;dct:title "Hypermedia MAS Core Ontology"@en,&#10;"Ontologie Centrale des SMA Hypermédias"@fr ;&#10;vann:preferredNamespacePrefix "hmas" ;&#10;vann:preferredNamespaceUri : .</code></pre>|
|Pointer|<pre lang="Turtle"><code>:Role a owl:Class ;&#10;rdfs:label "role"@en,&#10;"rôle"@fr ;&#10;rdfs:comment "A Role defines positions of members (i.e., Agents) in an Org..."@en ;&#10;rdfs:isDefinedBy :regulation .</code></pre>|

***
### MinorFail Assertion number 108

[Jump to summary definition](#summary-MinorFail-108)

:exclamation:MinorFail assertion
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All the fragments from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages that are syntaxically correct as well as their recursive imports|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)<br/>- [Modelet domain-template/scenario-template/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/domain-template/scenario-template/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-behavior-specifications/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-core/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Modelet logistics/create-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/create-organization/onto.ttl)<br/>- [Modelet logistics/structure-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#terms-differenciation)|
|----|----|
|Title|Terms differenciation test|
|Description|A test case from the Best Practices tests checking if all the terms are different enough from each other according to the Levenshtein distance metric.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|Too close terms|
|Description|The following terms are too similar: :isMembershipOf and :isMembershipIn|
|Pointer|<pre lang="Turtle"><code>:isMembershipOf a owl:ObjectProperty ;&#10;rdfs:label "is membership of"@en,&#10;"est l'appartenance à"@fr ;&#10;rdfs:comment "A relation that refers to the Agent involved in a Membership..."@en ;&#10;rdfs:domain :Membership ;&#10;rdfs:isDefinedBy :regulation ;&#10;rdfs:range :Agent .</code></pre>|
|Pointer|<pre lang="Turtle"><code>:isMembershipIn a owl:ObjectProperty ;&#10;rdfs:label "is membership in"@en,&#10;"est l'appartenance à"@fr ;&#10;rdfs:comment "A relation that refers to the Group involved in a Membership..."@en ;&#10;rdfs:domain :Membership ;&#10;rdfs:isDefinedBy :regulation ;&#10;rdfs:range :Group .</code></pre>|

***
### MinorFail Assertion number 109

[Jump to summary definition](#summary-MinorFail-109)

:exclamation:MinorFail assertion
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All the fragments from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages that are syntaxically correct as well as their recursive imports|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)<br/>- [Modelet domain-template/scenario-template/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/domain-template/scenario-template/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-behavior-specifications/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-core/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Modelet logistics/create-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/create-organization/onto.ttl)<br/>- [Modelet logistics/structure-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#terms-differenciation)|
|----|----|
|Title|Terms differenciation test|
|Description|A test case from the Best Practices tests checking if all the terms are different enough from each other according to the Levenshtein distance metric.|

#### Outcome Detail
|Type|:exclamation:MinorFail|
|----|----|
|Title|Too close terms|
|Description|The following terms are too similar: :signifies and :Signifier|
|Pointer|<pre lang="Turtle"><code>:signifies a owl:ObjectProperty ;&#10;rdfs:label "signifies"@en,&#10;"signifie"@fr ;&#10;rdfs:comment "A relation between a signifier and the specification of a be..."@en ;&#10;rdfs:domain :Signifier ;&#10;rdfs:isDefinedBy :interaction .</code></pre>|
|Pointer|<pre lang="Turtle"><code>:Signifier a owl:Class ;&#10;rdfs:label "Signifier"@en,&#10;"signifier"@en,&#10;"Signifiant"@fr,&#10;"signifiant"@fr ;&#10;rdfs:comment "A perceivable sign/cue that can be interpreted meaningfully ..."@en ;&#10;rdfs:isDefinedBy :core ;&#10;rdfs:seeAlso &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/13#issuecomment-1028904491>, &#10; &#60;https://github.com/HyperAgents/ns.hyperagents.org/issues/41> ;&#10;rdfs:subClassOf :Hostable ;&#10;skos:note ":Signifier works as a bridge between the Core and the Intera..."@en ;&#10;skos:related :Affordance,&#10;:Signifier .</code></pre>|

***

</details>

***


# NotTested Assertions

Here is the chapter related to the NotTested assertion

:grey_question:30 NotTested assertions

<details>
<summary>Fold/Unfold the 30 summary and details</summary>

## NotTested Assertions Summary

[Jump to statistic summary](#statistic-summary)

:grey_question:30 NotTested assertions

|*Jump*|*Number*|*Status*|*Subject*|*Criterion*|*Title*|*Link*|
|------|--------|--------|---------|-----------|-------|------|
|[Table top](#nottested-assertions-summary)|<div id="summary-NotTested-1">1/30</div>|:grey_question:*NotTested*|`meta`|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|The test could not be run|[Jump](#nottested-assertion-number-1)|
|[Table top](#nottested-assertions-summary)|<div id="summary-NotTested-2">2/30</div>|:grey_question:*NotTested*|`meta`|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|The test could not be run|[Jump](#nottested-assertion-number-2)|
|[Table top](#nottested-assertions-summary)|<div id="summary-NotTested-3">3/30</div>|:grey_question:*NotTested*|`meta`|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|The test could not be run|[Jump](#nottested-assertion-number-3)|
|[Table top](#nottested-assertions-summary)|<div id="summary-NotTested-4">4/30</div>|:grey_question:*NotTested*|`meta`|[owl-rl-constraint](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#owl-rl-constraint)|The test could not be run|[Jump](#nottested-assertion-number-4)|
|[Table top](#nottested-assertions-summary)|<div id="summary-NotTested-5">5/30</div>|:grey_question:*NotTested*|`meta`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|The test could not be run|[Jump](#nottested-assertion-number-5)|
|[Table top](#nottested-assertions-summary)|<div id="summary-NotTested-6">6/30</div>|:grey_question:*NotTested*|`meta`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|The test could not be run|[Jump](#nottested-assertion-number-6)|
|[Table top](#nottested-assertions-summary)|<div id="summary-NotTested-7">7/30</div>|:grey_question:*NotTested*|`meta`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|The test could not be run|[Jump](#nottested-assertion-number-7)|
|[Table top](#nottested-assertions-summary)|<div id="summary-NotTested-8">8/30</div>|:grey_question:*NotTested*|`meta`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|The test could not be run|[Jump](#nottested-assertion-number-8)|
|[Table top](#nottested-assertions-summary)|<div id="summary-NotTested-9">9/30</div>|:grey_question:*NotTested*|`meta`|[term-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#term-referencing)|The test could not be run|[Jump](#nottested-assertion-number-9)|
|[Table top](#nottested-assertions-summary)|<div id="summary-NotTested-10">10/30</div>|:grey_question:*NotTested*|`meta`|[terms-differenciation](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#terms-differenciation)|The test could not be run|[Jump](#nottested-assertion-number-10)|
|[Table top](#nottested-assertions-summary)|<div id="summary-NotTested-11">11/30</div>|:grey_question:*NotTested*|`manufacturing-environments-safety-rules`|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|The test could not be run|[Jump](#nottested-assertion-number-11)|
|[Table top](#nottested-assertions-summary)|<div id="summary-NotTested-12">12/30</div>|:grey_question:*NotTested*|`manufacturing-environments-safety-rules`|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|The test could not be run|[Jump](#nottested-assertion-number-12)|
|[Table top](#nottested-assertions-summary)|<div id="summary-NotTested-13">13/30</div>|:grey_question:*NotTested*|`manufacturing-environments-safety-rules`|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|The test could not be run|[Jump](#nottested-assertion-number-13)|
|[Table top](#nottested-assertions-summary)|<div id="summary-NotTested-14">14/30</div>|:grey_question:*NotTested*|`manufacturing-environments-safety-rules`|[owl-rl-constraint](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#owl-rl-constraint)|The test could not be run|[Jump](#nottested-assertion-number-14)|
|[Table top](#nottested-assertions-summary)|<div id="summary-NotTested-15">15/30</div>|:grey_question:*NotTested*|`manufacturing-environments-safety-rules`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|The test could not be run|[Jump](#nottested-assertion-number-15)|
|[Table top](#nottested-assertions-summary)|<div id="summary-NotTested-16">16/30</div>|:grey_question:*NotTested*|`manufacturing-environments-safety-rules`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|The test could not be run|[Jump](#nottested-assertion-number-16)|
|[Table top](#nottested-assertions-summary)|<div id="summary-NotTested-17">17/30</div>|:grey_question:*NotTested*|`manufacturing-environments-safety-rules`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|The test could not be run|[Jump](#nottested-assertion-number-17)|
|[Table top](#nottested-assertions-summary)|<div id="summary-NotTested-18">18/30</div>|:grey_question:*NotTested*|`manufacturing-environments-safety-rules`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|The test could not be run|[Jump](#nottested-assertion-number-18)|
|[Table top](#nottested-assertions-summary)|<div id="summary-NotTested-19">19/30</div>|:grey_question:*NotTested*|`manufacturing-environments-safety-rules`|[term-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#term-referencing)|The test could not be run|[Jump](#nottested-assertion-number-19)|
|[Table top](#nottested-assertions-summary)|<div id="summary-NotTested-20">20/30</div>|:grey_question:*NotTested*|`manufacturing-environments-safety-rules`|[terms-differenciation](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#terms-differenciation)|The test could not be run|[Jump](#nottested-assertion-number-20)|
|[Table top](#nottested-assertions-summary)|<div id="summary-NotTested-21">21/30</div>|:grey_question:*NotTested*|`fipa`|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|The test could not be run|[Jump](#nottested-assertion-number-21)|
|[Table top](#nottested-assertions-summary)|<div id="summary-NotTested-22">22/30</div>|:grey_question:*NotTested*|`fipa`|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|The test could not be run|[Jump](#nottested-assertion-number-22)|
|[Table top](#nottested-assertions-summary)|<div id="summary-NotTested-23">23/30</div>|:grey_question:*NotTested*|`fipa`|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|The test could not be run|[Jump](#nottested-assertion-number-23)|
|[Table top](#nottested-assertions-summary)|<div id="summary-NotTested-24">24/30</div>|:grey_question:*NotTested*|`fipa`|[owl-rl-constraint](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#owl-rl-constraint)|The test could not be run|[Jump](#nottested-assertion-number-24)|
|[Table top](#nottested-assertions-summary)|<div id="summary-NotTested-25">25/30</div>|:grey_question:*NotTested*|`fipa`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|The test could not be run|[Jump](#nottested-assertion-number-25)|
|[Table top](#nottested-assertions-summary)|<div id="summary-NotTested-26">26/30</div>|:grey_question:*NotTested*|`fipa`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|The test could not be run|[Jump](#nottested-assertion-number-26)|
|[Table top](#nottested-assertions-summary)|<div id="summary-NotTested-27">27/30</div>|:grey_question:*NotTested*|`fipa`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|The test could not be run|[Jump](#nottested-assertion-number-27)|
|[Table top](#nottested-assertions-summary)|<div id="summary-NotTested-28">28/30</div>|:grey_question:*NotTested*|`fipa`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|The test could not be run|[Jump](#nottested-assertion-number-28)|
|[Table top](#nottested-assertions-summary)|<div id="summary-NotTested-29">29/30</div>|:grey_question:*NotTested*|`fipa`|[term-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#term-referencing)|The test could not be run|[Jump](#nottested-assertion-number-29)|
|[Table top](#nottested-assertions-summary)|<div id="summary-NotTested-30">30/30</div>|:grey_question:*NotTested*|`fipa`|[terms-differenciation](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#terms-differenciation)|The test could not be run|[Jump](#nottested-assertion-number-30)|

***

## NotTested Assertion Details

This subchapter gives more details to the :grey_question:NotTested assertions

### NotTested Assertion number 1

[Jump to summary definition](#summary-NotTested-1)

:grey_question:NotTested assertion
#### Subject detail
|Name|meta|
|----|----|
|Title|Standalone module src/meta.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module meta.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/meta.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Type|:grey_question:NotTested|
|----|----|
|Title|The test could not be run|
|Description|The syntax of the subject and any of its imports must be syntaxically correct|

***
### NotTested Assertion number 2

[Jump to summary definition](#summary-NotTested-2)

:grey_question:NotTested assertion
#### Subject detail
|Name|meta|
|----|----|
|Title|Standalone module src/meta.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module meta.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/meta.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Type|:grey_question:NotTested|
|----|----|
|Title|The test could not be run|
|Description|The syntax of the subject and any of its imports must be syntaxically correct|

***
### NotTested Assertion number 3

[Jump to summary definition](#summary-NotTested-3)

:grey_question:NotTested assertion
#### Subject detail
|Name|meta|
|----|----|
|Title|Standalone module src/meta.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module meta.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/meta.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|
|----|----|
|Title|Term labeling test|
|Description|A test case from the Best Practices tests checking if all the terms of the subject have a rdfs:label property pointing to a literal in English|

#### Outcome Detail
|Type|:grey_question:NotTested|
|----|----|
|Title|The test could not be run|
|Description|The subject and its recursive imports must be syntaxically correct|

***
### NotTested Assertion number 4

[Jump to summary definition](#summary-NotTested-4)

:grey_question:NotTested assertion
#### Subject detail
|Name|meta|
|----|----|
|Title|Standalone module src/meta.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module meta.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/meta.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#owl-rl-constraint)|
|----|----|
|Title|OWL RL Constraint test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:grey_question:NotTested|
|----|----|
|Title|The test could not be run|
|Description|The subject and its recursive imports must be syntaxically correct|

***
### NotTested Assertion number 5

[Jump to summary definition](#summary-NotTested-5)

:grey_question:NotTested assertion
#### Subject detail
|Name|meta|
|----|----|
|Title|Standalone module src/meta.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module meta.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/meta.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:grey_question:NotTested|
|----|----|
|Title|The test could not be run|
|Description|The subject must be syntaxically correct|

***
### NotTested Assertion number 6

[Jump to summary definition](#summary-NotTested-6)

:grey_question:NotTested assertion
#### Subject detail
|Name|meta|
|----|----|
|Title|Standalone module src/meta.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module meta.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/meta.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:grey_question:NotTested|
|----|----|
|Title|The test could not be run|
|Description|The subject must be syntaxically correct|

***
### NotTested Assertion number 7

[Jump to summary definition](#summary-NotTested-7)

:grey_question:NotTested assertion
#### Subject detail
|Name|meta|
|----|----|
|Title|Standalone module src/meta.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module meta.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/meta.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:grey_question:NotTested|
|----|----|
|Title|The test could not be run|
|Description|The subject must be syntaxically correct|

***
### NotTested Assertion number 8

[Jump to summary definition](#summary-NotTested-8)

:grey_question:NotTested assertion
#### Subject detail
|Name|meta|
|----|----|
|Title|Standalone module src/meta.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module meta.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/meta.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:grey_question:NotTested|
|----|----|
|Title|The test could not be run|
|Description|The subject must be syntaxically correct|

***
### NotTested Assertion number 9

[Jump to summary definition](#summary-NotTested-9)

:grey_question:NotTested assertion
#### Subject detail
|Name|meta|
|----|----|
|Title|Standalone module src/meta.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module meta.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/meta.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#term-referencing)|
|----|----|
|Title|Term referencing test|
|Description|A test case from the Best Practices tests checking if each term of the test subject is referenced to a module through a rdfs:isDefinedBy property.|

#### Outcome Detail
|Type|:grey_question:NotTested|
|----|----|
|Title|The test could not be run|
|Description|The subject syntax must be correct|

***
### NotTested Assertion number 10

[Jump to summary definition](#summary-NotTested-10)

:grey_question:NotTested assertion
#### Subject detail
|Name|meta|
|----|----|
|Title|Standalone module src/meta.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module meta.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/meta.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#terms-differenciation)|
|----|----|
|Title|Terms differenciation test|
|Description|A test case from the Best Practices tests checking if all the terms are different enough from each other according to the Levenshtein distance metric.|

#### Outcome Detail
|Type|:grey_question:NotTested|
|----|----|
|Title|The test could not be run|
|Description|The subject needs to be syntaxically correct|

***
### NotTested Assertion number 11

[Jump to summary definition](#summary-NotTested-11)

:grey_question:NotTested assertion
#### Subject detail
|Name|manufacturing-environments-safety-rules|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/safety-rules/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/safety-rules/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/safety-rules/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Type|:grey_question:NotTested|
|----|----|
|Title|The test could not be run|
|Description|The syntax of the subject and any of its imports must be syntaxically correct|

***
### NotTested Assertion number 12

[Jump to summary definition](#summary-NotTested-12)

:grey_question:NotTested assertion
#### Subject detail
|Name|manufacturing-environments-safety-rules|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/safety-rules/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/safety-rules/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/safety-rules/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Type|:grey_question:NotTested|
|----|----|
|Title|The test could not be run|
|Description|The syntax of the subject and any of its imports must be syntaxically correct|

***
### NotTested Assertion number 13

[Jump to summary definition](#summary-NotTested-13)

:grey_question:NotTested assertion
#### Subject detail
|Name|manufacturing-environments-safety-rules|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/safety-rules/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/safety-rules/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/safety-rules/onto.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|
|----|----|
|Title|Term labeling test|
|Description|A test case from the Best Practices tests checking if all the terms of the subject have a rdfs:label property pointing to a literal in English|

#### Outcome Detail
|Type|:grey_question:NotTested|
|----|----|
|Title|The test could not be run|
|Description|The subject and its recursive imports must be syntaxically correct|

***
### NotTested Assertion number 14

[Jump to summary definition](#summary-NotTested-14)

:grey_question:NotTested assertion
#### Subject detail
|Name|manufacturing-environments-safety-rules|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/safety-rules/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/safety-rules/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/safety-rules/onto.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#owl-rl-constraint)|
|----|----|
|Title|OWL RL Constraint test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:grey_question:NotTested|
|----|----|
|Title|The test could not be run|
|Description|The subject and its recursive imports must be syntaxically correct|

***
### NotTested Assertion number 15

[Jump to summary definition](#summary-NotTested-15)

:grey_question:NotTested assertion
#### Subject detail
|Name|manufacturing-environments-safety-rules|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/safety-rules/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/safety-rules/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/safety-rules/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:grey_question:NotTested|
|----|----|
|Title|The test could not be run|
|Description|The subject must be syntaxically correct|

***
### NotTested Assertion number 16

[Jump to summary definition](#summary-NotTested-16)

:grey_question:NotTested assertion
#### Subject detail
|Name|manufacturing-environments-safety-rules|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/safety-rules/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/safety-rules/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/safety-rules/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:grey_question:NotTested|
|----|----|
|Title|The test could not be run|
|Description|The subject must be syntaxically correct|

***
### NotTested Assertion number 17

[Jump to summary definition](#summary-NotTested-17)

:grey_question:NotTested assertion
#### Subject detail
|Name|manufacturing-environments-safety-rules|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/safety-rules/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/safety-rules/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/safety-rules/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:grey_question:NotTested|
|----|----|
|Title|The test could not be run|
|Description|The subject must be syntaxically correct|

***
### NotTested Assertion number 18

[Jump to summary definition](#summary-NotTested-18)

:grey_question:NotTested assertion
#### Subject detail
|Name|manufacturing-environments-safety-rules|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/safety-rules/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/safety-rules/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/safety-rules/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:grey_question:NotTested|
|----|----|
|Title|The test could not be run|
|Description|The subject must be syntaxically correct|

***
### NotTested Assertion number 19

[Jump to summary definition](#summary-NotTested-19)

:grey_question:NotTested assertion
#### Subject detail
|Name|manufacturing-environments-safety-rules|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/safety-rules/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/safety-rules/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/safety-rules/onto.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#term-referencing)|
|----|----|
|Title|Term referencing test|
|Description|A test case from the Best Practices tests checking if each term of the test subject is referenced to a module through a rdfs:isDefinedBy property.|

#### Outcome Detail
|Type|:grey_question:NotTested|
|----|----|
|Title|The test could not be run|
|Description|The subject syntax must be correct|

***
### NotTested Assertion number 20

[Jump to summary definition](#summary-NotTested-20)

:grey_question:NotTested assertion
#### Subject detail
|Name|manufacturing-environments-safety-rules|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/safety-rules/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/safety-rules/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/safety-rules/onto.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#terms-differenciation)|
|----|----|
|Title|Terms differenciation test|
|Description|A test case from the Best Practices tests checking if all the terms are different enough from each other according to the Levenshtein distance metric.|

#### Outcome Detail
|Type|:grey_question:NotTested|
|----|----|
|Title|The test could not be run|
|Description|The subject needs to be syntaxically correct|

***
### NotTested Assertion number 21

[Jump to summary definition](#summary-NotTested-21)

:grey_question:NotTested assertion
#### Subject detail
|Name|fipa|
|----|----|
|Title|Standalone module src/fipa.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module fipa.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/fipa.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Type|:grey_question:NotTested|
|----|----|
|Title|The test could not be run|
|Description|The syntax of the subject and any of its imports must be syntaxically correct|

***
### NotTested Assertion number 22

[Jump to summary definition](#summary-NotTested-22)

:grey_question:NotTested assertion
#### Subject detail
|Name|fipa|
|----|----|
|Title|Standalone module src/fipa.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module fipa.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/fipa.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Type|:grey_question:NotTested|
|----|----|
|Title|The test could not be run|
|Description|The syntax of the subject and any of its imports must be syntaxically correct|

***
### NotTested Assertion number 23

[Jump to summary definition](#summary-NotTested-23)

:grey_question:NotTested assertion
#### Subject detail
|Name|fipa|
|----|----|
|Title|Standalone module src/fipa.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module fipa.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/fipa.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|
|----|----|
|Title|Term labeling test|
|Description|A test case from the Best Practices tests checking if all the terms of the subject have a rdfs:label property pointing to a literal in English|

#### Outcome Detail
|Type|:grey_question:NotTested|
|----|----|
|Title|The test could not be run|
|Description|The subject and its recursive imports must be syntaxically correct|

***
### NotTested Assertion number 24

[Jump to summary definition](#summary-NotTested-24)

:grey_question:NotTested assertion
#### Subject detail
|Name|fipa|
|----|----|
|Title|Standalone module src/fipa.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module fipa.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/fipa.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#owl-rl-constraint)|
|----|----|
|Title|OWL RL Constraint test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:grey_question:NotTested|
|----|----|
|Title|The test could not be run|
|Description|The subject and its recursive imports must be syntaxically correct|

***
### NotTested Assertion number 25

[Jump to summary definition](#summary-NotTested-25)

:grey_question:NotTested assertion
#### Subject detail
|Name|fipa|
|----|----|
|Title|Standalone module src/fipa.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module fipa.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/fipa.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:grey_question:NotTested|
|----|----|
|Title|The test could not be run|
|Description|The subject must be syntaxically correct|

***
### NotTested Assertion number 26

[Jump to summary definition](#summary-NotTested-26)

:grey_question:NotTested assertion
#### Subject detail
|Name|fipa|
|----|----|
|Title|Standalone module src/fipa.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module fipa.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/fipa.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:grey_question:NotTested|
|----|----|
|Title|The test could not be run|
|Description|The subject must be syntaxically correct|

***
### NotTested Assertion number 27

[Jump to summary definition](#summary-NotTested-27)

:grey_question:NotTested assertion
#### Subject detail
|Name|fipa|
|----|----|
|Title|Standalone module src/fipa.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module fipa.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/fipa.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:grey_question:NotTested|
|----|----|
|Title|The test could not be run|
|Description|The subject must be syntaxically correct|

***
### NotTested Assertion number 28

[Jump to summary definition](#summary-NotTested-28)

:grey_question:NotTested assertion
#### Subject detail
|Name|fipa|
|----|----|
|Title|Standalone module src/fipa.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module fipa.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/fipa.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:grey_question:NotTested|
|----|----|
|Title|The test could not be run|
|Description|The subject must be syntaxically correct|

***
### NotTested Assertion number 29

[Jump to summary definition](#summary-NotTested-29)

:grey_question:NotTested assertion
#### Subject detail
|Name|fipa|
|----|----|
|Title|Standalone module src/fipa.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module fipa.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/fipa.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#term-referencing)|
|----|----|
|Title|Term referencing test|
|Description|A test case from the Best Practices tests checking if each term of the test subject is referenced to a module through a rdfs:isDefinedBy property.|

#### Outcome Detail
|Type|:grey_question:NotTested|
|----|----|
|Title|The test could not be run|
|Description|The subject syntax must be correct|

***
### NotTested Assertion number 30

[Jump to summary definition](#summary-NotTested-30)

:grey_question:NotTested assertion
#### Subject detail
|Name|fipa|
|----|----|
|Title|Standalone module src/fipa.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module fipa.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/fipa.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#terms-differenciation)|
|----|----|
|Title|Terms differenciation test|
|Description|A test case from the Best Practices tests checking if all the terms are different enough from each other according to the Levenshtein distance metric.|

#### Outcome Detail
|Type|:grey_question:NotTested|
|----|----|
|Title|The test could not be run|
|Description|The subject needs to be syntaxically correct|

***

</details>

***


# Pass Assertions

Here is the chapter related to the Pass assertion

:white_check_mark:133 Pass assertions

<details>
<summary>Fold/Unfold the 133 summary and details</summary>

## Pass Assertions Summary

[Jump to statistic summary](#statistic-summary)

:white_check_mark:133 Pass assertions

|*Jump*|*Number*|*Status*|*Subject*|*Criterion*|*Title*|*Link*|
|------|--------|--------|---------|-----------|-------|------|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-1">1/133</div>|:white_check_mark:*Pass*|`regulation-logistics-structure-organization`|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-assertion-number-1)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-2">2/133</div>|:white_check_mark:*Pass*|`regulation-logistics-structure-organization`|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-assertion-number-2)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-3">3/133</div>|:white_check_mark:*Pass*|`regulation-logistics-structure-organization`|[owl-rl-constraint](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-assertion-number-3)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-4">4/133</div>|:white_check_mark:*Pass*|`regulation-logistics-structure-organization`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL TC Profile compatible|[Jump](#pass-assertion-number-4)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-5">5/133</div>|:white_check_mark:*Pass*|`regulation-logistics-structure-organization`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-assertion-number-5)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-6">6/133</div>|:white_check_mark:*Pass*|`regulation-logistics-structure-organization`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL QL Profile compatible|[Jump](#pass-assertion-number-6)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-7">7/133</div>|:white_check_mark:*Pass*|`regulation-logistics-structure-organization`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL EL Profile compatible|[Jump](#pass-assertion-number-7)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-8">8/133</div>|:white_check_mark:*Pass*|`regulation-logistics-structure-organization`|[term-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#term-referencing)|Any term is referenced|[Jump](#pass-assertion-number-8)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-9">9/133</div>|:white_check_mark:*Pass*|`regulation-logistics-create-organization`|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-assertion-number-9)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-10">10/133</div>|:white_check_mark:*Pass*|`regulation-logistics-create-organization`|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-assertion-number-10)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-11">11/133</div>|:white_check_mark:*Pass*|`regulation-logistics-create-organization`|[owl-rl-constraint](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-assertion-number-11)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-12">12/133</div>|:white_check_mark:*Pass*|`regulation-logistics-create-organization`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL TC Profile compatible|[Jump](#pass-assertion-number-12)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-13">13/133</div>|:white_check_mark:*Pass*|`regulation-logistics-create-organization`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-assertion-number-13)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-14">14/133</div>|:white_check_mark:*Pass*|`regulation-logistics-create-organization`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL QL Profile compatible|[Jump](#pass-assertion-number-14)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-15">15/133</div>|:white_check_mark:*Pass*|`regulation-logistics-create-organization`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL EL Profile compatible|[Jump](#pass-assertion-number-15)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-16">16/133</div>|:white_check_mark:*Pass*|`regulation-logistics-create-organization`|[term-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#term-referencing)|Any term is referenced|[Jump](#pass-assertion-number-16)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-17">17/133</div>|:white_check_mark:*Pass*|`regulation`|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-assertion-number-17)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-18">18/133</div>|:white_check_mark:*Pass*|`regulation`|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-assertion-number-18)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-19">19/133</div>|:white_check_mark:*Pass*|`regulation`|[owl-rl-constraint](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-assertion-number-19)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-20">20/133</div>|:white_check_mark:*Pass*|`regulation`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL TC Profile compatible|[Jump](#pass-assertion-number-20)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-21">21/133</div>|:white_check_mark:*Pass*|`regulation`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-assertion-number-21)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-22">22/133</div>|:white_check_mark:*Pass*|`regulation`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL QL Profile compatible|[Jump](#pass-assertion-number-22)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-23">23/133</div>|:white_check_mark:*Pass*|`regulation`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL EL Profile compatible|[Jump](#pass-assertion-number-23)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-24">24/133</div>|:white_check_mark:*Pass*|`regulation`|[term-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#term-referencing)|Any term is referenced|[Jump](#pass-assertion-number-24)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-25">25/133</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-signifiers`|[owl-rl-constraint](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-assertion-number-25)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-26">26/133</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-signifiers`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL TC Profile compatible|[Jump](#pass-assertion-number-26)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-27">27/133</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-signifiers`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-assertion-number-27)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-28">28/133</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-signifiers`|[term-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#term-referencing)|Any term is referenced|[Jump](#pass-assertion-number-28)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-29">29/133</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-signifiers`|[terms-differenciation](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#terms-differenciation)|Terms differenciated enough|[Jump](#pass-assertion-number-29)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-30">30/133</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-platforms`|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|All terms labeled|[Jump](#pass-assertion-number-30)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-31">31/133</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-platforms`|[owl-rl-constraint](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-assertion-number-31)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-32">32/133</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-platforms`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL TC Profile compatible|[Jump](#pass-assertion-number-32)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-33">33/133</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-platforms`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-assertion-number-33)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-34">34/133</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-platforms`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL QL Profile compatible|[Jump](#pass-assertion-number-34)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-35">35/133</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-platforms`|[term-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#term-referencing)|Any term is referenced|[Jump](#pass-assertion-number-35)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-36">36/133</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-platforms`|[terms-differenciation](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#terms-differenciation)|Terms differenciated enough|[Jump](#pass-assertion-number-36)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-37">37/133</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-organization`|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|All terms labeled|[Jump](#pass-assertion-number-37)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-38">38/133</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-organization`|[owl-rl-constraint](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-assertion-number-38)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-39">39/133</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-organization`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL TC Profile compatible|[Jump](#pass-assertion-number-39)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-40">40/133</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-organization`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-assertion-number-40)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-41">41/133</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-organization`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL QL Profile compatible|[Jump](#pass-assertion-number-41)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-42">42/133</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-organization`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL EL Profile compatible|[Jump](#pass-assertion-number-42)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-43">43/133</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-organization`|[term-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#term-referencing)|Any term is referenced|[Jump](#pass-assertion-number-43)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-44">44/133</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-organization`|[terms-differenciation](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#terms-differenciation)|Terms differenciated enough|[Jump](#pass-assertion-number-44)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-45">45/133</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-core`|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|All terms labeled|[Jump](#pass-assertion-number-45)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-46">46/133</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-core`|[owl-rl-constraint](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-assertion-number-46)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-47">47/133</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-core`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL TC Profile compatible|[Jump](#pass-assertion-number-47)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-48">48/133</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-core`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-assertion-number-48)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-49">49/133</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-core`|[term-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#term-referencing)|Any term is referenced|[Jump](#pass-assertion-number-49)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-50">50/133</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-core`|[terms-differenciation](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#terms-differenciation)|Terms differenciated enough|[Jump](#pass-assertion-number-50)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-51">51/133</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-behavior-specifications`|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|All terms labeled|[Jump](#pass-assertion-number-51)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-52">52/133</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-behavior-specifications`|[owl-rl-constraint](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-assertion-number-52)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-53">53/133</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-behavior-specifications`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL TC Profile compatible|[Jump](#pass-assertion-number-53)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-54">54/133</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-behavior-specifications`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-assertion-number-54)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-55">55/133</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-behavior-specifications`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL QL Profile compatible|[Jump](#pass-assertion-number-55)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-56">56/133</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-behavior-specifications`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL EL Profile compatible|[Jump](#pass-assertion-number-56)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-57">57/133</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-behavior-specifications`|[term-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#term-referencing)|Any term is referenced|[Jump](#pass-assertion-number-57)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-58">58/133</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-behavior-specifications`|[terms-differenciation](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#terms-differenciation)|Terms differenciated enough|[Jump](#pass-assertion-number-58)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-59">59/133</div>|:white_check_mark:*Pass*|`logistics-structure-organization`|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|All terms labeled|[Jump](#pass-assertion-number-59)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-60">60/133</div>|:white_check_mark:*Pass*|`logistics-structure-organization`|[owl-rl-constraint](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-assertion-number-60)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-61">61/133</div>|:white_check_mark:*Pass*|`logistics-structure-organization`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL TC Profile compatible|[Jump](#pass-assertion-number-61)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-62">62/133</div>|:white_check_mark:*Pass*|`logistics-structure-organization`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-assertion-number-62)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-63">63/133</div>|:white_check_mark:*Pass*|`logistics-structure-organization`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL QL Profile compatible|[Jump](#pass-assertion-number-63)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-64">64/133</div>|:white_check_mark:*Pass*|`logistics-structure-organization`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL EL Profile compatible|[Jump](#pass-assertion-number-64)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-65">65/133</div>|:white_check_mark:*Pass*|`logistics-structure-organization`|[term-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#term-referencing)|Any term is referenced|[Jump](#pass-assertion-number-65)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-66">66/133</div>|:white_check_mark:*Pass*|`logistics-create-organization`|[owl-rl-constraint](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-assertion-number-66)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-67">67/133</div>|:white_check_mark:*Pass*|`logistics-create-organization`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL TC Profile compatible|[Jump](#pass-assertion-number-67)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-68">68/133</div>|:white_check_mark:*Pass*|`logistics-create-organization`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-assertion-number-68)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-69">69/133</div>|:white_check_mark:*Pass*|`logistics-create-organization`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL QL Profile compatible|[Jump](#pass-assertion-number-69)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-70">70/133</div>|:white_check_mark:*Pass*|`logistics-create-organization`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL EL Profile compatible|[Jump](#pass-assertion-number-70)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-71">71/133</div>|:white_check_mark:*Pass*|`logistics-create-organization`|[term-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#term-referencing)|Any term is referenced|[Jump](#pass-assertion-number-71)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-72">72/133</div>|:white_check_mark:*Pass*|`logistics-create-organization`|[terms-differenciation](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#terms-differenciation)|Terms differenciated enough|[Jump](#pass-assertion-number-72)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-73">73/133</div>|:white_check_mark:*Pass*|`interaction-manufacturing-environments-discover-behavior-specifications`|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-assertion-number-73)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-74">74/133</div>|:white_check_mark:*Pass*|`interaction-manufacturing-environments-discover-behavior-specifications`|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-assertion-number-74)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-75">75/133</div>|:white_check_mark:*Pass*|`interaction-manufacturing-environments-discover-behavior-specifications`|[owl-rl-constraint](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-assertion-number-75)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-76">76/133</div>|:white_check_mark:*Pass*|`interaction-manufacturing-environments-discover-behavior-specifications`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL TC Profile compatible|[Jump](#pass-assertion-number-76)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-77">77/133</div>|:white_check_mark:*Pass*|`interaction-manufacturing-environments-discover-behavior-specifications`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-assertion-number-77)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-78">78/133</div>|:white_check_mark:*Pass*|`interaction-manufacturing-environments-discover-behavior-specifications`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL QL Profile compatible|[Jump](#pass-assertion-number-78)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-79">79/133</div>|:white_check_mark:*Pass*|`interaction-manufacturing-environments-discover-behavior-specifications`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL EL Profile compatible|[Jump](#pass-assertion-number-79)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-80">80/133</div>|:white_check_mark:*Pass*|`interaction-manufacturing-environments-discover-behavior-specifications`|[term-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#term-referencing)|Any term is referenced|[Jump](#pass-assertion-number-80)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-81">81/133</div>|:white_check_mark:*Pass*|`interaction-manufacturing-environments-discover-behavior-specifications`|[terms-differenciation](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#terms-differenciation)|Terms differenciated enough|[Jump](#pass-assertion-number-81)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-82">82/133</div>|:white_check_mark:*Pass*|`interaction`|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-assertion-number-82)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-83">83/133</div>|:white_check_mark:*Pass*|`interaction`|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-assertion-number-83)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-84">84/133</div>|:white_check_mark:*Pass*|`interaction`|[owl-rl-constraint](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-assertion-number-84)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-85">85/133</div>|:white_check_mark:*Pass*|`interaction`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL TC Profile compatible|[Jump](#pass-assertion-number-85)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-86">86/133</div>|:white_check_mark:*Pass*|`interaction`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-assertion-number-86)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-87">87/133</div>|:white_check_mark:*Pass*|`interaction`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL QL Profile compatible|[Jump](#pass-assertion-number-87)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-88">88/133</div>|:white_check_mark:*Pass*|`interaction`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL EL Profile compatible|[Jump](#pass-assertion-number-88)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-89">89/133</div>|:white_check_mark:*Pass*|`interaction`|[term-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#term-referencing)|Any term is referenced|[Jump](#pass-assertion-number-89)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-90">90/133</div>|:white_check_mark:*Pass*|`interaction`|[terms-differenciation](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#terms-differenciation)|Terms differenciated enough|[Jump](#pass-assertion-number-90)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-91">91/133</div>|:white_check_mark:*Pass*|`core-manufacturing-environments-discover-signifiers`|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-assertion-number-91)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-92">92/133</div>|:white_check_mark:*Pass*|`core-manufacturing-environments-discover-signifiers`|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-assertion-number-92)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-93">93/133</div>|:white_check_mark:*Pass*|`core-manufacturing-environments-discover-signifiers`|[owl-rl-constraint](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-assertion-number-93)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-94">94/133</div>|:white_check_mark:*Pass*|`core-manufacturing-environments-discover-signifiers`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL TC Profile compatible|[Jump](#pass-assertion-number-94)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-95">95/133</div>|:white_check_mark:*Pass*|`core-manufacturing-environments-discover-signifiers`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-assertion-number-95)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-96">96/133</div>|:white_check_mark:*Pass*|`core-manufacturing-environments-discover-signifiers`|[term-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#term-referencing)|Any term is referenced|[Jump](#pass-assertion-number-96)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-97">97/133</div>|:white_check_mark:*Pass*|`core-manufacturing-environments-discover-signifiers`|[terms-differenciation](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#terms-differenciation)|Terms differenciated enough|[Jump](#pass-assertion-number-97)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-98">98/133</div>|:white_check_mark:*Pass*|`core-manufacturing-environments-discover-platforms`|[owl-rl-constraint](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-assertion-number-98)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-99">99/133</div>|:white_check_mark:*Pass*|`core-manufacturing-environments-discover-platforms`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL TC Profile compatible|[Jump](#pass-assertion-number-99)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-100">100/133</div>|:white_check_mark:*Pass*|`core-manufacturing-environments-discover-platforms`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-assertion-number-100)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-101">101/133</div>|:white_check_mark:*Pass*|`core-manufacturing-environments-discover-platforms`|[term-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#term-referencing)|Any term is referenced|[Jump](#pass-assertion-number-101)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-102">102/133</div>|:white_check_mark:*Pass*|`core-manufacturing-environments-discover-platforms`|[terms-differenciation](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#terms-differenciation)|Terms differenciated enough|[Jump](#pass-assertion-number-102)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-103">103/133</div>|:white_check_mark:*Pass*|`core-manufacturing-environments-discover-organization`|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-assertion-number-103)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-104">104/133</div>|:white_check_mark:*Pass*|`core-manufacturing-environments-discover-organization`|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-assertion-number-104)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-105">105/133</div>|:white_check_mark:*Pass*|`core-manufacturing-environments-discover-organization`|[owl-rl-constraint](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-assertion-number-105)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-106">106/133</div>|:white_check_mark:*Pass*|`core-manufacturing-environments-discover-organization`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL TC Profile compatible|[Jump](#pass-assertion-number-106)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-107">107/133</div>|:white_check_mark:*Pass*|`core-manufacturing-environments-discover-organization`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-assertion-number-107)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-108">108/133</div>|:white_check_mark:*Pass*|`core-manufacturing-environments-discover-organization`|[term-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#term-referencing)|Any term is referenced|[Jump](#pass-assertion-number-108)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-109">109/133</div>|:white_check_mark:*Pass*|`core-manufacturing-environments-discover-organization`|[terms-differenciation](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#terms-differenciation)|Terms differenciated enough|[Jump](#pass-assertion-number-109)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-110">110/133</div>|:white_check_mark:*Pass*|`core-manufacturing-environments-discover-core`|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-assertion-number-110)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-111">111/133</div>|:white_check_mark:*Pass*|`core-manufacturing-environments-discover-core`|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-assertion-number-111)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-112">112/133</div>|:white_check_mark:*Pass*|`core-manufacturing-environments-discover-core`|[owl-rl-constraint](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-assertion-number-112)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-113">113/133</div>|:white_check_mark:*Pass*|`core-manufacturing-environments-discover-core`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL TC Profile compatible|[Jump](#pass-assertion-number-113)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-114">114/133</div>|:white_check_mark:*Pass*|`core-manufacturing-environments-discover-core`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-assertion-number-114)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-115">115/133</div>|:white_check_mark:*Pass*|`core-manufacturing-environments-discover-core`|[term-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#term-referencing)|Any term is referenced|[Jump](#pass-assertion-number-115)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-116">116/133</div>|:white_check_mark:*Pass*|`core-manufacturing-environments-discover-core`|[terms-differenciation](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#terms-differenciation)|Terms differenciated enough|[Jump](#pass-assertion-number-116)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-117">117/133</div>|:white_check_mark:*Pass*|`core`|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-assertion-number-117)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-118">118/133</div>|:white_check_mark:*Pass*|`core`|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-assertion-number-118)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-119">119/133</div>|:white_check_mark:*Pass*|`core`|[owl-rl-constraint](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-assertion-number-119)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-120">120/133</div>|:white_check_mark:*Pass*|`core`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL TC Profile compatible|[Jump](#pass-assertion-number-120)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-121">121/133</div>|:white_check_mark:*Pass*|`core`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-assertion-number-121)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-122">122/133</div>|:white_check_mark:*Pass*|`core`|[term-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#term-referencing)|Any term is referenced|[Jump](#pass-assertion-number-122)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-123">123/133</div>|:white_check_mark:*Pass*|`core`|[terms-differenciation](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#terms-differenciation)|Terms differenciated enough|[Jump](#pass-assertion-number-123)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-124">124/133</div>|:white_check_mark:*Pass*|`all-modules`|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|Domains properly defined|[Jump](#pass-assertion-number-124)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-125">125/133</div>|:white_check_mark:*Pass*|`all-modules`|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|Ranges properly defined|[Jump](#pass-assertion-number-125)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-126">126/133</div>|:white_check_mark:*Pass*|`all-modules`|[owl-rl-constraint](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-assertion-number-126)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-127">127/133</div>|:white_check_mark:*Pass*|`all-modules`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL TC Profile compatible|[Jump](#pass-assertion-number-127)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-128">128/133</div>|:white_check_mark:*Pass*|`all-modules`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-assertion-number-128)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-129">129/133</div>|:white_check_mark:*Pass*|`all-modules`|[term-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#term-referencing)|Any term is referenced|[Jump](#pass-assertion-number-129)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-130">130/133</div>|:white_check_mark:*Pass*|`all-fragments`|[owl-rl-constraint](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-assertion-number-130)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-131">131/133</div>|:white_check_mark:*Pass*|`all-fragments`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL TC Profile compatible|[Jump](#pass-assertion-number-131)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-132">132/133</div>|:white_check_mark:*Pass*|`all-fragments`|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|OWL RL Profile compatible|[Jump](#pass-assertion-number-132)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-133">133/133</div>|:white_check_mark:*Pass*|`all-fragments`|[term-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#term-referencing)|Any term is referenced|[Jump](#pass-assertion-number-133)|

***

## Pass Assertion Details

This subchapter gives more details to the :white_check_mark:Pass assertions

### Pass Assertion number 1

[Jump to summary definition](#summary-Pass-1)

:white_check_mark:Pass assertion
#### Subject detail
|Name|regulation-logistics-structure-organization|
|----|----|
|Title|Merged module src/regulation.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/logistics/structure-organization/onto.ttl|
|Composition|- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)<br/>- [Modelet logistics/structure-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Domains properly defined|
|Description|Each rdfs:domain is defined within the fragment|

***
### Pass Assertion number 2

[Jump to summary definition](#summary-Pass-2)

:white_check_mark:Pass assertion
#### Subject detail
|Name|regulation-logistics-structure-organization|
|----|----|
|Title|Merged module src/regulation.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/logistics/structure-organization/onto.ttl|
|Composition|- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)<br/>- [Modelet logistics/structure-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Ranges properly defined|
|Description|Each rdfs:range is defined within the fragment|

***
### Pass Assertion number 3

[Jump to summary definition](#summary-Pass-3)

:white_check_mark:Pass assertion
#### Subject detail
|Name|regulation-logistics-structure-organization|
|----|----|
|Title|Merged module src/regulation.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/logistics/structure-organization/onto.ttl|
|Composition|- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)<br/>- [Modelet logistics/structure-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#owl-rl-constraint)|
|----|----|
|Title|OWL RL Constraint test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL RL consistent|
|Description|The provided graph is consistent for any OWL RL constraint|

***
### Pass Assertion number 4

[Jump to summary definition](#summary-Pass-4)

:white_check_mark:Pass assertion
#### Subject detail
|Name|regulation-logistics-structure-organization|
|----|----|
|Title|Merged module src/regulation.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/logistics/structure-organization/onto.ttl|
|Composition|- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)<br/>- [Modelet logistics/structure-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL TC Profile compatible|
|Description|The subject is included in the OWL TC sublanguage|

***
### Pass Assertion number 5

[Jump to summary definition](#summary-Pass-5)

:white_check_mark:Pass assertion
#### Subject detail
|Name|regulation-logistics-structure-organization|
|----|----|
|Title|Merged module src/regulation.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/logistics/structure-organization/onto.ttl|
|Composition|- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)<br/>- [Modelet logistics/structure-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL RL Profile compatible|
|Description|The subject is included in the OWL RL sublanguage|

***
### Pass Assertion number 6

[Jump to summary definition](#summary-Pass-6)

:white_check_mark:Pass assertion
#### Subject detail
|Name|regulation-logistics-structure-organization|
|----|----|
|Title|Merged module src/regulation.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/logistics/structure-organization/onto.ttl|
|Composition|- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)<br/>- [Modelet logistics/structure-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL QL Profile compatible|
|Description|The subject is included in the OWL QL sublanguage|

***
### Pass Assertion number 7

[Jump to summary definition](#summary-Pass-7)

:white_check_mark:Pass assertion
#### Subject detail
|Name|regulation-logistics-structure-organization|
|----|----|
|Title|Merged module src/regulation.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/logistics/structure-organization/onto.ttl|
|Composition|- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)<br/>- [Modelet logistics/structure-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL EL Profile compatible|
|Description|The subject is included in the OWL EL sublanguage|

***
### Pass Assertion number 8

[Jump to summary definition](#summary-Pass-8)

:white_check_mark:Pass assertion
#### Subject detail
|Name|regulation-logistics-structure-organization|
|----|----|
|Title|Merged module src/regulation.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/logistics/structure-organization/onto.ttl|
|Composition|- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)<br/>- [Modelet logistics/structure-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#term-referencing)|
|----|----|
|Title|Term referencing test|
|Description|A test case from the Best Practices tests checking if each term of the test subject is referenced to a module through a rdfs:isDefinedBy property.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Any term is referenced|
|Description|Each term of the test subject is linked to a module by a rdfs:isDefinedBy property|

***
### Pass Assertion number 9

[Jump to summary definition](#summary-Pass-9)

:white_check_mark:Pass assertion
#### Subject detail
|Name|regulation-logistics-create-organization|
|----|----|
|Title|Merged module src/regulation.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/logistics/create-organization/onto.ttl|
|Composition|- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)<br/>- [Modelet logistics/create-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/create-organization/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Domains properly defined|
|Description|Each rdfs:domain is defined within the fragment|

***
### Pass Assertion number 10

[Jump to summary definition](#summary-Pass-10)

:white_check_mark:Pass assertion
#### Subject detail
|Name|regulation-logistics-create-organization|
|----|----|
|Title|Merged module src/regulation.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/logistics/create-organization/onto.ttl|
|Composition|- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)<br/>- [Modelet logistics/create-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/create-organization/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Ranges properly defined|
|Description|Each rdfs:range is defined within the fragment|

***
### Pass Assertion number 11

[Jump to summary definition](#summary-Pass-11)

:white_check_mark:Pass assertion
#### Subject detail
|Name|regulation-logistics-create-organization|
|----|----|
|Title|Merged module src/regulation.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/logistics/create-organization/onto.ttl|
|Composition|- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)<br/>- [Modelet logistics/create-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/create-organization/onto.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#owl-rl-constraint)|
|----|----|
|Title|OWL RL Constraint test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL RL consistent|
|Description|The provided graph is consistent for any OWL RL constraint|

***
### Pass Assertion number 12

[Jump to summary definition](#summary-Pass-12)

:white_check_mark:Pass assertion
#### Subject detail
|Name|regulation-logistics-create-organization|
|----|----|
|Title|Merged module src/regulation.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/logistics/create-organization/onto.ttl|
|Composition|- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)<br/>- [Modelet logistics/create-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/create-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL TC Profile compatible|
|Description|The subject is included in the OWL TC sublanguage|

***
### Pass Assertion number 13

[Jump to summary definition](#summary-Pass-13)

:white_check_mark:Pass assertion
#### Subject detail
|Name|regulation-logistics-create-organization|
|----|----|
|Title|Merged module src/regulation.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/logistics/create-organization/onto.ttl|
|Composition|- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)<br/>- [Modelet logistics/create-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/create-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL RL Profile compatible|
|Description|The subject is included in the OWL RL sublanguage|

***
### Pass Assertion number 14

[Jump to summary definition](#summary-Pass-14)

:white_check_mark:Pass assertion
#### Subject detail
|Name|regulation-logistics-create-organization|
|----|----|
|Title|Merged module src/regulation.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/logistics/create-organization/onto.ttl|
|Composition|- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)<br/>- [Modelet logistics/create-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/create-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL QL Profile compatible|
|Description|The subject is included in the OWL QL sublanguage|

***
### Pass Assertion number 15

[Jump to summary definition](#summary-Pass-15)

:white_check_mark:Pass assertion
#### Subject detail
|Name|regulation-logistics-create-organization|
|----|----|
|Title|Merged module src/regulation.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/logistics/create-organization/onto.ttl|
|Composition|- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)<br/>- [Modelet logistics/create-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/create-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL EL Profile compatible|
|Description|The subject is included in the OWL EL sublanguage|

***
### Pass Assertion number 16

[Jump to summary definition](#summary-Pass-16)

:white_check_mark:Pass assertion
#### Subject detail
|Name|regulation-logistics-create-organization|
|----|----|
|Title|Merged module src/regulation.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/logistics/create-organization/onto.ttl|
|Composition|- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)<br/>- [Modelet logistics/create-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/create-organization/onto.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#term-referencing)|
|----|----|
|Title|Term referencing test|
|Description|A test case from the Best Practices tests checking if each term of the test subject is referenced to a module through a rdfs:isDefinedBy property.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Any term is referenced|
|Description|Each term of the test subject is linked to a module by a rdfs:isDefinedBy property|

***
### Pass Assertion number 17

[Jump to summary definition](#summary-Pass-17)

:white_check_mark:Pass assertion
#### Subject detail
|Name|regulation|
|----|----|
|Title|Standalone module src/regulation.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Domains properly defined|
|Description|Each rdfs:domain is defined within the fragment|

***
### Pass Assertion number 18

[Jump to summary definition](#summary-Pass-18)

:white_check_mark:Pass assertion
#### Subject detail
|Name|regulation|
|----|----|
|Title|Standalone module src/regulation.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Ranges properly defined|
|Description|Each rdfs:range is defined within the fragment|

***
### Pass Assertion number 19

[Jump to summary definition](#summary-Pass-19)

:white_check_mark:Pass assertion
#### Subject detail
|Name|regulation|
|----|----|
|Title|Standalone module src/regulation.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#owl-rl-constraint)|
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
|Name|regulation|
|----|----|
|Title|Standalone module src/regulation.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL TC Profile compatible|
|Description|The subject is included in the OWL TC sublanguage|

***
### Pass Assertion number 21

[Jump to summary definition](#summary-Pass-21)

:white_check_mark:Pass assertion
#### Subject detail
|Name|regulation|
|----|----|
|Title|Standalone module src/regulation.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL RL Profile compatible|
|Description|The subject is included in the OWL RL sublanguage|

***
### Pass Assertion number 22

[Jump to summary definition](#summary-Pass-22)

:white_check_mark:Pass assertion
#### Subject detail
|Name|regulation|
|----|----|
|Title|Standalone module src/regulation.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL QL Profile compatible|
|Description|The subject is included in the OWL QL sublanguage|

***
### Pass Assertion number 23

[Jump to summary definition](#summary-Pass-23)

:white_check_mark:Pass assertion
#### Subject detail
|Name|regulation|
|----|----|
|Title|Standalone module src/regulation.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL EL Profile compatible|
|Description|The subject is included in the OWL EL sublanguage|

***
### Pass Assertion number 24

[Jump to summary definition](#summary-Pass-24)

:white_check_mark:Pass assertion
#### Subject detail
|Name|regulation|
|----|----|
|Title|Standalone module src/regulation.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#term-referencing)|
|----|----|
|Title|Term referencing test|
|Description|A test case from the Best Practices tests checking if each term of the test subject is referenced to a module through a rdfs:isDefinedBy property.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Any term is referenced|
|Description|Each term of the test subject is linked to a module by a rdfs:isDefinedBy property|

***
### Pass Assertion number 25

[Jump to summary definition](#summary-Pass-25)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-signifiers|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/discover-signifiers/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#owl-rl-constraint)|
|----|----|
|Title|OWL RL Constraint test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL RL consistent|
|Description|The provided graph is consistent for any OWL RL constraint|

***
### Pass Assertion number 26

[Jump to summary definition](#summary-Pass-26)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-signifiers|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/discover-signifiers/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL TC Profile compatible|
|Description|The subject is included in the OWL TC sublanguage|

***
### Pass Assertion number 27

[Jump to summary definition](#summary-Pass-27)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-signifiers|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/discover-signifiers/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL RL Profile compatible|
|Description|The subject is included in the OWL RL sublanguage|

***
### Pass Assertion number 28

[Jump to summary definition](#summary-Pass-28)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-signifiers|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/discover-signifiers/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#term-referencing)|
|----|----|
|Title|Term referencing test|
|Description|A test case from the Best Practices tests checking if each term of the test subject is referenced to a module through a rdfs:isDefinedBy property.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Any term is referenced|
|Description|Each term of the test subject is linked to a module by a rdfs:isDefinedBy property|

***
### Pass Assertion number 29

[Jump to summary definition](#summary-Pass-29)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-signifiers|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/discover-signifiers/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#terms-differenciation)|
|----|----|
|Title|Terms differenciation test|
|Description|A test case from the Best Practices tests checking if all the terms are different enough from each other according to the Levenshtein distance metric.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Terms differenciated enough|
|Description|All the terms have have a satisfying Levenshtein distance from each other term.|

***
### Pass Assertion number 30

[Jump to summary definition](#summary-Pass-30)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-platforms|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/discover-platforms/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/discover-platforms/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-platforms/onto.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|
|----|----|
|Title|Term labeling test|
|Description|A test case from the Best Practices tests checking if all the terms of the subject have a rdfs:label property pointing to a literal in English|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|All terms labeled|
|Description|All the terms defined in the subject have a rdfs:label in English|

***
### Pass Assertion number 31

[Jump to summary definition](#summary-Pass-31)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-platforms|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/discover-platforms/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/discover-platforms/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-platforms/onto.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#owl-rl-constraint)|
|----|----|
|Title|OWL RL Constraint test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL RL consistent|
|Description|The provided graph is consistent for any OWL RL constraint|

***
### Pass Assertion number 32

[Jump to summary definition](#summary-Pass-32)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-platforms|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/discover-platforms/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/discover-platforms/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-platforms/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL TC Profile compatible|
|Description|The subject is included in the OWL TC sublanguage|

***
### Pass Assertion number 33

[Jump to summary definition](#summary-Pass-33)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-platforms|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/discover-platforms/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/discover-platforms/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-platforms/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL RL Profile compatible|
|Description|The subject is included in the OWL RL sublanguage|

***
### Pass Assertion number 34

[Jump to summary definition](#summary-Pass-34)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-platforms|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/discover-platforms/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/discover-platforms/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-platforms/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL QL Profile compatible|
|Description|The subject is included in the OWL QL sublanguage|

***
### Pass Assertion number 35

[Jump to summary definition](#summary-Pass-35)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-platforms|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/discover-platforms/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/discover-platforms/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-platforms/onto.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#term-referencing)|
|----|----|
|Title|Term referencing test|
|Description|A test case from the Best Practices tests checking if each term of the test subject is referenced to a module through a rdfs:isDefinedBy property.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Any term is referenced|
|Description|Each term of the test subject is linked to a module by a rdfs:isDefinedBy property|

***
### Pass Assertion number 36

[Jump to summary definition](#summary-Pass-36)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-platforms|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/discover-platforms/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/discover-platforms/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-platforms/onto.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#terms-differenciation)|
|----|----|
|Title|Terms differenciation test|
|Description|A test case from the Best Practices tests checking if all the terms are different enough from each other according to the Levenshtein distance metric.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Terms differenciated enough|
|Description|All the terms have have a satisfying Levenshtein distance from each other term.|

***
### Pass Assertion number 37

[Jump to summary definition](#summary-Pass-37)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-organization|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/discover-organization/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/discover-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-organization/onto.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|
|----|----|
|Title|Term labeling test|
|Description|A test case from the Best Practices tests checking if all the terms of the subject have a rdfs:label property pointing to a literal in English|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|All terms labeled|
|Description|All the terms defined in the subject have a rdfs:label in English|

***
### Pass Assertion number 38

[Jump to summary definition](#summary-Pass-38)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-organization|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/discover-organization/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/discover-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-organization/onto.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#owl-rl-constraint)|
|----|----|
|Title|OWL RL Constraint test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL RL consistent|
|Description|The provided graph is consistent for any OWL RL constraint|

***
### Pass Assertion number 39

[Jump to summary definition](#summary-Pass-39)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-organization|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/discover-organization/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/discover-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL TC Profile compatible|
|Description|The subject is included in the OWL TC sublanguage|

***
### Pass Assertion number 40

[Jump to summary definition](#summary-Pass-40)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-organization|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/discover-organization/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/discover-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL RL Profile compatible|
|Description|The subject is included in the OWL RL sublanguage|

***
### Pass Assertion number 41

[Jump to summary definition](#summary-Pass-41)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-organization|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/discover-organization/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/discover-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL QL Profile compatible|
|Description|The subject is included in the OWL QL sublanguage|

***
### Pass Assertion number 42

[Jump to summary definition](#summary-Pass-42)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-organization|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/discover-organization/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/discover-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL EL Profile compatible|
|Description|The subject is included in the OWL EL sublanguage|

***
### Pass Assertion number 43

[Jump to summary definition](#summary-Pass-43)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-organization|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/discover-organization/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/discover-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-organization/onto.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#term-referencing)|
|----|----|
|Title|Term referencing test|
|Description|A test case from the Best Practices tests checking if each term of the test subject is referenced to a module through a rdfs:isDefinedBy property.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Any term is referenced|
|Description|Each term of the test subject is linked to a module by a rdfs:isDefinedBy property|

***
### Pass Assertion number 44

[Jump to summary definition](#summary-Pass-44)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-organization|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/discover-organization/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/discover-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-organization/onto.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#terms-differenciation)|
|----|----|
|Title|Terms differenciation test|
|Description|A test case from the Best Practices tests checking if all the terms are different enough from each other according to the Levenshtein distance metric.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Terms differenciated enough|
|Description|All the terms have have a satisfying Levenshtein distance from each other term.|

***
### Pass Assertion number 45

[Jump to summary definition](#summary-Pass-45)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-core|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/discover-core/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/discover-core/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-core/onto.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|
|----|----|
|Title|Term labeling test|
|Description|A test case from the Best Practices tests checking if all the terms of the subject have a rdfs:label property pointing to a literal in English|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|All terms labeled|
|Description|All the terms defined in the subject have a rdfs:label in English|

***
### Pass Assertion number 46

[Jump to summary definition](#summary-Pass-46)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-core|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/discover-core/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/discover-core/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-core/onto.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#owl-rl-constraint)|
|----|----|
|Title|OWL RL Constraint test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL RL consistent|
|Description|The provided graph is consistent for any OWL RL constraint|

***
### Pass Assertion number 47

[Jump to summary definition](#summary-Pass-47)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-core|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/discover-core/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/discover-core/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-core/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL TC Profile compatible|
|Description|The subject is included in the OWL TC sublanguage|

***
### Pass Assertion number 48

[Jump to summary definition](#summary-Pass-48)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-core|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/discover-core/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/discover-core/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-core/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL RL Profile compatible|
|Description|The subject is included in the OWL RL sublanguage|

***
### Pass Assertion number 49

[Jump to summary definition](#summary-Pass-49)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-core|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/discover-core/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/discover-core/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-core/onto.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#term-referencing)|
|----|----|
|Title|Term referencing test|
|Description|A test case from the Best Practices tests checking if each term of the test subject is referenced to a module through a rdfs:isDefinedBy property.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Any term is referenced|
|Description|Each term of the test subject is linked to a module by a rdfs:isDefinedBy property|

***
### Pass Assertion number 50

[Jump to summary definition](#summary-Pass-50)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-core|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/discover-core/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/discover-core/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-core/onto.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#terms-differenciation)|
|----|----|
|Title|Terms differenciation test|
|Description|A test case from the Best Practices tests checking if all the terms are different enough from each other according to the Levenshtein distance metric.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Terms differenciated enough|
|Description|All the terms have have a satisfying Levenshtein distance from each other term.|

***
### Pass Assertion number 51

[Jump to summary definition](#summary-Pass-51)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/discover-behavior-specifications/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/discover-behavior-specifications/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|
|----|----|
|Title|Term labeling test|
|Description|A test case from the Best Practices tests checking if all the terms of the subject have a rdfs:label property pointing to a literal in English|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|All terms labeled|
|Description|All the terms defined in the subject have a rdfs:label in English|

***
### Pass Assertion number 52

[Jump to summary definition](#summary-Pass-52)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/discover-behavior-specifications/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/discover-behavior-specifications/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#owl-rl-constraint)|
|----|----|
|Title|OWL RL Constraint test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL RL consistent|
|Description|The provided graph is consistent for any OWL RL constraint|

***
### Pass Assertion number 53

[Jump to summary definition](#summary-Pass-53)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/discover-behavior-specifications/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/discover-behavior-specifications/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL TC Profile compatible|
|Description|The subject is included in the OWL TC sublanguage|

***
### Pass Assertion number 54

[Jump to summary definition](#summary-Pass-54)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/discover-behavior-specifications/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/discover-behavior-specifications/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL RL Profile compatible|
|Description|The subject is included in the OWL RL sublanguage|

***
### Pass Assertion number 55

[Jump to summary definition](#summary-Pass-55)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/discover-behavior-specifications/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/discover-behavior-specifications/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL QL Profile compatible|
|Description|The subject is included in the OWL QL sublanguage|

***
### Pass Assertion number 56

[Jump to summary definition](#summary-Pass-56)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/discover-behavior-specifications/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/discover-behavior-specifications/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL EL Profile compatible|
|Description|The subject is included in the OWL EL sublanguage|

***
### Pass Assertion number 57

[Jump to summary definition](#summary-Pass-57)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/discover-behavior-specifications/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/discover-behavior-specifications/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#term-referencing)|
|----|----|
|Title|Term referencing test|
|Description|A test case from the Best Practices tests checking if each term of the test subject is referenced to a module through a rdfs:isDefinedBy property.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Any term is referenced|
|Description|Each term of the test subject is linked to a module by a rdfs:isDefinedBy property|

***
### Pass Assertion number 58

[Jump to summary definition](#summary-Pass-58)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Standalone modelet domains/manufacturing-environments/discover-behavior-specifications/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet manufacturing-environments/discover-behavior-specifications/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#terms-differenciation)|
|----|----|
|Title|Terms differenciation test|
|Description|A test case from the Best Practices tests checking if all the terms are different enough from each other according to the Levenshtein distance metric.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Terms differenciated enough|
|Description|All the terms have have a satisfying Levenshtein distance from each other term.|

***
### Pass Assertion number 59

[Jump to summary definition](#summary-Pass-59)

:white_check_mark:Pass assertion
#### Subject detail
|Name|logistics-structure-organization|
|----|----|
|Title|Standalone modelet domains/logistics/structure-organization/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet logistics/structure-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[labeled-terms](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#labeled-terms)|
|----|----|
|Title|Term labeling test|
|Description|A test case from the Best Practices tests checking if all the terms of the subject have a rdfs:label property pointing to a literal in English|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|All terms labeled|
|Description|All the terms defined in the subject have a rdfs:label in English|

***
### Pass Assertion number 60

[Jump to summary definition](#summary-Pass-60)

:white_check_mark:Pass assertion
#### Subject detail
|Name|logistics-structure-organization|
|----|----|
|Title|Standalone modelet domains/logistics/structure-organization/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet logistics/structure-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#owl-rl-constraint)|
|----|----|
|Title|OWL RL Constraint test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL RL consistent|
|Description|The provided graph is consistent for any OWL RL constraint|

***
### Pass Assertion number 61

[Jump to summary definition](#summary-Pass-61)

:white_check_mark:Pass assertion
#### Subject detail
|Name|logistics-structure-organization|
|----|----|
|Title|Standalone modelet domains/logistics/structure-organization/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet logistics/structure-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL TC Profile compatible|
|Description|The subject is included in the OWL TC sublanguage|

***
### Pass Assertion number 62

[Jump to summary definition](#summary-Pass-62)

:white_check_mark:Pass assertion
#### Subject detail
|Name|logistics-structure-organization|
|----|----|
|Title|Standalone modelet domains/logistics/structure-organization/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet logistics/structure-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL RL Profile compatible|
|Description|The subject is included in the OWL RL sublanguage|

***
### Pass Assertion number 63

[Jump to summary definition](#summary-Pass-63)

:white_check_mark:Pass assertion
#### Subject detail
|Name|logistics-structure-organization|
|----|----|
|Title|Standalone modelet domains/logistics/structure-organization/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet logistics/structure-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL QL Profile compatible|
|Description|The subject is included in the OWL QL sublanguage|

***
### Pass Assertion number 64

[Jump to summary definition](#summary-Pass-64)

:white_check_mark:Pass assertion
#### Subject detail
|Name|logistics-structure-organization|
|----|----|
|Title|Standalone modelet domains/logistics/structure-organization/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet logistics/structure-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL EL Profile compatible|
|Description|The subject is included in the OWL EL sublanguage|

***
### Pass Assertion number 65

[Jump to summary definition](#summary-Pass-65)

:white_check_mark:Pass assertion
#### Subject detail
|Name|logistics-structure-organization|
|----|----|
|Title|Standalone modelet domains/logistics/structure-organization/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet logistics/structure-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#term-referencing)|
|----|----|
|Title|Term referencing test|
|Description|A test case from the Best Practices tests checking if each term of the test subject is referenced to a module through a rdfs:isDefinedBy property.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Any term is referenced|
|Description|Each term of the test subject is linked to a module by a rdfs:isDefinedBy property|

***
### Pass Assertion number 66

[Jump to summary definition](#summary-Pass-66)

:white_check_mark:Pass assertion
#### Subject detail
|Name|logistics-create-organization|
|----|----|
|Title|Standalone modelet domains/logistics/create-organization/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet logistics/create-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/create-organization/onto.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#owl-rl-constraint)|
|----|----|
|Title|OWL RL Constraint test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL RL consistent|
|Description|The provided graph is consistent for any OWL RL constraint|

***
### Pass Assertion number 67

[Jump to summary definition](#summary-Pass-67)

:white_check_mark:Pass assertion
#### Subject detail
|Name|logistics-create-organization|
|----|----|
|Title|Standalone modelet domains/logistics/create-organization/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet logistics/create-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/create-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL TC Profile compatible|
|Description|The subject is included in the OWL TC sublanguage|

***
### Pass Assertion number 68

[Jump to summary definition](#summary-Pass-68)

:white_check_mark:Pass assertion
#### Subject detail
|Name|logistics-create-organization|
|----|----|
|Title|Standalone modelet domains/logistics/create-organization/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet logistics/create-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/create-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL RL Profile compatible|
|Description|The subject is included in the OWL RL sublanguage|

***
### Pass Assertion number 69

[Jump to summary definition](#summary-Pass-69)

:white_check_mark:Pass assertion
#### Subject detail
|Name|logistics-create-organization|
|----|----|
|Title|Standalone modelet domains/logistics/create-organization/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet logistics/create-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/create-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL QL Profile compatible|
|Description|The subject is included in the OWL QL sublanguage|

***
### Pass Assertion number 70

[Jump to summary definition](#summary-Pass-70)

:white_check_mark:Pass assertion
#### Subject detail
|Name|logistics-create-organization|
|----|----|
|Title|Standalone modelet domains/logistics/create-organization/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet logistics/create-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/create-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL EL Profile compatible|
|Description|The subject is included in the OWL EL sublanguage|

***
### Pass Assertion number 71

[Jump to summary definition](#summary-Pass-71)

:white_check_mark:Pass assertion
#### Subject detail
|Name|logistics-create-organization|
|----|----|
|Title|Standalone modelet domains/logistics/create-organization/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet logistics/create-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/create-organization/onto.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#term-referencing)|
|----|----|
|Title|Term referencing test|
|Description|A test case from the Best Practices tests checking if each term of the test subject is referenced to a module through a rdfs:isDefinedBy property.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Any term is referenced|
|Description|Each term of the test subject is linked to a module by a rdfs:isDefinedBy property|

***
### Pass Assertion number 72

[Jump to summary definition](#summary-Pass-72)

:white_check_mark:Pass assertion
#### Subject detail
|Name|logistics-create-organization|
|----|----|
|Title|Standalone modelet domains/logistics/create-organization/onto.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Modelet logistics/create-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/create-organization/onto.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#terms-differenciation)|
|----|----|
|Title|Terms differenciation test|
|Description|A test case from the Best Practices tests checking if all the terms are different enough from each other according to the Levenshtein distance metric.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Terms differenciated enough|
|Description|All the terms have have a satisfying Levenshtein distance from each other term.|

***
### Pass Assertion number 73

[Jump to summary definition](#summary-Pass-73)

:white_check_mark:Pass assertion
#### Subject detail
|Name|interaction-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Merged module src/interaction.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-behavior-specifications/onto.ttl|
|Composition|- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Modelet manufacturing-environments/discover-behavior-specifications/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Domains properly defined|
|Description|Each rdfs:domain is defined within the fragment|

***
### Pass Assertion number 74

[Jump to summary definition](#summary-Pass-74)

:white_check_mark:Pass assertion
#### Subject detail
|Name|interaction-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Merged module src/interaction.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-behavior-specifications/onto.ttl|
|Composition|- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Modelet manufacturing-environments/discover-behavior-specifications/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Ranges properly defined|
|Description|Each rdfs:range is defined within the fragment|

***
### Pass Assertion number 75

[Jump to summary definition](#summary-Pass-75)

:white_check_mark:Pass assertion
#### Subject detail
|Name|interaction-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Merged module src/interaction.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-behavior-specifications/onto.ttl|
|Composition|- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Modelet manufacturing-environments/discover-behavior-specifications/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#owl-rl-constraint)|
|----|----|
|Title|OWL RL Constraint test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL RL consistent|
|Description|The provided graph is consistent for any OWL RL constraint|

***
### Pass Assertion number 76

[Jump to summary definition](#summary-Pass-76)

:white_check_mark:Pass assertion
#### Subject detail
|Name|interaction-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Merged module src/interaction.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-behavior-specifications/onto.ttl|
|Composition|- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Modelet manufacturing-environments/discover-behavior-specifications/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL TC Profile compatible|
|Description|The subject is included in the OWL TC sublanguage|

***
### Pass Assertion number 77

[Jump to summary definition](#summary-Pass-77)

:white_check_mark:Pass assertion
#### Subject detail
|Name|interaction-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Merged module src/interaction.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-behavior-specifications/onto.ttl|
|Composition|- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Modelet manufacturing-environments/discover-behavior-specifications/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL RL Profile compatible|
|Description|The subject is included in the OWL RL sublanguage|

***
### Pass Assertion number 78

[Jump to summary definition](#summary-Pass-78)

:white_check_mark:Pass assertion
#### Subject detail
|Name|interaction-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Merged module src/interaction.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-behavior-specifications/onto.ttl|
|Composition|- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Modelet manufacturing-environments/discover-behavior-specifications/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL QL Profile compatible|
|Description|The subject is included in the OWL QL sublanguage|

***
### Pass Assertion number 79

[Jump to summary definition](#summary-Pass-79)

:white_check_mark:Pass assertion
#### Subject detail
|Name|interaction-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Merged module src/interaction.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-behavior-specifications/onto.ttl|
|Composition|- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Modelet manufacturing-environments/discover-behavior-specifications/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL EL Profile compatible|
|Description|The subject is included in the OWL EL sublanguage|

***
### Pass Assertion number 80

[Jump to summary definition](#summary-Pass-80)

:white_check_mark:Pass assertion
#### Subject detail
|Name|interaction-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Merged module src/interaction.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-behavior-specifications/onto.ttl|
|Composition|- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Modelet manufacturing-environments/discover-behavior-specifications/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#term-referencing)|
|----|----|
|Title|Term referencing test|
|Description|A test case from the Best Practices tests checking if each term of the test subject is referenced to a module through a rdfs:isDefinedBy property.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Any term is referenced|
|Description|Each term of the test subject is linked to a module by a rdfs:isDefinedBy property|

***
### Pass Assertion number 81

[Jump to summary definition](#summary-Pass-81)

:white_check_mark:Pass assertion
#### Subject detail
|Name|interaction-manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Merged module src/interaction.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-behavior-specifications/onto.ttl|
|Composition|- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Modelet manufacturing-environments/discover-behavior-specifications/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#terms-differenciation)|
|----|----|
|Title|Terms differenciation test|
|Description|A test case from the Best Practices tests checking if all the terms are different enough from each other according to the Levenshtein distance metric.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Terms differenciated enough|
|Description|All the terms have have a satisfying Levenshtein distance from each other term.|

***
### Pass Assertion number 82

[Jump to summary definition](#summary-Pass-82)

:white_check_mark:Pass assertion
#### Subject detail
|Name|interaction|
|----|----|
|Title|Standalone module src/interaction.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Domains properly defined|
|Description|Each rdfs:domain is defined within the fragment|

***
### Pass Assertion number 83

[Jump to summary definition](#summary-Pass-83)

:white_check_mark:Pass assertion
#### Subject detail
|Name|interaction|
|----|----|
|Title|Standalone module src/interaction.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Ranges properly defined|
|Description|Each rdfs:range is defined within the fragment|

***
### Pass Assertion number 84

[Jump to summary definition](#summary-Pass-84)

:white_check_mark:Pass assertion
#### Subject detail
|Name|interaction|
|----|----|
|Title|Standalone module src/interaction.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#owl-rl-constraint)|
|----|----|
|Title|OWL RL Constraint test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL RL consistent|
|Description|The provided graph is consistent for any OWL RL constraint|

***
### Pass Assertion number 85

[Jump to summary definition](#summary-Pass-85)

:white_check_mark:Pass assertion
#### Subject detail
|Name|interaction|
|----|----|
|Title|Standalone module src/interaction.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL TC Profile compatible|
|Description|The subject is included in the OWL TC sublanguage|

***
### Pass Assertion number 86

[Jump to summary definition](#summary-Pass-86)

:white_check_mark:Pass assertion
#### Subject detail
|Name|interaction|
|----|----|
|Title|Standalone module src/interaction.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL RL Profile compatible|
|Description|The subject is included in the OWL RL sublanguage|

***
### Pass Assertion number 87

[Jump to summary definition](#summary-Pass-87)

:white_check_mark:Pass assertion
#### Subject detail
|Name|interaction|
|----|----|
|Title|Standalone module src/interaction.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL QL Profile compatible|
|Description|The subject is included in the OWL QL sublanguage|

***
### Pass Assertion number 88

[Jump to summary definition](#summary-Pass-88)

:white_check_mark:Pass assertion
#### Subject detail
|Name|interaction|
|----|----|
|Title|Standalone module src/interaction.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL EL Profile compatible|
|Description|The subject is included in the OWL EL sublanguage|

***
### Pass Assertion number 89

[Jump to summary definition](#summary-Pass-89)

:white_check_mark:Pass assertion
#### Subject detail
|Name|interaction|
|----|----|
|Title|Standalone module src/interaction.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#term-referencing)|
|----|----|
|Title|Term referencing test|
|Description|A test case from the Best Practices tests checking if each term of the test subject is referenced to a module through a rdfs:isDefinedBy property.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Any term is referenced|
|Description|Each term of the test subject is linked to a module by a rdfs:isDefinedBy property|

***
### Pass Assertion number 90

[Jump to summary definition](#summary-Pass-90)

:white_check_mark:Pass assertion
#### Subject detail
|Name|interaction|
|----|----|
|Title|Standalone module src/interaction.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#terms-differenciation)|
|----|----|
|Title|Terms differenciation test|
|Description|A test case from the Best Practices tests checking if all the terms are different enough from each other according to the Levenshtein distance metric.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Terms differenciated enough|
|Description|All the terms have have a satisfying Levenshtein distance from each other term.|

***
### Pass Assertion number 91

[Jump to summary definition](#summary-Pass-91)

:white_check_mark:Pass assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-signifiers/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Domains properly defined|
|Description|Each rdfs:domain is defined within the fragment|

***
### Pass Assertion number 92

[Jump to summary definition](#summary-Pass-92)

:white_check_mark:Pass assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-signifiers/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Ranges properly defined|
|Description|Each rdfs:range is defined within the fragment|

***
### Pass Assertion number 93

[Jump to summary definition](#summary-Pass-93)

:white_check_mark:Pass assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-signifiers/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#owl-rl-constraint)|
|----|----|
|Title|OWL RL Constraint test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL RL consistent|
|Description|The provided graph is consistent for any OWL RL constraint|

***
### Pass Assertion number 94

[Jump to summary definition](#summary-Pass-94)

:white_check_mark:Pass assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-signifiers/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL TC Profile compatible|
|Description|The subject is included in the OWL TC sublanguage|

***
### Pass Assertion number 95

[Jump to summary definition](#summary-Pass-95)

:white_check_mark:Pass assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-signifiers/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL RL Profile compatible|
|Description|The subject is included in the OWL RL sublanguage|

***
### Pass Assertion number 96

[Jump to summary definition](#summary-Pass-96)

:white_check_mark:Pass assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-signifiers/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#term-referencing)|
|----|----|
|Title|Term referencing test|
|Description|A test case from the Best Practices tests checking if each term of the test subject is referenced to a module through a rdfs:isDefinedBy property.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Any term is referenced|
|Description|Each term of the test subject is linked to a module by a rdfs:isDefinedBy property|

***
### Pass Assertion number 97

[Jump to summary definition](#summary-Pass-97)

:white_check_mark:Pass assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-signifiers|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-signifiers/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#terms-differenciation)|
|----|----|
|Title|Terms differenciation test|
|Description|A test case from the Best Practices tests checking if all the terms are different enough from each other according to the Levenshtein distance metric.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Terms differenciated enough|
|Description|All the terms have have a satisfying Levenshtein distance from each other term.|

***
### Pass Assertion number 98

[Jump to summary definition](#summary-Pass-98)

:white_check_mark:Pass assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-platforms|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-platforms/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-platforms/onto.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#owl-rl-constraint)|
|----|----|
|Title|OWL RL Constraint test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL RL consistent|
|Description|The provided graph is consistent for any OWL RL constraint|

***
### Pass Assertion number 99

[Jump to summary definition](#summary-Pass-99)

:white_check_mark:Pass assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-platforms|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-platforms/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-platforms/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL TC Profile compatible|
|Description|The subject is included in the OWL TC sublanguage|

***
### Pass Assertion number 100

[Jump to summary definition](#summary-Pass-100)

:white_check_mark:Pass assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-platforms|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-platforms/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-platforms/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL RL Profile compatible|
|Description|The subject is included in the OWL RL sublanguage|

***
### Pass Assertion number 101

[Jump to summary definition](#summary-Pass-101)

:white_check_mark:Pass assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-platforms|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-platforms/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-platforms/onto.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#term-referencing)|
|----|----|
|Title|Term referencing test|
|Description|A test case from the Best Practices tests checking if each term of the test subject is referenced to a module through a rdfs:isDefinedBy property.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Any term is referenced|
|Description|Each term of the test subject is linked to a module by a rdfs:isDefinedBy property|

***
### Pass Assertion number 102

[Jump to summary definition](#summary-Pass-102)

:white_check_mark:Pass assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-platforms|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-platforms/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-platforms/onto.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#terms-differenciation)|
|----|----|
|Title|Terms differenciation test|
|Description|A test case from the Best Practices tests checking if all the terms are different enough from each other according to the Levenshtein distance metric.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Terms differenciated enough|
|Description|All the terms have have a satisfying Levenshtein distance from each other term.|

***
### Pass Assertion number 103

[Jump to summary definition](#summary-Pass-103)

:white_check_mark:Pass assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-organization|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-organization/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-organization/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Domains properly defined|
|Description|Each rdfs:domain is defined within the fragment|

***
### Pass Assertion number 104

[Jump to summary definition](#summary-Pass-104)

:white_check_mark:Pass assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-organization|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-organization/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-organization/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Ranges properly defined|
|Description|Each rdfs:range is defined within the fragment|

***
### Pass Assertion number 105

[Jump to summary definition](#summary-Pass-105)

:white_check_mark:Pass assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-organization|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-organization/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-organization/onto.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#owl-rl-constraint)|
|----|----|
|Title|OWL RL Constraint test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL RL consistent|
|Description|The provided graph is consistent for any OWL RL constraint|

***
### Pass Assertion number 106

[Jump to summary definition](#summary-Pass-106)

:white_check_mark:Pass assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-organization|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-organization/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL TC Profile compatible|
|Description|The subject is included in the OWL TC sublanguage|

***
### Pass Assertion number 107

[Jump to summary definition](#summary-Pass-107)

:white_check_mark:Pass assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-organization|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-organization/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL RL Profile compatible|
|Description|The subject is included in the OWL RL sublanguage|

***
### Pass Assertion number 108

[Jump to summary definition](#summary-Pass-108)

:white_check_mark:Pass assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-organization|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-organization/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-organization/onto.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#term-referencing)|
|----|----|
|Title|Term referencing test|
|Description|A test case from the Best Practices tests checking if each term of the test subject is referenced to a module through a rdfs:isDefinedBy property.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Any term is referenced|
|Description|Each term of the test subject is linked to a module by a rdfs:isDefinedBy property|

***
### Pass Assertion number 109

[Jump to summary definition](#summary-Pass-109)

:white_check_mark:Pass assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-organization|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-organization/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-organization/onto.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#terms-differenciation)|
|----|----|
|Title|Terms differenciation test|
|Description|A test case from the Best Practices tests checking if all the terms are different enough from each other according to the Levenshtein distance metric.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Terms differenciated enough|
|Description|All the terms have have a satisfying Levenshtein distance from each other term.|

***
### Pass Assertion number 110

[Jump to summary definition](#summary-Pass-110)

:white_check_mark:Pass assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-core|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-core/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-core/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-core/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Domains properly defined|
|Description|Each rdfs:domain is defined within the fragment|

***
### Pass Assertion number 111

[Jump to summary definition](#summary-Pass-111)

:white_check_mark:Pass assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-core|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-core/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-core/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-core/onto.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Ranges properly defined|
|Description|Each rdfs:range is defined within the fragment|

***
### Pass Assertion number 112

[Jump to summary definition](#summary-Pass-112)

:white_check_mark:Pass assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-core|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-core/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-core/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-core/onto.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#owl-rl-constraint)|
|----|----|
|Title|OWL RL Constraint test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL RL consistent|
|Description|The provided graph is consistent for any OWL RL constraint|

***
### Pass Assertion number 113

[Jump to summary definition](#summary-Pass-113)

:white_check_mark:Pass assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-core|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-core/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-core/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-core/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL TC Profile compatible|
|Description|The subject is included in the OWL TC sublanguage|

***
### Pass Assertion number 114

[Jump to summary definition](#summary-Pass-114)

:white_check_mark:Pass assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-core|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-core/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-core/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-core/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL RL Profile compatible|
|Description|The subject is included in the OWL RL sublanguage|

***
### Pass Assertion number 115

[Jump to summary definition](#summary-Pass-115)

:white_check_mark:Pass assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-core|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-core/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-core/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-core/onto.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#term-referencing)|
|----|----|
|Title|Term referencing test|
|Description|A test case from the Best Practices tests checking if each term of the test subject is referenced to a module through a rdfs:isDefinedBy property.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Any term is referenced|
|Description|Each term of the test subject is linked to a module by a rdfs:isDefinedBy property|

***
### Pass Assertion number 116

[Jump to summary definition](#summary-Pass-116)

:white_check_mark:Pass assertion
#### Subject detail
|Name|core-manufacturing-environments-discover-core|
|----|----|
|Title|Merged module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages with related terms from the fragments domains/manufacturing-environments/discover-core/onto.ttl|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Modelet manufacturing-environments/discover-core/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-core/onto.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#terms-differenciation)|
|----|----|
|Title|Terms differenciation test|
|Description|A test case from the Best Practices tests checking if all the terms are different enough from each other according to the Levenshtein distance metric.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Terms differenciated enough|
|Description|All the terms have have a satisfying Levenshtein distance from each other term.|

***
### Pass Assertion number 117

[Jump to summary definition](#summary-Pass-117)

:white_check_mark:Pass assertion
#### Subject detail
|Name|core|
|----|----|
|Title|Standalone module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Domains properly defined|
|Description|Each rdfs:domain is defined within the fragment|

***
### Pass Assertion number 118

[Jump to summary definition](#summary-Pass-118)

:white_check_mark:Pass assertion
#### Subject detail
|Name|core|
|----|----|
|Title|Standalone module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Ranges properly defined|
|Description|Each rdfs:range is defined within the fragment|

***
### Pass Assertion number 119

[Jump to summary definition](#summary-Pass-119)

:white_check_mark:Pass assertion
#### Subject detail
|Name|core|
|----|----|
|Title|Standalone module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#owl-rl-constraint)|
|----|----|
|Title|OWL RL Constraint test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL RL consistent|
|Description|The provided graph is consistent for any OWL RL constraint|

***
### Pass Assertion number 120

[Jump to summary definition](#summary-Pass-120)

:white_check_mark:Pass assertion
#### Subject detail
|Name|core|
|----|----|
|Title|Standalone module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL TC Profile compatible|
|Description|The subject is included in the OWL TC sublanguage|

***
### Pass Assertion number 121

[Jump to summary definition](#summary-Pass-121)

:white_check_mark:Pass assertion
#### Subject detail
|Name|core|
|----|----|
|Title|Standalone module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL RL Profile compatible|
|Description|The subject is included in the OWL RL sublanguage|

***
### Pass Assertion number 122

[Jump to summary definition](#summary-Pass-122)

:white_check_mark:Pass assertion
#### Subject detail
|Name|core|
|----|----|
|Title|Standalone module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#term-referencing)|
|----|----|
|Title|Term referencing test|
|Description|A test case from the Best Practices tests checking if each term of the test subject is referenced to a module through a rdfs:isDefinedBy property.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Any term is referenced|
|Description|Each term of the test subject is linked to a module by a rdfs:isDefinedBy property|

***
### Pass Assertion number 123

[Jump to summary definition](#summary-Pass-123)

:white_check_mark:Pass assertion
#### Subject detail
|Name|core|
|----|----|
|Title|Standalone module src/core.ttl from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)|

#### Criterion detail
|Identifier|[terms-differenciation](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#terms-differenciation)|
|----|----|
|Title|Terms differenciation test|
|Description|A test case from the Best Practices tests checking if all the terms are different enough from each other according to the Levenshtein distance metric.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Terms differenciated enough|
|Description|All the terms have have a satisfying Levenshtein distance from each other term.|

***
### Pass Assertion number 124

[Jump to summary definition](#summary-Pass-124)

:white_check_mark:Pass assertion
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All the modules from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages that are syntaxically correct as well as their recursive imports|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Domains properly defined|
|Description|Each rdfs:domain is defined within the fragment|

***
### Pass Assertion number 125

[Jump to summary definition](#summary-Pass-125)

:white_check_mark:Pass assertion
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All the modules from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages that are syntaxically correct as well as their recursive imports|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)|

#### Criterion detail
|Identifier|[domain-and-range-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#domain-and-range-referencing)|
|----|----|
|Title|Domain and range referencing test|
|Description|A test case from the Best Practices tests checking if all the ranges and domains from the test subject point to terms that are defined in the vocabulary.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Ranges properly defined|
|Description|Each rdfs:range is defined within the fragment|

***
### Pass Assertion number 126

[Jump to summary definition](#summary-Pass-126)

:white_check_mark:Pass assertion
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All the modules from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages that are syntaxically correct as well as their recursive imports|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#owl-rl-constraint)|
|----|----|
|Title|OWL RL Constraint test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL RL consistent|
|Description|The provided graph is consistent for any OWL RL constraint|

***
### Pass Assertion number 127

[Jump to summary definition](#summary-Pass-127)

:white_check_mark:Pass assertion
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All the modules from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages that are syntaxically correct as well as their recursive imports|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL TC Profile compatible|
|Description|The subject is included in the OWL TC sublanguage|

***
### Pass Assertion number 128

[Jump to summary definition](#summary-Pass-128)

:white_check_mark:Pass assertion
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All the modules from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages that are syntaxically correct as well as their recursive imports|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL RL Profile compatible|
|Description|The subject is included in the OWL RL sublanguage|

***
### Pass Assertion number 129

[Jump to summary definition](#summary-Pass-129)

:white_check_mark:Pass assertion
#### Subject detail
|Name|all-modules|
|----|----|
|Title|All the modules from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages that are syntaxically correct as well as their recursive imports|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#term-referencing)|
|----|----|
|Title|Term referencing test|
|Description|A test case from the Best Practices tests checking if each term of the test subject is referenced to a module through a rdfs:isDefinedBy property.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Any term is referenced|
|Description|Each term of the test subject is linked to a module by a rdfs:isDefinedBy property|

***
### Pass Assertion number 130

[Jump to summary definition](#summary-Pass-130)

:white_check_mark:Pass assertion
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All the fragments from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages that are syntaxically correct as well as their recursive imports|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)<br/>- [Modelet domain-template/scenario-template/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/domain-template/scenario-template/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-behavior-specifications/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-core/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Modelet logistics/create-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/create-organization/onto.ttl)<br/>- [Modelet logistics/structure-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#owl-rl-constraint)|
|----|----|
|Title|OWL RL Constraint test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL RL consistent|
|Description|The provided graph is consistent for any OWL RL constraint|

***
### Pass Assertion number 131

[Jump to summary definition](#summary-Pass-131)

:white_check_mark:Pass assertion
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All the fragments from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages that are syntaxically correct as well as their recursive imports|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)<br/>- [Modelet domain-template/scenario-template/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/domain-template/scenario-template/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-behavior-specifications/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-core/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Modelet logistics/create-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/create-organization/onto.ttl)<br/>- [Modelet logistics/structure-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL TC Profile compatible|
|Description|The subject is included in the OWL TC sublanguage|

***
### Pass Assertion number 132

[Jump to summary definition](#summary-Pass-132)

:white_check_mark:Pass assertion
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All the fragments from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages that are syntaxically correct as well as their recursive imports|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)<br/>- [Modelet domain-template/scenario-template/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/domain-template/scenario-template/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-behavior-specifications/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-core/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Modelet logistics/create-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/create-organization/onto.ttl)<br/>- [Modelet logistics/structure-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[profile-compatibility](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#profile-compatibility)|
|----|----|
|Title|Profile compatibility test|
|Description|A test meant to check whether the test subject is compatible with a profile or not, and if it is not, why.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL RL Profile compatible|
|Description|The subject is included in the OWL RL sublanguage|

***
### Pass Assertion number 133

[Jump to summary definition](#summary-Pass-133)

:white_check_mark:Pass assertion
#### Subject detail
|Name|all-fragments|
|----|----|
|Title|All the fragments from branch 227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages that are syntaxically correct as well as their recursive imports|
|Composition|- [Module core.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/core.ttl)<br/>- [Module interaction.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/interaction.ttl)<br/>- [Module regulation.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/src/regulation.ttl)<br/>- [Modelet domain-template/scenario-template/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/domain-template/scenario-template/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-behavior-specifications/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-behavior-specifications/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-signifiers/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-signifiers/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-core/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-core/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-organization/onto.ttl)<br/>- [Modelet manufacturing-environments/discover-platforms/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/manufacturing-environments/discover-platforms/onto.ttl)<br/>- [Modelet logistics/create-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/create-organization/onto.ttl)<br/>- [Modelet logistics/structure-organization/onto.ttl](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/domains/logistics/structure-organization/onto.ttl)|

#### Criterion detail
|Identifier|[term-referencing](https://github.com/HyperAgents/hmas/blob/227-motivating-scenario-discovery-of-behavior-specifications-for-sending-messages/.acimov/model-test/model-test-onto.ttl#term-referencing)|
|----|----|
|Title|Term referencing test|
|Description|A test case from the Best Practices tests checking if each term of the test subject is referenced to a module through a rdfs:isDefinedBy property.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Any term is referenced|
|Description|Each term of the test subject is linked to a module by a rdfs:isDefinedBy property|

***

</details>

***

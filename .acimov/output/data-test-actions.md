# Test Report Markdown export

This file is an export of the RDF test report made out of [EARL vocabulary](https://www.w3.org/TR/EARL10/)

This test is powered by Corese, check the [website](https://project.inria.fr/corese/) and the [repository](https://github.com/Wimmics/corese)

The original test report is available in turtle syntax [here](./data-test-actions.ttl).

# Test Context

Here is some context about under which context this test was made

|Assertor|[NicoRobertIn](https://github.com/NicoRobertIn)|
|----|-----|
|Title|NicoRobertIn using actions script|
|Description|Test triggered by [@NicoRobertIn](https://github.com/NicoRobertIn) by actions trigger|
|Script|[suite.py](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/data/suite.py)
|Date|2024-01-15 10:28:26|

***


# Statistic summary

Here is a short overview for this test report

20 Assertions

:boom:1 MajorFail, :exclamation:0 MinorFail, :warning:0 CannotTell, :grey_question:1 NotTested, :white_check_mark:18 Pass

<div  style="border-radius: 12px; height: 25px; overflow: hidden"><img src="../assets/red.png" width="5%" height="25px"/><img src="../assets/orange.png" width="0%" height="25px"/><img src="../assets/grey.png" width="0%" height="25px"/><img src="../assets/white.png" width="5%" height="25px"/><img src="../assets/green.png" width="90%" height="25px"/></div>

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
|[Table top](#majorfail-assertions-summary)|<div id="summary-MajorFail-1">1/1</div>|:boom:*MajorFail*|`manufacturing-environments-safety-rules`|[syntax](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/model/model-test-onto.ttl#syntax)|Test subject has syntax errors|[Jump](#majorfail-assertion-number-1)|

***

## MajorFail Assertion Details

This subchapter gives more details to the :boom:MajorFail assertions

### MajorFail Assertion number 1

[Jump to summary definition](#summary-MajorFail-1)

:boom:MajorFail assertion
#### Subject detail
|Name|manufacturing-environments-safety-rules|
|----|----|
|Title|Standalone dataset domains/manufacturing-environments/safety-rules/dataset.ttl from branch refs/heads/olivaw|
|Composition|- [Dataset manufacturing-environments/safety-rules/dataset.ttl](https://github.com/HyperAgents/hmas/blob/refs/heads/olivaw/domains/manufacturing-environments/safety-rules/dataset.ttl)|

#### Criterion detail
|Identifier|[syntax](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/model/model-test-onto.ttl#syntax)|
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


# NotTested Assertions

Here is the chapter related to the NotTested assertion

:grey_question:1 NotTested assertions

<details>
<summary>Fold/Unfold the 1 summary and details</summary>

## NotTested Assertions Summary

[Jump to statistic summary](#statistic-summary)

:grey_question:1 NotTested assertions

|*Jump*|*Number*|*Status*|*Subject*|*Criterion*|*Title*|*Link*|
|------|--------|--------|---------|-----------|-------|------|
|[Table top](#nottested-assertions-summary)|<div id="summary-NotTested-1">1/1</div>|:grey_question:*NotTested*|`manufacturing-environments-safety-rules`|[owl-rl-constraint](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/model/model-test-onto.ttl#owl-rl-constraint)|The test could not be run|[Jump](#nottested-assertion-number-1)|

***

## NotTested Assertion Details

This subchapter gives more details to the :grey_question:NotTested assertions

### NotTested Assertion number 1

[Jump to summary definition](#summary-NotTested-1)

:grey_question:NotTested assertion
#### Subject detail
|Name|manufacturing-environments-safety-rules|
|----|----|
|Title|Standalone dataset domains/manufacturing-environments/safety-rules/dataset.ttl from branch refs/heads/olivaw|
|Composition|- [Dataset manufacturing-environments/safety-rules/dataset.ttl](https://github.com/HyperAgents/hmas/blob/refs/heads/olivaw/domains/manufacturing-environments/safety-rules/dataset.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/model/model-test-onto.ttl#owl-rl-constraint)|
|----|----|
|Title|OWL RL Constraint test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:grey_question:NotTested|
|----|----|
|Title|The test could not be run|
|Description|The subject and its recursive imports must be syntaxically correct|

***

</details>

***


# Pass Assertions

Here is the chapter related to the Pass assertion

:white_check_mark:18 Pass assertions

<details>
<summary>Fold/Unfold the 18 summary and details</summary>

## Pass Assertions Summary

[Jump to statistic summary](#statistic-summary)

:white_check_mark:18 Pass assertions

|*Jump*|*Number*|*Status*|*Subject*|*Criterion*|*Title*|*Link*|
|------|--------|--------|---------|-----------|-------|------|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-1">1/18</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-signifiers`|[owl-rl-constraint](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/model/model-test-onto.ttl#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-assertion-number-1)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-2">2/18</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-signifiers`|[syntax](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/model/model-test-onto.ttl#syntax)|Correct syntax|[Jump](#pass-assertion-number-2)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-3">3/18</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-platforms`|[owl-rl-constraint](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/model/model-test-onto.ttl#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-assertion-number-3)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-4">4/18</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-platforms`|[syntax](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/model/model-test-onto.ttl#syntax)|Correct syntax|[Jump](#pass-assertion-number-4)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-5">5/18</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-organization`|[owl-rl-constraint](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/model/model-test-onto.ttl#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-assertion-number-5)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-6">6/18</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-organization`|[syntax](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/model/model-test-onto.ttl#syntax)|Correct syntax|[Jump](#pass-assertion-number-6)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-7">7/18</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-core`|[owl-rl-constraint](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/model/model-test-onto.ttl#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-assertion-number-7)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-8">8/18</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-core`|[syntax](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/model/model-test-onto.ttl#syntax)|Correct syntax|[Jump](#pass-assertion-number-8)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-9">9/18</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-behavior-specifications`|[owl-rl-constraint](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/model/model-test-onto.ttl#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-assertion-number-9)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-10">10/18</div>|:white_check_mark:*Pass*|`manufacturing-environments-discover-behavior-specifications`|[syntax](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/model/model-test-onto.ttl#syntax)|Correct syntax|[Jump](#pass-assertion-number-10)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-11">11/18</div>|:white_check_mark:*Pass*|`manufacturing`|[owl-rl-constraint](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/model/model-test-onto.ttl#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-assertion-number-11)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-12">12/18</div>|:white_check_mark:*Pass*|`manufacturing`|[syntax](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/model/model-test-onto.ttl#syntax)|Correct syntax|[Jump](#pass-assertion-number-12)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-13">13/18</div>|:white_check_mark:*Pass*|`logistics-structure-organization`|[owl-rl-constraint](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/model/model-test-onto.ttl#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-assertion-number-13)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-14">14/18</div>|:white_check_mark:*Pass*|`logistics-structure-organization`|[syntax](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/model/model-test-onto.ttl#syntax)|Correct syntax|[Jump](#pass-assertion-number-14)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-15">15/18</div>|:white_check_mark:*Pass*|`logistics-create-organization`|[owl-rl-constraint](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/model/model-test-onto.ttl#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-assertion-number-15)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-16">16/18</div>|:white_check_mark:*Pass*|`logistics-create-organization`|[syntax](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/model/model-test-onto.ttl#syntax)|Correct syntax|[Jump](#pass-assertion-number-16)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-17">17/18</div>|:white_check_mark:*Pass*|`domain-template-scenario-template`|[owl-rl-constraint](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/model/model-test-onto.ttl#owl-rl-constraint)|OWL RL consistent|[Jump](#pass-assertion-number-17)|
|[Table top](#pass-assertions-summary)|<div id="summary-Pass-18">18/18</div>|:white_check_mark:*Pass*|`domain-template-scenario-template`|[syntax](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/model/model-test-onto.ttl#syntax)|Correct syntax|[Jump](#pass-assertion-number-18)|

***

## Pass Assertion Details

This subchapter gives more details to the :white_check_mark:Pass assertions

### Pass Assertion number 1

[Jump to summary definition](#summary-Pass-1)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-signifiers|
|----|----|
|Title|Standalone dataset domains/manufacturing-environments/discover-signifiers/dataset.ttl from branch refs/heads/olivaw|
|Composition|- [Dataset manufacturing-environments/discover-signifiers/dataset.ttl](https://github.com/HyperAgents/hmas/blob/refs/heads/olivaw/domains/manufacturing-environments/discover-signifiers/dataset.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/model/model-test-onto.ttl#owl-rl-constraint)|
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
|Title|Standalone dataset domains/manufacturing-environments/discover-signifiers/dataset.ttl from branch refs/heads/olivaw|
|Composition|- [Dataset manufacturing-environments/discover-signifiers/dataset.ttl](https://github.com/HyperAgents/hmas/blob/refs/heads/olivaw/domains/manufacturing-environments/discover-signifiers/dataset.ttl)|

#### Criterion detail
|Identifier|[syntax](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/model/model-test-onto.ttl#syntax)|
|----|----|
|Title|Syntax test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Correct syntax|
|Description|Test subject has a correct syntax|

***
### Pass Assertion number 3

[Jump to summary definition](#summary-Pass-3)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-platforms|
|----|----|
|Title|Standalone dataset domains/manufacturing-environments/discover-platforms/dataset.ttl from branch refs/heads/olivaw|
|Composition|- [Dataset manufacturing-environments/discover-platforms/dataset.ttl](https://github.com/HyperAgents/hmas/blob/refs/heads/olivaw/domains/manufacturing-environments/discover-platforms/dataset.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/model/model-test-onto.ttl#owl-rl-constraint)|
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
|Name|manufacturing-environments-discover-platforms|
|----|----|
|Title|Standalone dataset domains/manufacturing-environments/discover-platforms/dataset.ttl from branch refs/heads/olivaw|
|Composition|- [Dataset manufacturing-environments/discover-platforms/dataset.ttl](https://github.com/HyperAgents/hmas/blob/refs/heads/olivaw/domains/manufacturing-environments/discover-platforms/dataset.ttl)|

#### Criterion detail
|Identifier|[syntax](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/model/model-test-onto.ttl#syntax)|
|----|----|
|Title|Syntax test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Correct syntax|
|Description|Test subject has a correct syntax|

***
### Pass Assertion number 5

[Jump to summary definition](#summary-Pass-5)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-organization|
|----|----|
|Title|Standalone dataset domains/manufacturing-environments/discover-organization/dataset.ttl from branch refs/heads/olivaw|
|Composition|- [Dataset manufacturing-environments/discover-organization/dataset.ttl](https://github.com/HyperAgents/hmas/blob/refs/heads/olivaw/domains/manufacturing-environments/discover-organization/dataset.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/model/model-test-onto.ttl#owl-rl-constraint)|
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
|Name|manufacturing-environments-discover-organization|
|----|----|
|Title|Standalone dataset domains/manufacturing-environments/discover-organization/dataset.ttl from branch refs/heads/olivaw|
|Composition|- [Dataset manufacturing-environments/discover-organization/dataset.ttl](https://github.com/HyperAgents/hmas/blob/refs/heads/olivaw/domains/manufacturing-environments/discover-organization/dataset.ttl)|

#### Criterion detail
|Identifier|[syntax](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/model/model-test-onto.ttl#syntax)|
|----|----|
|Title|Syntax test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Correct syntax|
|Description|Test subject has a correct syntax|

***
### Pass Assertion number 7

[Jump to summary definition](#summary-Pass-7)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-core|
|----|----|
|Title|Standalone dataset domains/manufacturing-environments/discover-core/dataset.ttl from branch refs/heads/olivaw|
|Composition|- [Dataset manufacturing-environments/discover-core/dataset.ttl](https://github.com/HyperAgents/hmas/blob/refs/heads/olivaw/domains/manufacturing-environments/discover-core/dataset.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/model/model-test-onto.ttl#owl-rl-constraint)|
|----|----|
|Title|OWL RL Constraint test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL RL consistent|
|Description|The provided graph is consistent for any OWL RL constraint|

***
### Pass Assertion number 8

[Jump to summary definition](#summary-Pass-8)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-core|
|----|----|
|Title|Standalone dataset domains/manufacturing-environments/discover-core/dataset.ttl from branch refs/heads/olivaw|
|Composition|- [Dataset manufacturing-environments/discover-core/dataset.ttl](https://github.com/HyperAgents/hmas/blob/refs/heads/olivaw/domains/manufacturing-environments/discover-core/dataset.ttl)|

#### Criterion detail
|Identifier|[syntax](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/model/model-test-onto.ttl#syntax)|
|----|----|
|Title|Syntax test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Correct syntax|
|Description|Test subject has a correct syntax|

***
### Pass Assertion number 9

[Jump to summary definition](#summary-Pass-9)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Standalone dataset domains/manufacturing-environments/discover-behavior-specifications/dataset.ttl from branch refs/heads/olivaw|
|Composition|- [Dataset manufacturing-environments/discover-behavior-specifications/dataset.ttl](https://github.com/HyperAgents/hmas/blob/refs/heads/olivaw/domains/manufacturing-environments/discover-behavior-specifications/dataset.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/model/model-test-onto.ttl#owl-rl-constraint)|
|----|----|
|Title|OWL RL Constraint test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL RL consistent|
|Description|The provided graph is consistent for any OWL RL constraint|

***
### Pass Assertion number 10

[Jump to summary definition](#summary-Pass-10)

:white_check_mark:Pass assertion
#### Subject detail
|Name|manufacturing-environments-discover-behavior-specifications|
|----|----|
|Title|Standalone dataset domains/manufacturing-environments/discover-behavior-specifications/dataset.ttl from branch refs/heads/olivaw|
|Composition|- [Dataset manufacturing-environments/discover-behavior-specifications/dataset.ttl](https://github.com/HyperAgents/hmas/blob/refs/heads/olivaw/domains/manufacturing-environments/discover-behavior-specifications/dataset.ttl)|

#### Criterion detail
|Identifier|[syntax](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/model/model-test-onto.ttl#syntax)|
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
|Name|manufacturing|
|----|----|
|Title|Standalone use case use-cases/manufacturing/dataset-v1.ttl from branch refs/heads/olivaw|
|Composition|- [Use case manufacturing/dataset-v1.ttl](https://github.com/HyperAgents/hmas/blob/refs/heads/olivaw/use-cases/manufacturing/dataset-v1.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/model/model-test-onto.ttl#owl-rl-constraint)|
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
|Name|manufacturing|
|----|----|
|Title|Standalone use case use-cases/manufacturing/dataset-v1.ttl from branch refs/heads/olivaw|
|Composition|- [Use case manufacturing/dataset-v1.ttl](https://github.com/HyperAgents/hmas/blob/refs/heads/olivaw/use-cases/manufacturing/dataset-v1.ttl)|

#### Criterion detail
|Identifier|[syntax](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/model/model-test-onto.ttl#syntax)|
|----|----|
|Title|Syntax test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Correct syntax|
|Description|Test subject has a correct syntax|

***
### Pass Assertion number 13

[Jump to summary definition](#summary-Pass-13)

:white_check_mark:Pass assertion
#### Subject detail
|Name|logistics-structure-organization|
|----|----|
|Title|Standalone dataset domains/logistics/structure-organization/dataset.ttl from branch refs/heads/olivaw|
|Composition|- [Dataset logistics/structure-organization/dataset.ttl](https://github.com/HyperAgents/hmas/blob/refs/heads/olivaw/domains/logistics/structure-organization/dataset.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/model/model-test-onto.ttl#owl-rl-constraint)|
|----|----|
|Title|OWL RL Constraint test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL RL consistent|
|Description|The provided graph is consistent for any OWL RL constraint|

***
### Pass Assertion number 14

[Jump to summary definition](#summary-Pass-14)

:white_check_mark:Pass assertion
#### Subject detail
|Name|logistics-structure-organization|
|----|----|
|Title|Standalone dataset domains/logistics/structure-organization/dataset.ttl from branch refs/heads/olivaw|
|Composition|- [Dataset logistics/structure-organization/dataset.ttl](https://github.com/HyperAgents/hmas/blob/refs/heads/olivaw/domains/logistics/structure-organization/dataset.ttl)|

#### Criterion detail
|Identifier|[syntax](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/model/model-test-onto.ttl#syntax)|
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
|Name|logistics-create-organization|
|----|----|
|Title|Standalone dataset domains/logistics/create-organization/dataset.ttl from branch refs/heads/olivaw|
|Composition|- [Dataset logistics/create-organization/dataset.ttl](https://github.com/HyperAgents/hmas/blob/refs/heads/olivaw/domains/logistics/create-organization/dataset.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/model/model-test-onto.ttl#owl-rl-constraint)|
|----|----|
|Title|OWL RL Constraint test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL RL consistent|
|Description|The provided graph is consistent for any OWL RL constraint|

***
### Pass Assertion number 16

[Jump to summary definition](#summary-Pass-16)

:white_check_mark:Pass assertion
#### Subject detail
|Name|logistics-create-organization|
|----|----|
|Title|Standalone dataset domains/logistics/create-organization/dataset.ttl from branch refs/heads/olivaw|
|Composition|- [Dataset logistics/create-organization/dataset.ttl](https://github.com/HyperAgents/hmas/blob/refs/heads/olivaw/domains/logistics/create-organization/dataset.ttl)|

#### Criterion detail
|Identifier|[syntax](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/model/model-test-onto.ttl#syntax)|
|----|----|
|Title|Syntax test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Correct syntax|
|Description|Test subject has a correct syntax|

***
### Pass Assertion number 17

[Jump to summary definition](#summary-Pass-17)

:white_check_mark:Pass assertion
#### Subject detail
|Name|domain-template-scenario-template|
|----|----|
|Title|Standalone dataset domains/domain-template/scenario-template/dataset.ttl from branch refs/heads/olivaw|
|Composition|- [Dataset domain-template/scenario-template/dataset.ttl](https://github.com/HyperAgents/hmas/blob/refs/heads/olivaw/domains/domain-template/scenario-template/dataset.ttl)|

#### Criterion detail
|Identifier|[owl-rl-constraint](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/model/model-test-onto.ttl#owl-rl-constraint)|
|----|----|
|Title|OWL RL Constraint test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|OWL RL consistent|
|Description|The provided graph is consistent for any OWL RL constraint|

***
### Pass Assertion number 18

[Jump to summary definition](#summary-Pass-18)

:white_check_mark:Pass assertion
#### Subject detail
|Name|domain-template-scenario-template|
|----|----|
|Title|Standalone dataset domains/domain-template/scenario-template/dataset.ttl from branch refs/heads/olivaw|
|Composition|- [Dataset domain-template/scenario-template/dataset.ttl](https://github.com/HyperAgents/hmas/blob/refs/heads/olivaw/domains/domain-template/scenario-template/dataset.ttl)|

#### Criterion detail
|Identifier|[syntax](https://github.com/Wimmics/olivaw/blob/main/olivaw/test/model/model-test-onto.ttl#syntax)|
|----|----|
|Title|Syntax test|
|Description|A test meant to check wether the test subject is syntaxically correct or not.|

#### Outcome Detail
|Type|:white_check_mark:Pass|
|----|----|
|Title|Correct syntax|
|Description|Test subject has a correct syntax|

***

</details>

***

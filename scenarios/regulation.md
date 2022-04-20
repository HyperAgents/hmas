
# Regulation of agents and platforms

The existence of norms, and laws in society allow to facilitate interactions between people. In Multi-Agent Systems it allows to regulate bad interactions. This motivating scenario allows to bring in HypermediaMASPlatform a way for building norms and laws so that HyperAgents understand these rules for interacting with other agents. 

## **A short description**

Norms and laws are explicitely considered in a hMAS. Thus, one agent needs to understand these norms to know if it is allowed to perform or not an action but also must know the sanctions when they are violated.  In case of violations of norms, sanctions have to be applied.  

## **Covered features** 

This motivating scenario aims to allow HyperAgents to:
* know the norms of the MAS ;
* detect violation of a norm when it happens ;
* know and apply sanctions .


## **A set of examples**

The following example present the features.

### 1) Feature : know the norms 

    Fabiana Gordana (@j) needs high-dose aspirin (more than 500 mg per day) because she has a terrible headache since she got pregnant. 
    
    She connects to an online platform for medical products (UbarDrugSTORE) because she really doesn't have the strength to go into town. 
    
    Furthermore, she needs the drugs as soon as possible. UbarMedicament provides a home delivery service with a medical emergency option.
    
    She logs in to the site with her login and password. 
    
    She sees the site interface and goes to the products for sale tab and the non-morphine analgesics category.
    
    She orders 10 boxes of 50 tablets. However, the agent in charge of sending the order needs to check the requirements to send that order to the logistics department.
    
    Some information in Fabiana's profile are required (e.g. is she pregnant?).
    
    Then the agent sends a small form back to Fabiana to complete that information.
    
    Fabiana completes this form and states that she is pregnant. 
    
    Although it is permitted to send this type of product, it is strongly discouraged to consume more than 500 mg per day. 
    
    The agent therefore needs to ask the estimated daily consumption.
    
    Fabiana completes a new form giving information that she will be taking more than 500mg per day. 
    
    However even if it is highly not recommended to provide such products, it is not forbidden.
    
    The agent returns to Fabiana some arguments to not take the products. 
    
    In the web interface Fabiana sees the answer which is : 
    since (arguments) "Fabiana is pregnant", "Aspirin is dangerous for pregnant women when we consumed it more than 500 mg per day", then  (result) it is highly not recommended.
    
    However, Fabiana is very stubborn and places the order.




### 2) Feature : detect violation of a rule

    Fabiana Gordana (@j) is browsing on the web page of UbarDrugSTORE.
    
    She sees an advertisement for an anti-aging pill with extraordinary effects. 
    
    These pills promise you a complete cell regeneration, giving you back your youthful skin. 
    
    Since her 30th birthday, Fabiana has been dreaming of getting her baby skin back. 
    
    She orders 10 packs of 50 pills.
    
    No rules and no recommandation for not using the product were applied for the case of Fabiana.
    
    Thus, Fabiana was allowed to buy and receive her pills. 
    
    However, the site strictly prohibits the sale of products whose effects have not been clinically proven. 
    
    The anti-aging pills have not been clinically proven according to an update of the database of the High Authority for Health. 
    
    But the supplier lied and confirmed that the product was clinically proven.
    
    Derogating from this rule means a total ban of the supplier.  (punishment)
    
    All users who purchased this product are notified to return their products. 
    



### 3) Feature : apply sanctions 

    According to the law in France (Article R. 5125-74 of the Public Health Code), to distribute medicines, the UbarDrugSTORE platform must be on the list of pharmacy websites provided by the national order of pharmacists. (regulationOfInternetPlatforms)
    
    Each supplier of UbarDrugSTORE must be either : a pharmacist established in France who is holder of a pharmacy, a pharmacist managing a mutualist pharmacy or an emergency mining pharmacy. 
    
    However the supplier that provided drugs to Fabiana was an ex-Pharcamist who ceased his activity several years ago. 
    
    The cessation of activity of the pharmacy therefore entails the closure of its account. 
    
    The High Health Authority has been notified of this fraud and decided to sanction UbarDrugStore for its negligence.
    
    The informed Ministry of Health ordered UbarDrugSTORE not to sell any more medicines until all suppliers on the platform had certified all information on their profile. 
    
    
## **A glossary of new terms**

List of new terms introduced by the motivating scenario :
* law : ...
* norm : ...
* punishment : ...


## **Competency questions**

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

## **Formal description** 

** Please give the formal SPARQL request **

```
cq: ** identifier of the competency question it **
query: |-
 ** Example : SELECT ?workspace ?agent WHERE { ?workspace hmas:hosts ?agent } **
output: ** Result :  { (<w>,<a>) s.t.<w> hmas:hosts <a>  }  **
```


### **Link to query the related issues** 

* [regulation](https://github.com/HyperAgents/ns.hyperagents.org/issues?q=regulation)




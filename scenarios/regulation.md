
# Regulation of agents and platforms

## Quick definition of terms (@Adnane)


## Basic features : knowing norms, detecting violations and defining sanctions

Agent/Platform must know if it is allowed to perform an action

description: 

  Agents must know the norms associated with an environment (its workspace) in real time and the associated punishments (since norms may change and be violated).



## 1) Standard motivating scenario : an agent must know the norms (general case) 

    Fabiana Gordana (@j) needs high-dose aspirin (more than 500 mg per day) because she has a terrible headache since she got pregnant. 
    
    She connects to an online platform for medical products (UbarDrugSTORE) because she really doesn't have the strength to go into town. (UbarDrugSTORE rdfs:subClassOf Platform)
    
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




## 2) Feature : violation of a rule by lying on its profile data.

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
    



## 3) Feature : negligence of a platform and sanctions   

    According to the law in France (Article R. 5125-74 of the Public Health Code), to distribute medicines, the UbarDrugSTORE platform must be on the list of pharmacy websites provided by the national order of pharmacists. (regulationOfInternetPlatforms)
    
    Each supplier of UbarDrugSTORE must be either : a pharmacist established in France who is holder of a pharmacy, a pharmacist managing a mutualist pharmacy or an emergency mining pharmacy. 
    
    However the supplier that provided drugs to Fabiana was an ex-Pharcamist who ceased his activity several years ago. 
    
    The cessation of activity of the pharmacy therefore entails the closure of its account. 
    
    The High Health Authority has been notified of this fraud and decided to sanction UbarDrugStore for its negligence.
    
    The informed Ministry of Health ordered UbarDrugSTORE not to sell any more medicines until all suppliers on the platform had certified all information on their profile. 

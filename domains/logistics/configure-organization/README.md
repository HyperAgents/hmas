# Configure an Organization

## Description

The FL Logistics has a depot in Lyon and another in Saint-Étienne. Each depot has one _receiving_ and one _picking_ setting. Each _receiving_ setting has one forklift, one pallet jack, and one barcode reader. Each _picking_ setting has one forklift, one pallet jack, and one label printer. Only one employee can be associated with the usage of one setting, but the same employee can be associated with the usage of multiple settings.

Forklifts are capable of raising and lowering materials on pallets to/from high shelves, as well as moving them from one location to another. Pallet jacks are capable of raising and lowering the materials on pallets placed on the floor and move them from one location to another. They both are used for loading and unloading trucks by moving materials in the _receiving_ and the _picking_ settings.

The barcode reader is capable of reading barcodes identifying the materials on a pallet. The label machine is capable of printing labels with barcode to identify the materials on a pallet.

Marie can use the forklift and pallet jack to unload trucks (i.e., lift pallets and move them in the _receiving_ setting) and the barcode reader to check the pallet content.

Nancy can use the forklift and pallet jack to load trucks (i.e., lift pallets and move them in the _picking_ setting) and the label printer to print the labels identifying the pallets content.

Leo can use the forklift and pallet jack to unload trucks (i.e., lift pallets and move them in the _receiving_ setting) and load trucks (i.e., lift pallets and move them in the _picking_ setting), the barcode reader to check the pallet content, and the label printer to print the labels identifying the pallets content.

## Competency questions

| ID | Question in Natural Language | Example |
|----|------------------------------|---------|
| q1 | What are the artifacts that an agent of the organization X can have in setting Y? | What are the artifacts that an agent of the FL Logistics can have in the _receiving_ setting? `ex:Barcode_Reader_1`, `ex:Barcode_Reader_2`, `ex:Forklift_1`, `ex:Forklift_2`, `ex:Forklift_3`, `ex:Forklift_4`, `ex:Palletjack_1`, `ex:Palletjack_2`, `ex:Palletjack_3`, `ex:Palletjack_4`                    |
| q2 | What are the settings that set the organization X?                                | What are the settings that set the FL Logistics? `ex:PickingSetting`, `ex:ReceivingSetting` |
| q3 | What are the facilities that the artifact X have?                                 | What are the facilities that Forklift 1 have? `ex:LiftDown`, `ex:LiftUp`, `ex:Move`         |
| q4 | What are the agents currently in the setting Y?                                   | What are the agents currently in the _picking_ setting? `ex:Leo`, `ex:Nancy`                |

## Glossary

![image](configure-organization.png)

* **Usage**: A set of Facilities that Agents can use in a Setting.
* **Use**: An engagement of an Agent of using an Artifact in the context of an Usage.
* **Usage Constraint**: A constraint imposed on Usages, e.g., limiting the number of Agents participating in that Usage or the same Agent cannot be part of two Usages simultaneously.
* **Setting**: A Setting is the context in which a Usage is set.
* **Facility**: see [Create an Organization](https://github.com/HyperAgents/ns.hyperagents.org/blob/master/domains/logistics/create-organization/README.md) scenario.
* **Organization**: see [Discover Organizations, their Members and Materials in Hypermedia Environments](https://github.com/HyperAgents/hmas/blob/master/domains/manufacturing-environments/discover-organization/README.md) scenario.
* **Agent**: see [Discover Organizations, their Members and Materials in Hypermedia Environments](https://github.com/HyperAgents/hmas/blob/master/domains/manufacturing-environments/discover-organization/README.md) scenario.
* **Artifact**: see [Discover Organizations, their Members and Materials in Hypermedia Environments](https://github.com/HyperAgents/hmas/blob/master/domains/manufacturing-environments/discover-organization/README.md) scenario.

## Recommendations

* The Use Constraint is represented as a SHACL shape instead of an RDF triple. For example, the SHACL shape constraining the use of a Usage by a single Agent whose Artifacts is

```
ex:UsageCardinalityShape a sh:NodeShape ;
    sh:targetObjectsOf hmas:isUseFor;
    sh:property [
        sh:path ( [ sh:inversePath hmas:isUseFor ] hmas:isUseBy ) ;
        sh:maxCount 1 ;
        ] .
```

In the same way, the Use Constraint uses SHACL shape instead of an RDF triple. For example, the SHACL shape constraining the use 

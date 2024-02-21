# CRUD Actions

## Description

Most basic Web interfaces follow the Create/Replace/Update/Delete pattern to manipulate resources. A forum, for instance, may expose actions to create or edit (replace) a post, to create a response to a post or even to create or delete a new discussion space dedicated to a particular topic.

## Competency Questions

| ID | Question in natural language | Example of answer |
|---|---|---|
| q1_1 | What request to send to post a message? | POST /topics/random/posts |
| q1_2 | What request to send to respond to a post? | POST /topics/random/posts/123/answers |
| q2 | What request to send to edit a post? | PUT /topics/random/posts/123 |
| q3 | What request to send to delete a peviously posted message? | DELETE /topics/random/posts/123 |
| q4 | What request to send to add a user to some forum? | POST /topics/random |

Editing a post may either be executed as a single update operation, as a replace operation or as a sequence of delete and create operations. In case the three options have different side effects, an agent should be informed of the side effects of each action.

## Glossary

* [**CreateAction**](https://purl.org/hmas/CreateAction): Action to create a new resource.
* [**ReplaceAction**](https://purl.org/hmas/ReplaceAction): Action to replace an existing resource.
* [**UpdateAction**](https://purl.org/hmas/UpdateAction): Action to update the representation of an existing resource by adding statements to it.
* [**DeleteAction**](https://purl.org/hmas/DeleteAction): Action to delete an existing resource.

### Recommendations

- On-going actions can be described as temporal entities with the [PROV-O](https://www.w3.org/TR/prov-o/) and [OWL Time](https://www.w3.org/TR/owl-time/) ontologies. Action specification can be given as SHACL shapes on `prov:Activity` instances.
- [DublinCore terms](http://purl.org/dc/terms/) can capture the fact that a resource has a new version after every action.

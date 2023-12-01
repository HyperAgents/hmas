# Online forums

## Description

An open discussion forum where agents (humans and software) can start a discussion thread on a topic, respond to an existing thread, read individual messages and list threads. Also, allowing the agents to interact with existing open online forums for reading, posting messages and creating new threads.

The scenario could be later extended with authentication, roles such as "moderator", "editor", etc. and more actions, like keyword search, removing posts, renaming, creating subforums, assigning threads to specific subforums, and so on.

## Competency Questions

| ID | Question in natural language |
|---|---|
| q1 | Is this platform a discussion board or online forum? |
| q2 | What are the existing threads? |
| q3 | What messages respond to what thread/message? |
| q4 | How can I start a new thread? |
| q5 | How can I post a message in response to a given thread/message? |

Compentency question q4 should also allow one to publish a blog post, and q5 should allow one to respond to a blog post, or post a comment on any page/resource that offers this possibility.

## Glossary

* **Online forum**: The class of discussion websites which indicate that there should be ways of consulting messages or threads and responding to messages or threads.
* **Thread**: A discussion on a certain topic. It may be associated with text or simply provide a container for messages that respond to it.
* **Post**: A single posted text. This includes blog posts, comments, forum messages, tweets. This generally corresponds to any piece of text (with or without layout style) that is submitted via a Web form and immediately added to a web page for everyone to read.
* **Responding**: A class of affordances(?) that indicate that there is a way of posting messages in response to a given thread or post.
* **Starting thread**: A class of affordances(?) that indicate that there is a way of starting threads that others can respond to.
* **title**: The title (or textual topic) of a thread.
* **content**: The textual (and styling) content of a post.
* **created**: The date a post was made.
* **creator**: The creator.

We can use the SIOC ontology ([Semantically Interlinked Online Communities](http://sioc-project.org/)) to describe the forums, but we need additional terms that extend the HMAS ontology for posting/reading messages.

### Recommendations

Start with read only forums. Find the latest posts or list of all posts, extract the title and text from an individual post. Make this possible for any open online forum, provided that there is a description file. The description file may describe multiple forums and may describe online platforms that are not forums at all.

When consulting an individual message, we should have a description of it in RDF. Forums that exclusively use HTML can still return RDF by providing a transformation. When posting a message, it should be possible to post an RDF graph. Forums that require submitting JSON or other formats can rely on transformation from RDF to comply with the requirement.

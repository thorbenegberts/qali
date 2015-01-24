# QALI

QALI is a user driven Q&amp;A and learning interface. QALI means: **Q**uestion **A**nswer **L**earning **I**nterface. It is not meant to be just another Q&A database. People should be able to create their own content and be actively guided to learn new things. QALI will not just give people answers, but will build a bridge between the known and the unknown by giving you recommendations.

Work on QALI is just starting. Stay tuned :-)

## RESTful API

QALI is mainly a RESTful API for adding, reading and removing questions. A documentation will follow.

## UI

QALI has no official UI yet. However, it will be done in another project. By building the API first, we separate the service from any UI. Doing so, people will be able to build their own UI, plugins for other applications like Confluence or even build their own services on top of it.

## Setup

QALI is build using [Flask RESTful](https://github.com/flask-restful/flask-restful). To run locally run:

```
python api.py
```
# QALI

QALI is a Q&amp;A and learning platform for user-generated content. QALI stands for: **Q**uestion **A**nswer **L**earning **I**nterface. It is not meant to be just another Q&A platform. People should be able to create their own content and be actively guided to learn new things, together. QALI will not just give people answers, but can build the bridge between the known and the unknown by giving recommendations.

Work on QALI is just starting. Stay tuned :-)

## RESTful API

QALI is mainly a RESTful API for adding, reading and removing questions. A documentation will follow.

## UI

QALI has no official UI yet. However, it will be done in another project. By building the API first, we separate the service from any UI. Doing so, people will be able to build their own UI, plugins for other applications like Confluence or even build their own services on top of it.

## Setup

QALI is build with Python. Mainly the [Flask RESTful](https://github.com/flask-restful/flask-restful). package is used.

To setup, run:

```
sh setup.sh
```

## Run Locally

To run locally, run:

```
foreman start web
```

Note that `foreman` is part of the [Heroku Toolbelt](https://toolbelt.heroku.com/).

Now open

```
localhost:5000
```

in your browser.
==================
Test Documentation
==================


Requirements
============
Ensure that the following tools are installed (if you want to test locally, without docker):

* Python >= 3.4
* `pipenv <https://pip.pypa.io/en/stable/installing/>`_
* `splinter <https://splinter.readthedocs.org/en/latest/>`_ **DEPRECATED**


Backend with WebTest
====================
Backend tests are realized by the use of *WebTest*. A quick tutorial can be found in the
`documentation of pyramid <http://docs.pylonsproject.org/projects/pyramid/en/latest/quick_tutorial/functional_testing.html>`_
or in the `documentation of WebTest <http://docs.pylonsproject.org/projects/webtest/en/latest/>`_.
Webtests are normally unit tests, but can be used for end-to-end-full-stack tests as well.

Execute these tests with::

    nosetests


If you want to stay very clean on your machine, you could just run the tests in your container with::

    docker exec dbas_web_1 nosetests


Please note, that every module has its own tests

Note
====
If you call::

    def setUp(self):
        self.config = testing.setUp()

Please also call::

    def tearDown(self):
        testing.tearDown()

Or even if you add or delete some entries, flush and commit your actions. Otherwise the transactions for the database will brake.

Code
====

.. automodule:: dbas.tests
    :members:

.. automodule:: dbas.auth.tests
    :members:

.. automodule:: dbas.auth.oauth.tests
    :members:

.. automodule:: dbas.handler.tests
    :members:

.. automodule:: dbas.review.tests
    :members:

.. automodule:: dbas.review.queue.tests
    :members:

.. automodule:: dbas.strings.tests
    :members:

.. automodule:: dbas.validators.tests
    :members:

.. automodule:: dbas.views.tests
    :members:

.. automodule:: dbas.views.discussion.tests
    :members:

.. automodule:: dbas.views.main.tests
    :members:

.. automodule:: dbas.views.review.tests
    :members:

.. automodule:: dbas.views.user.tests
    :members:

Frontend with Cypress
=====================
**Up to date**

First of all you have to add the *cypress.env.json* into the frontendtest folder.

The folder structure will look like this::

    frontendtest/
        -> cypress/
            -> fixtures
            -> integration
            -> plugins
            -> support
        -> cypress.json
        -> cypress.env.json


Fill *cypress.env.json* with the environment variables used in development.env::

    {
        "WEB_PROTOCOL": <the protocol which is used by D-BAS>,
        "WEB_HOST": <the host of the running D-BAS container>,
        "WEB_PORT": <the port on which you can enter D-BAS>
    }

If you have added all environment variables to the *cypress.env.json* you have two options to run the tests stored in *integration/*::

    // navigate into frontendtest

    // this command will open the cypress IDE where you can see and interact with the tests
    $ cypress open

    // this will run the tests on the console
    $ cypress run

    // to run a specific test use the --spec flag
    $ cypress run --spec /path/to/the/test

    // to run the tests in a specific browser use the --browser flag and make sure that this browser is installed
    // cypress will use the Electron-Browser for default
    $ cypress run --browser chrome

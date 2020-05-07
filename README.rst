Python and Vue JS Application for Risk Management
================================================

Sample Project

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django


:License: MIT


Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run manage.py test
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ py.test

Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html





Sentry
^^^^^^

Sentry is an error logging aggregator service. You can sign up for a free account at  https://sentry.io/signup/?code=cookiecutter  or download and host it yourself.
The system is setup with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.


Steps to deploy and test in in Local:
--------------------------------------
1. Git clone

2. Git checkout master

3. Python3 pip install -r requiremetnts/requirements.txt

4. Python3 manage.py migrate

5. Create a super user using: python3 manage.py createsuperuser

6. Run server using: Python3 manage.py runserver

7. Login to admin panel using the superuser credentials

8. Add Risk Types, Risk Fields and RiskField Choices for any field.

9. Go to home page.


Steps to deploy and test in in AWS Lambda:
--------------------------------------
1. Git clone

2. Git checkout aws-deploy

3. Create a virtual env in your machine

4. Activate the virtual env using: Python3 pip install -r requiremetnts/requirements.txt

5. zappa init and follow the instructions to create lambda function: 

6. zappa deploy dev to deploy the application

7. zappa manage dec migrate to run migrations

8. Create a super user using: zappa invoke --raw dev "from django.contrib.auth import get_user_model; User=get_user_model(); User.objects.create_superuser('roshan','brishi98@gmail.com', 'roshan123')"

9. zappa update dev

10. Login to admin panel using the superuser credentials

11. Add Risk Types, Risk Fields and RiskField Choices for any field.
12. Go to home page.


Docker
^^^^^^

See detailed `cookiecutter-django Docker documentation`_.

.. _`cookiecutter-django Docker documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html




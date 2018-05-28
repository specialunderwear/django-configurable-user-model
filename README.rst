Example app of a very dynamic django app
----------------------------------------

In this example we demonstrate how a very dynamic django application can
be constricted by means of metaclasses.

This repo contains a reusable module called ``django_configurable_user_model`` as
well as an example application called ``testsite``.

The ``django_configurable_user_model`` application allows modification of
the built-in django.auth ``User`` model in a json file.

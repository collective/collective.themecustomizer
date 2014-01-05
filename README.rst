**************************
collective.themecustomizer
**************************

.. contents:: Table of Contents

Life, the Universe, and Everything
==================================

``collective.themecustomizer`` provides some simple but very useful customizations
of a Plone site theme in an intuitive interface known by any site administrator.

Additionally ``portal.site_actions`` viewlet, originally only in ``plone.portalfooter``
manager, is displayed in ``plone.portalheader`` as well.

Mostly Harmless
===============

.. image:: https://secure.travis-ci.org/collective/collective.themecustomizer.png?branch=master
    :alt: Travis CI badge
    :target: http://travis-ci.org/collective/collective.themecustomizer

.. image:: https://coveralls.io/repos/collective/collective.themecustomizer/badge.png?branch=master
    :alt: coveralls badge
    :target: https://coveralls.io/r/collective/collective.themecustomizer

Got an idea? Found a bug? Let us know by `opening a support ticket`_.

.. _`opening a support ticket`: https://github.com/collective/collective.themecustomizer/issues

Don't Panic
===========

Installation
------------

To enable this package in a buildout-based installation:

#. Edit your buildout.cfg and add add the following to it::

    [buildout]
    ...
    eggs =
        collective.themecustomizer

After updating the configuration you need to run ''bin/buildout'', which will
take care of updating your system.

Go to the 'Site Setup' page in a Plone site and click on the 'Add-ons' link.

Check the box next to ``collective.themecustomizer`` and click the 'Activate'
button.

.. Note::
    You may have to empty your browser cache and save your resource registries
    in order to see the effects of the product installation.

Usage
-----

Once installed ``collective.themecustomizer`` go to **Site controlpanel** to
find the customization options:

- Display text in Header

- Logo image

- Display logo in Header

- Header background image

After saving your preferences you'll see your desired options already applied.

To-do list
----------

- Provide even more theme customizations like footer text and colors.

- Use English for strings everywhere.

- Provide a preview scale of the image in the imagewidget

- Separate imagewidget to a new package

- Move customization options to theme controlpanel or a new configlet

- Store customizations in registry


Not entirely unlike
===================

TBD.

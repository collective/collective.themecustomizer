**************************
collective.themecustomizer
**************************

.. contents:: Table of Contents

Life, the Universe, and Everything
==================================

``collective.themecustomizer`` provides some simple but very useful customizations
of a Plone site theme in an intuitive interface known by any site administrator.

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

Go to the **Site Setup** page in a Plone site and click on the **Add-ons** link.

Check the box next to ``collective.themecustomizer`` and click the **Activate**
button.

.. Note::
    You may have to empty your browser cache and save your resource registries
    in order to see the effects of the product installation.

Usage
-----

Once ``collective.themecustomizer`` is installed go to **Site controlpanel** to
find the customization options:

- Display text in Header

- Logo image

- Display logo in Header

- Header background image

After saving your preferences you'll see your desired options already applied.

How it works
------------

The package overrides ``plone.logo`` and ``plone.header`` viewlets (via a
custom **browserlayer**) respecting their default behavior, in case no
customization was made yet.

Using with Diazo
----------------

To use themecustomizer with Diazo you can add some lines to your rules.xml, to
change the HTML when the background image is in use::

    <!-- Themecustomizer rules -->
    <rules css:if-not-content="#portal-header[style='']">
      <copy attributes="style" css:content="#portal-header" css:theme="header" />
      <merge attributes="class" css:content="#portal-header" css:theme="header" />
    </rules>

The first rule will apply themecustomizer background image to your theme HTML. In the 
example above, the background image will be added to <header> tag. You can change 
css:theme="header" to wharever you want to show the themecustomizer image, like body 
or footer.

The second rule will add an aditional class to the tag when the themecustomizer image 
is in use. With this class you can disable your theme original background image when
user select another imagem using theme customizer.

HTML::

    <header class="customizer-background" style="background-image: url(http://localhost:8080/Plone/background.png)">

CSS::

    header {background: url("img/background.jpg");}
    .customizer-background {background: transparent;}


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

`CSSManager`_
    Provides a simple interface to tweak logo and CSS properties by 
    overriding old ``base_properties`` sheet, which is not used by 
    Plone 4 default Sunburst theme.
    Although it works if you choose **Plone Classic Theme** in a Plone 4 site
    theme settings.
    If you want to install it you'll have to manually add ``elementtree``
    to the ``eggs`` section in your buildout file.

`Products.CustomOverrides`_
    Allows content managers to inject custom stylesheets and Javascript
    that will be added to choosen folder and its descendants.
    It requieres CSS and JS knowledge.

.. _`CSSManager`: https://pypi.python.org/pypi/Products.CSSManager
.. _`Products.CustomOverrides`: https://pypi.python.org/pypi/Products.CustomOverrides

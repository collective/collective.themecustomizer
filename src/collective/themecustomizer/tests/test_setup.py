# -*- coding: utf-8 -*-

from collective.themecustomizer.config import PROJECTNAME
from collective.themecustomizer.testing import INTEGRATION_TESTING
from plone.browserlayer.utils import registered_layers
from plone.testing.z2 import Browser

import unittest


class InstallTestCase(unittest.TestCase):
    """Ensure product is properly installed."""

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.qi = self.portal['portal_quickinstaller']

    def test_installed(self):
        self.assertTrue(self.qi.isProductInstalled(PROJECTNAME),
                        '%s not installed' % PROJECTNAME)

    def test_addon_layer_is_registered(self):
        layers = [l.getName() for l in registered_layers()]
        self.assertIn('IThemeCustomizer', layers)

    def test_site_properties_registered(self):
        site_properties = self.portal['portal_properties'].site_properties
        self.assertTrue(hasattr(site_properties, 'show_header_text'))
        self.assertFalse(site_properties.show_header_text)
        self.assertTrue(hasattr(site_properties, 'show_header_logo'))
        self.assertTrue(site_properties.show_header_logo)

    def test_static_resource_directory(self):
        app = self.layer['app']

        browser = Browser(app)
        portal_url = self.portal.absolute_url()

        browser.open('%s/++resource++collective.themecustomizer' % portal_url)
        self.assertEqual(browser.headers['status'], '200 Ok')


class UninstallTestCase(unittest.TestCase):
    """Ensure product is properly uninstalled."""

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.qi = self.portal['portal_quickinstaller']
        self.qi.uninstallProducts(products=[PROJECTNAME])

    def test_uninstalled(self):
        self.assertFalse(self.qi.isProductInstalled(PROJECTNAME))

    def test_addon_layer_is_unregistered(self):
        layers = [l.getName() for l in registered_layers()]
        self.assertNotIn('IThemeCustomizer', layers)

    def test_site_properties_unregistered(self):
        site_properties = self.portal['portal_properties'].site_properties
        self.assertFalse(hasattr(site_properties, 'show_header_text'))
        self.assertFalse(hasattr(site_properties, 'show_header_logo'))

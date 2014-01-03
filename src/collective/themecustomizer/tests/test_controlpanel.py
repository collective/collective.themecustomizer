# -*- coding: utf-8 -*-

from collective.themecustomizer.config import PROJECTNAME
from collective.themecustomizer.interfaces import IThemeCustomizer
from collective.themecustomizer.testing import INTEGRATION_TESTING
from plone import api
from zope.interface import directlyProvides

import unittest2 as unittest


class ControlPanelTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        directlyProvides(self.request, IThemeCustomizer)

    def test_controlpanel_adapted(self):
        with api.env.adopt_roles(['Manager']):
            controlpanel = self.portal.restrictedTraverse('@@site-controlpanel')
        controlpanel.setUpWidgets()
        self.assertIsNotNone(controlpanel.widgets.get('image'))
        self.assertIsNotNone(controlpanel.widgets.get('background'))

    def test_controlpanel_deadapted_on_uninstall(self):
        qi = self.portal['portal_quickinstaller']
        with api.env.adopt_roles(['Manager']):
            qi.uninstallProducts(products=[PROJECTNAME])
            controlpanel = self.portal.restrictedTraverse('@@site-controlpanel')
        controlpanel.setUpWidgets()
        self.assertIsNone(controlpanel.widgets.get('image'))
        self.assertIsNone(controlpanel.widgets.get('background'))

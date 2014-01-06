# -*- coding: utf-8 -*-

from plone import api
from plone.app.layout.viewlets.common import LogoViewlet as BaseViewlet
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class LogoViewlet(BaseViewlet):
    """ Custom plone.logo viewlet to show/hide logo image and
    site title and description
    """

    index = ViewPageTemplateFile('templates/logo.pt')

    def update(self):
        super(LogoViewlet, self).update()

        portal = api.portal.get()

        self.navigation_root_title = self.portal_state.navigation_root_title()

        logoTitle = self.portal_state.portal_title()

        # If there already is a customized logo.png image in portal root, use it
        if portal.get('logo.png'):
            self.logo_tag = portal.get('logo.png').tag(title=logoTitle, alt=logoTitle)
        else:
            # If not, get the logo filename from base_properties, if found
            bprops = portal.restrictedTraverse('base_properties', None)
            if bprops is not None:
                logoName = bprops.logoName
            else:
                # If not found, use Plone 4 default logo filename
                logoName = 'logo.jpg'

            self.logo_tag = portal.restrictedTraverse(logoName).tag(title=logoTitle, alt=logoTitle)


class HeaderViewlet(BaseViewlet):
    """ Custom plone.header viewlet to show/hide background image
    """

    def logo_background_style(self):
        portal = api.portal.get()
        if portal.get('background.png'):
            return 'background-image: url(' + portal.absolute_url() + '/background.png)'
        return ''

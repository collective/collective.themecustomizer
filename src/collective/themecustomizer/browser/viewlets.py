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

        portal = self.portal_state.portal()
        bprops = portal.restrictedTraverse('base_properties', None)
        if bprops is not None:
            logoName = bprops.logoName
        else:
            logoName = 'logo.jpg'

        logoTitle = self.portal_state.portal_title()
        self.logo_tag = portal.restrictedTraverse(logoName).tag(title=logoTitle, alt=logoTitle)
        self.navigation_root_title = self.portal_state.navigation_root_title()

        if logoName not in portal:
            self.logo_tag = '<img src="{0}/{1}" alt="{2}" title="{2}" height="80" width="80" />'.format(
                portal.absolute_url(),
                '++resource++collective.themecustomizer/images/logo.png',
                logoTitle
            )


class HeaderViewlet(BaseViewlet):
    """ Custom plone.header viewlet to show/hide background image
    """

    def logo_background_style(self):
        portal = api.portal.get()
        if portal.get('background.png'):
            return 'background-image: url(' + portal.absolute_url() + '/background.png)'
        return ''

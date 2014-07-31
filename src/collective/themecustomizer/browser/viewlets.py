# -*- coding: utf-8 -*-
from plone import api
from plone.app.layout.viewlets.common import LogoViewlet as BaseViewlet
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class LogoViewlet(BaseViewlet):

    """Custom plone.logo viewlet to show portal logo, title and description."""

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

    def show_logo(self):
        """Return the value of the 'show_header_logo' site property."""
        pprops = api.portal.get_tool('portal_properties')
        sprops = pprops.site_properties
        return getattr(sprops, 'show_header_logo', True)

    def show_portal_title(self):
        """Return the value of the 'show_header_text' site property."""
        pprops = api.portal.get_tool('portal_properties')
        sprops = pprops.site_properties
        return getattr(sprops, 'show_header_text', False)

    def get_portal_title(self):
        """Return portal title."""
        return api.portal.get().title

    def get_portal_description(self):
        """Return portal description."""
        return api.portal.get().description


class HeaderViewlet(BaseViewlet):

    """Custom plone.header viewlet to show/hide background image."""

    def logo_background_style(self):
        portal = api.portal.get()
        if portal.get('background.png'):
            return 'background-image: url(' + portal.absolute_url() + '/background.png)'
        return ''

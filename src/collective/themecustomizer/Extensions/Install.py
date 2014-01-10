# -*- coding: utf-8 -*-

from plone import api

PROPERTIES = (
    'show_header_logo',
    'show_header_text',
)


def uninstall(portal, reinstall=False):
    if not reinstall:
        properties_tool = api.portal.get_tool('portal_properties')
        site_properties = properties_tool.site_properties
        site_properties.manage_delProperties(PROPERTIES)
        return 'Ran all uninstall steps.'

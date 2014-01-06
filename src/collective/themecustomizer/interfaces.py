# -*- coding: utf-8 -*-

from collective.themecustomizer import _
from plone.app.controlpanel.site import ISiteSchema as IBaseSiteSchema
from zope import schema
from zope.interface import Interface


class IThemeCustomizer(Interface):
    """Layer especifico para este add-on.
    """


class ISiteSchema(IBaseSiteSchema):

    show_header_text = schema.Bool(
        title=_(u'Display text in Header'),
        description=_(u'Displays site title and description on every site page.'),
        required=False,
        default=False,
    )

    image = schema.Bytes(
        title=_(u'Logo image'),
        description=_(u'The image you upload will replace current site\'s logo. '
                      'Once saved, if you want to get back the original one, just'
                      'remove your chosen image.'),
        required=False,
    )

    show_header_logo = schema.Bool(
        title=_(u'Display logo in Header'),
        description=_(u''),
        required=False,
        default=True,
    )

    background = schema.Bytes(
        title=_(u'Header background image'),
        description=_(u''),
        required=False,
    )

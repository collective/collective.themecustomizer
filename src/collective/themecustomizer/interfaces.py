# -*- coding: utf-8 -*-

from collective.themecustomizer import _
from plone.app.controlpanel.site import ISiteSchema as IBaseSiteSchema
from zope import schema
from zope.interface import Interface


class IThemeCustomizer(Interface):
    """A layer specific for this add-on product.
    """


class ISiteSchema(IBaseSiteSchema):

    show_header_text = schema.Bool(
        title=_(u'Display text in header'),
        description=_(u'Displays site title and description on every site page.'),
        required=False,
        default=False,
    )

    image = schema.Bytes(
        title=_(u'Logo image'),
        description=_(u'The image you upload will replace default site logo. '
                      u'Once saved, if you want to get back the original '
                      u'one, just remove your chosen image.'),
        required=False,
    )

    show_header_logo = schema.Bool(
        title=_(u'Display logo in header'),
        description=_(u''),
        required=False,
        default=True,
    )

    background = schema.Bytes(
        title=_(u'Background image'),
        description=_(u''),
        required=False,
    )

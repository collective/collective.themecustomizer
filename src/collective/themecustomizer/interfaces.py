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
        description=_(u'Displays site title and description on every site pages.'),
        required=False,
        default=True,
    )

    image = schema.Bytes(
        title=_(u'Imagem do Logo'),
        description=_(u'Insira nesse campo o logo do tema local'),
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

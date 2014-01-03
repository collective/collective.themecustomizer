# -*- coding: utf-8 -*-

from collective.themecustomizer.browser.imagewidget import ImageWidget
from collective.themecustomizer.interfaces import ISiteSchema
from plone import api
from plone.app.controlpanel.site import SiteControlPanel as BaseSiteControlPanel
from Products.CMFDefault.formlib.schema import ProxyFieldProperty
from Products.CMFDefault.formlib.schema import SchemaAdapterBase
from Products.CMFPlone.interfaces.siteroot import IPloneSiteRoot
from Products.CMFPlone.utils import safe_unicode
from zope.component import adapts
from zope.formlib import form
from zope.interface import implements


class SiteControlPanelAdapter(SchemaAdapterBase):
    """
    """
    adapts(IPloneSiteRoot)
    implements(ISiteSchema)

    def __init__(self, context):
        super(SiteControlPanelAdapter, self).__init__(context)
        self.portal = api.portal.get()
        pprop = api.portal.get_tool('portal_properties')
        self.context = pprop.site_properties
        self.encoding = pprop.site_properties.default_charset

    def get_site_title(self):
        title = getattr(self.portal, 'title', u'')
        return safe_unicode(title)

    def set_site_title(self, value):
        self.portal.title = value.encode(self.encoding)

    def get_site_description(self):
        description = getattr(self.portal, 'description', u'')
        return safe_unicode(description)

    def set_site_description(self, value):
        if value is not None:
            self.portal.description = value.encode(self.encoding)
        else:
            self.portal.description = ''

    def get_webstats_js(self):
        description = getattr(self.context, 'webstats_js', u'')
        return safe_unicode(description)

    def set_webstats_js(self, value):
        if value is not None:
            self.context.webstats_js = value.encode(self.encoding)
        else:
            self.context.webstats_js = ''

    def get_image(self):
        return self.portal.get('logo.png')

    def set_image(self, image):
        if not image:
            return True
        if image == 'remove':
            self.portal.manage_delObjects(['logo.png'])
            return True
        # verifica se a imagem existe
        conteudo = [i.getId() for i in self.portal.objectValues()]
        if not 'logo.png' in conteudo:
            self.portal.manage_addImage('logo.png', image, 'logo.png')
            return True
        else:
            img = self.portal.get('logo.png')
            img.update_data(image)
            return True
        return False

    def get_background(self):
        return self.portal.get('background.png')

    def set_background(self, image):
        if not image:
            return True
        if image == 'remove':
            self.portal.manage_delObjects(['background.png'])
            return True
        # verifica se a imagem existe
        conteudo = [i.getId() for i in self.portal.objectValues()]
        if not 'background.png' in conteudo:
            self.portal.manage_addImage('background.png', image, 'background.png')
            return True
        else:
            img = self.portal.get('background.png')
            img.update_data(image)
            return True
        return False

    site_title = property(get_site_title, set_site_title)
    site_description = property(get_site_description, set_site_description)
    webstats_js = property(get_webstats_js, set_webstats_js)
    image = property(get_image, set_image)
    background = property(get_background, set_background)

    show_header_text = ProxyFieldProperty(ISiteSchema['show_header_text'])
    show_header_logo = ProxyFieldProperty(ISiteSchema['show_header_logo'])
    enable_sitemap = ProxyFieldProperty(ISiteSchema['enable_sitemap'])
    exposeDCMetaTags = ProxyFieldProperty(ISiteSchema['exposeDCMetaTags'])

    def get_display_pub_date_in_byline(self):
        return getattr(
            self.context.site_properties, 'displayPublicationDateInByline', False)

    def set_display_pub_date_in_byline(self, value):
        self.context.site_properties.displayPublicationDateInByline = value

    display_pub_date_in_byline = property(get_display_pub_date_in_byline,
                                          set_display_pub_date_in_byline)


class SiteControlPanel(BaseSiteControlPanel):
    """
    """
    form_fields = form.FormFields(ISiteSchema)
    form_fields['image'].custom_widget = ImageWidget
    form_fields['background'].custom_widget = ImageWidget

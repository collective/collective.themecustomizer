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
    """This is a copy of p.a.controlpanel.site.SiteControlPanelAdapter
    with the additional code for the fields we are adding as theme
    customization options.
    """

    # TODO: Move this code to theme controlpanel?

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

    def _get_image(self, filename):
        """ Generic code for getting an image by filename
        """
        return self.portal.get(filename)

    def _set_image(self, image, filename):
        """ Create or update OFS.Image.Image object at portal root
        """
        # TODO: Store image in registry or other sensible place?
        if not image:
            return True
        if image == 'remove':
            self.portal.manage_delObjects([filename])
            return True
        # Does image already exists?
        content = [i.getId() for i in self.portal.objectValues()]
        if filename not in content:
            self.portal.manage_addImage(filename, image, filename)
            return True
        else:
            img = self.portal.get(filename)
            img.update_data(image)
            return True
        return False

    def get_image(self):
        """ Get the logo.png image created by setter
        """
        return self._get_image('logo.png')

    def set_image(self, image):
        """ Create or update a logo.png image provided by user
        """
        return self._set_image(image, 'logo.png')

    def get_background(self):
        """ Get the background.png image created by setter
        """
        return self._get_image('background.png')

    def set_background(self, image):
        """ Create or update a background.png image provided by user
        """
        return self._set_image(image, 'background.png')

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

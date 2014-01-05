# -*- coding: utf-8 -*-

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.formlib.textwidgets import FileWidget


class ImageWidget(FileWidget):
    """Custom implementation of ImageWidget
    """

    # The standard FileWidget returns a string instead of an IFile inst,
    # which means it will always fail schema validation in formlib.

    # TODO: Provide a preview scale of the image in the template

    template = ViewPageTemplateFile('templates/imagewidget.pt')
    displayWidth = 30

    def __call__(self):
        value = self._getFormValue() or None
        return self.template(name=self.context.__name__, value=value)

    def _toFieldValue(self, input):
        action = self.request.get('%s.action' % self.name, None)
        if action == 'remove':
            return 'remove'
        value = super(ImageWidget, self)._toFieldValue(input)
        return value

    def hasInput(self):
        return ((self.name + '.used' in self.request.form)
                or
                (self.name in self.request.form)
                ) and not self.request.form.get(self.name + '.nochange', '')

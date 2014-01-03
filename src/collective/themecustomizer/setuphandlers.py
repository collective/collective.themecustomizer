# -*- coding: utf-8 -*-

from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implements


class HiddenProfiles(object):
    implements(INonInstallable)

    def getNonInstallableProfiles(self):
        return [
        ]

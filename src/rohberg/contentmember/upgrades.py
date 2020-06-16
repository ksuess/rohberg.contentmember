# -*- coding: utf-8 -*-
from plone import api
from plone.app.upgrade.utils import loadMigrationProfile
import logging


def indexAuthors(context, logger=None):
    if logger is None:
        # Called as upgrade step: define our own logger.
        logger = logging.getLogger('your.addonpackage')
    
    PROFILE_ID = 'profile-rohberg.contentmember:default'
    setup = api.portal.get_tool('portal_setup')
    setup.runImportStepFromProfile(PROFILE_ID, 'catalog')

    catalog = api.portal.get_tool('portal_catalog')
    brains = catalog(portal_type='zhkathpage')
    count = 0
    for brain in brains:
        obj = brain.getObject()
        obj.reindexObject()

    setup.runImportStepFromProfile(PROFILE_ID, 'catalog')
    logger.info('%s pages indexed.' % count)

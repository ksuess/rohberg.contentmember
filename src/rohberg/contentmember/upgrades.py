# -*- coding: utf-8 -*-
from plone import api

# from plone.app.upgrade.utils import loadMigrationProfile
import logging


PROFILE_ID = "profile-rohberg.contentmember:default"


def indexAuthors(context, logger=None):
    if logger is None:
        # Called as upgrade step: define our own logger.
        logger = logging.getLogger("your.addonpackage")

    PROFILE_ID = "profile-rohberg.contentmember:default"

    setup = api.portal.get_tool("portal_setup")
    setup.runImportStepFromProfile(PROFILE_ID, "catalog")

    catalog = api.portal.get_tool("portal_catalog")
    brains = catalog(portal_type="zhkathpage")  # author?
    count = 0
    for brain in brains:
        obj = brain.getObject()
        obj.reindexObject()

    setup.runImportStepFromProfile(PROFILE_ID, "catalog")
    logger.info("%s pages indexed." % count)


def updateCatalog(context, logger=None):
    if logger is None:
        # Called as upgrade step: define our own logger.
        logger = logging.getLogger("rohberg.contentmember")

    setup = api.portal.get_tool("portal_setup")
    setup.runImportStepFromProfile(PROFILE_ID, "catalog")
    brains = api.content.find(portal_type="zhkathauthor")
    for brain in brains:
        obj = brain.getObject()
        obj.reindexObject()
    logger.info(f"{len(brains)} rohberg.contentmember objects reindexed")


def index_last_name(context, logger=None):
    updateCatalog(context)

    if logger is None:
        # Called as upgrade step: define our own logger.
        logger = logging.getLogger("rohberg.contentmember")

    setup = api.portal.get_tool("portal_setup")
    setup.runImportStepFromProfile(PROFILE_ID, "plone.app.registry")


def install_dependencies(context, logger=None):
    if logger is None:
        # Called as upgrade step: define our own logger.
        logger = logging.getLogger("rohberg.contentmember")

    setup = api.portal.get_tool("portal_setup")
    setup.runImportStepFromProfile(PROFILE_ID, "plone.app.registry")

    logger.info("tinymce registry settings updated.")

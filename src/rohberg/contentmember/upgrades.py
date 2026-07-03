# -*- coding: utf-8 -*-
from plone import api

# from plone.app.upgrade.utils import loadMigrationProfile
import logging
logger = logging.getLogger("rohberg.contentmember")


PROFILE_ID = "profile-rohberg.contentmember:default"


def indexAuthors(context):
    context.runImportStepFromProfile(PROFILE_ID, "catalog")

    catalog = api.portal.get_tool("portal_catalog")
    brains = catalog(portal_type="zhkathpage")  # author?
    count = 0
    for brain in brains:
        obj = brain.getObject()
        obj.reindexObject()

    context.runImportStepFromProfile(PROFILE_ID, "catalog")
    logger.info("%s pages indexed." % count)


def updateCatalog(context):
    context.runImportStepFromProfile(PROFILE_ID, "catalog")
    brains = api.content.find(portal_type="zhkathauthor")
    for brain in brains:
        obj = brain.getObject()
        obj.reindexObject()
    logger.info(f"{len(brains)} rohberg.contentmember objects reindexed")


def index_last_name(context):
    updateCatalog(context)

    context.runImportStepFromProfile(PROFILE_ID, "plone.app.registry")


def dummy(context):
    logger.info("dummy upgrade step")


def add_teamcategory_behavior(context):
    # Import registry settings for query field
    context.runImportStepFromProfile(PROFILE_ID, "plone.app.registry")
    logger.info("Imported registry settings for teamcategory query field")

    # Import catalog configuration
    context.runImportStepFromProfile(PROFILE_ID, "catalog")
    logger.info("Updated catalog configuration")

    # Reindex all content to make teamcategory field searchable
    brains = api.content.find(portal_type="zhkathauthor")
    for brain in brains:
        obj = brain.getObject()
        obj.reindexObject()

    logger.info(f"Reindexed {len(brains)} objects for teamcategory field")

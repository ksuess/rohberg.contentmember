# -*- coding: utf-8 -*-
from rohberg.contentmember.content.zhkathauthor import IZhkathauthor  # NOQA E501
from rohberg.contentmember.testing import ROHBERG_CONTENTMEMBER_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest


try:
    from plone.dexterity.schema import portalTypeToSchemaName
except ImportError:
    # Plone < 5
    from plone.dexterity.utils import portalTypeToSchemaName


class ZhkathauthorIntegrationTest(unittest.TestCase):

    layer = ROHBERG_CONTENTMEMBER_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_ct_zhkathauthor_schema(self):
        fti = queryUtility(IDexterityFTI, name='zhkathauthor')
        schema = fti.lookupSchema()
        schema_name = portalTypeToSchemaName('zhkathauthor')
        self.assertEqual(schema_name, schema.getName())

    def test_ct_zhkathauthor_fti(self):
        fti = queryUtility(IDexterityFTI, name='zhkathauthor')
        self.assertTrue(fti)

    def test_ct_zhkathauthor_factory(self):
        fti = queryUtility(IDexterityFTI, name='zhkathauthor')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IZhkathauthor.providedBy(obj),
            u'IZhkathauthor not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_zhkathauthor_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='zhkathauthor',
            id='zhkathauthor',
        )

        self.assertTrue(
            IZhkathauthor.providedBy(obj),
            u'IZhkathauthor not provided by {0}!'.format(
                obj.id,
            ),
        )

# -*- coding: utf-8 -*-
from rohberg.contentmember.behaviors.expert import IExpertMarker
from rohberg.contentmember.testing import ROHBERG_CONTENTMEMBER_INTEGRATION_TESTING  # noqa
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from zope.component import getUtility

import unittest


class ExpertIntegrationTest(unittest.TestCase):

    layer = ROHBERG_CONTENTMEMBER_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_expert(self):
        behavior = getUtility(IBehavior, 'rohberg.contentmember.expert')
        self.assertEqual(
            behavior.marker,
            IExpertMarker,
        )

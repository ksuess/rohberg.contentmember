# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from rohberg.contentmember.testing import ROHBERG_CONTENTMEMBER_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that rohberg.contentmember is properly installed."""

    layer = ROHBERG_CONTENTMEMBER_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if rohberg.contentmember is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'rohberg.contentmember'))

    def test_browserlayer(self):
        """Test that IRohbergContentmemberLayer is registered."""
        from rohberg.contentmember.interfaces import (
            IRohbergContentmemberLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IRohbergContentmemberLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = ROHBERG_CONTENTMEMBER_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['rohberg.contentmember'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if rohberg.contentmember is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'rohberg.contentmember'))

    def test_browserlayer_removed(self):
        """Test that IRohbergContentmemberLayer is removed."""
        from rohberg.contentmember.interfaces import \
            IRohbergContentmemberLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IRohbergContentmemberLayer,
            utils.registered_layers())

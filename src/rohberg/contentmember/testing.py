# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import rohberg.contentmember


class RohbergContentmemberLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=rohberg.contentmember)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'rohberg.contentmember:default')


ROHBERG_CONTENTMEMBER_FIXTURE = RohbergContentmemberLayer()


ROHBERG_CONTENTMEMBER_INTEGRATION_TESTING = IntegrationTesting(
    bases=(ROHBERG_CONTENTMEMBER_FIXTURE,),
    name='RohbergContentmemberLayer:IntegrationTesting',
)


ROHBERG_CONTENTMEMBER_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(ROHBERG_CONTENTMEMBER_FIXTURE,),
    name='RohbergContentmemberLayer:FunctionalTesting',
)


ROHBERG_CONTENTMEMBER_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        ROHBERG_CONTENTMEMBER_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='RohbergContentmemberLayer:AcceptanceTesting',
)

# -*- coding: utf-8 -*-

try:
    from plone.app.dexterity import textindexer
except ImportError:
    from collective import dexteritytextindexer as textindexer
from plone import schema
from plone.autoform.directives import order_after, widget
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from Products.CMFPlone.utils import safe_hasattr
from rohberg.contentmember import _
from z3c.form.browser.radio import RadioFieldWidget
from zope.component import adapter
from zope.interface import implementer, Interface, provider


class IExpertMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IExpert(model.Schema):
    """ """

    # textindexer.searchable('region') # extra index for filtering by region
    textindexer.searchable("organisation")

    region = schema.TextLine(title=_("Region"), required=False)
    organisation = schema.TextLine(
        title=_("Organisation"),
        required=False,
    )

    order_after(organisation="last_name")
    order_after(region="last_name")


@implementer(IExpert)
@adapter(IExpertMarker)
class Expert(object):
    def __init__(self, context):
        self.context = context

    @property
    def region(self):
        if safe_hasattr(self.context, "region"):
            return self.context.region
        return None

    @region.setter
    def region(self, value):
        self.context.region = value

    @property
    def organisation(self):
        if safe_hasattr(self.context, "organisation"):
            return self.context.organisation
        return None

    @organisation.setter
    def organisation(self, value):
        self.context.organisation = value

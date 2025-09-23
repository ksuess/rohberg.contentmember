# -*- coding: utf-8 -*-

try:
    from plone.app.dexterity import textindexer
except ImportError:
    from collective import dexteritytextindexer as textindexer
from plone import schema
from plone.autoform.directives import widget
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from Products.CMFPlone.utils import safe_hasattr
from rohberg.contentmember import _
from plone.app.z3cform.widget import AjaxSelectFieldWidget
from zope.component import adapter
from zope.interface import implementer, Interface, provider


class ITeamcategoryMarker(Interface):
    pass


@provider(IFormFieldProvider)
class ITeamcategory(model.Schema):
    """ """

    textindexer.searchable("teamcategory")

    fieldset(
        'categorization',
        label=_('Categorization'),
        fields=['teamcategory']
    )

    widget(
        'teamcategory',
        AjaxSelectFieldWidget,
        vocabulary="rohberg.contentmember.teamcategory"
    )
    teamcategory = schema.Tuple(
        title=_("Team Category"),
        description=_("Team categories for this item"),
        value_type=schema.TextLine(),
        required=False,
        missing_value=(),
    )


@implementer(ITeamcategory)
@adapter(ITeamcategoryMarker)
class Teamcategory(object):
    def __init__(self, context):
        self.context = context

    @property
    def teamcategory(self):
        if safe_hasattr(self.context, "teamcategory"):
            value = self.context.teamcategory
            if value is None:
                return ()
            return value
        return ()

    @teamcategory.setter
    def teamcategory(self, value):
        if value is None:
            value = ()
        self.context.teamcategory = value

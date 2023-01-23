# collective.dexteritytextindexer is integrated in Plon 6. Use plone.app.dexterity instead.
try:
    from plone.app.dexterity import textindexer
except ImportError:
    from collective import dexteritytextindexer as textindexer
from dexterity.membrane.behavior.user import INameFromFullName
from dexterity.membrane.content.member import IMember, is_email
from plone.autoform.directives import widget
from plone.dexterity.content import Item

# from plone.supermodel import model
from rohberg.contentmember.fields import URI_noprotocol
from zope import schema
from zope.interface import implementer

from rohberg.contentmember import _


class IZhkathauthor(IMember):
    """Marker interface for Zhkathauthor."""

    # TODO: make membrane fields searchable
    textindexer.searchable("first_name")
    textindexer.searchable("last_name")
    textindexer.searchable("companyposition")
    textindexer.searchable("bio")

    website = URI_noprotocol(
        title=_("Website"),
        description=_("e.g. www.abcjazzz.com"),
        required=False,
    )
    companyposition = schema.TextLine(
        title=_("label_companyposition", default="Position"),
        description=_(
            "help_companyposition",
            default="Funktion in seiner oder ihrer Organisation / Firma",
        ),
        required=False,
    )

    telnr = schema.TextLine(title=_("label_telnr", default="Telefon"), required=False)
    telnr_label = schema.TextLine(
        title=_("label_telnr_label", default="Label Telefon"), required=False
    )

    telnr2 = schema.TextLine(
        title=_("label_telnr2", default="Telefon #2"), required=False
    )
    telnr2_label = schema.TextLine(
        title=_("label_telnr2_label", default="Label Telefon #2"), required=False
    )

    alternativeEmail = schema.TextLine(
        title=_("label_alternativeEmail", default="alternative E-Mail"),
        required=False,
        constraint=is_email,
    )

    widget(authortype="z3c.form.browser.checkbox.CheckBoxFieldWidget")
    authortype = schema.Set(
        title=_("label_authortype", default="Typ"),
        value_type=schema.Choice(values=["Autor", "Kontakt"]),
        # required=True,
        required=False,
    )

    show_email = schema.Bool(
        title=_("show_email", default="Zeige Email in Kontaktkarte"), default=True
    )

    show_tagged_news_and_blogposts = schema.List(
        title=_(
            "show_tagged_news_and_blogposts",
            default="Zeige News und Blog-Posts nach Schlagwörtern",
        ),
        value_type=schema.Choice(source="plone.app.vocabularies.Keywords"),
        required=False,
    )


IZhkathauthor["homepage"].title = "homepage"


@implementer(IZhkathauthor)
class Zhkathauthor(Item):
    """ """

    def Title(self):
        return INameFromFullName(self).title

    @property
    def title(self):
        return INameFromFullName(self).title

    @title.setter
    def title(self, value):
        # self.context.title = value
        pass

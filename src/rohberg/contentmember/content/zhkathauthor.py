# coding: utf-8
from collective import dexteritytextindexer
from dexterity.membrane.behavior.user import INameFromFullName
from dexterity.membrane.content.member import IMember
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
    dexteritytextindexer.searchable('first_name')
    dexteritytextindexer.searchable('last_name')
    dexteritytextindexer.searchable('companyposition')
    dexteritytextindexer.searchable('bio')

    website = URI_noprotocol(
        title=_(u"Website"),
        description=_(u"e.g. www.abcjazzz.com"),
        required=False,
    )
    companyposition = schema.TextLine(
        title=_(u'label_companyposition', default=u'Position'),
        description=_(u'help_companyposition', default=u'Funktion innerhalb seiner oder ihrer Organisation / Firma'),
        required=False
    )

    telnr = schema.TextLine(
        title=_(u'label_telnr', default=u'Telefon'),
        required=False
    )
    telnr_label = schema.TextLine(
        title=_(u'label_telnr_label', default=u'Label Telefon'),
        required=False
    )

    telnr2 = schema.TextLine(
        title=_(u'label_telnr2', default=u'Telefon #2'),
        required=False
    )
    telnr2_label = schema.TextLine(
        title=_(u'label_telnr2_label', default=u'Label Telefon #2'),
        required=False
    )

    widget(authortype='z3c.form.browser.checkbox.CheckBoxFieldWidget')
    authortype = schema.Set(
        title=_(u"label_authortype", default=u"Typ"),
        value_type=schema.Choice(values=['Autor', 'Kontakt']),
        required=True,
        )

    show_email = schema.Bool(
        title=_(u"show_email", default=u"Zeige Email in Kontaktkarte"),
        default=True
    )


IZhkathauthor['homepage'].title = u"homepage"


@implementer(IZhkathauthor)
class Zhkathauthor(Item):
    """
    """
    def Title(self):
        return INameFromFullName(self).title

    @property
    def title(self):
        return INameFromFullName(self).title

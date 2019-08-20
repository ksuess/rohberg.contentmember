# coding: utf-8
from collective import dexteritytextindexer
from plone.app.textfield import RichText
from plone.app.z3cform.widget import RichTextFieldWidget
from plone.autoform import directives
from plone.dexterity.content import Item
from plone.supermodel import model
from plone.schema import Email
from rohberg.contentmember.fields import URI_noprotocol
from zope import schema
from zope.interface import implementer

from rohberg.contentmember import _


class IMember(model.Schema):
    """Define Author."""

    first_name = schema.TextLine(
        title=_(u'First Name'),
        required=True,
    )

    last_name = schema.TextLine(
        title=_(u'Last Name'),
        required=True,
    )

    email = Email(
        # String with validation in place looking for @, required.
        # Note that a person's email address will be their username.
        title=_(u'E-mail Address'),
        required=True,
    )
    #
    # homepage = schema.URI(
    #     # url format
    #     title=_(u'External Homepage'),
    #     required=False,
    # )

    directives.widget('bio', RichTextFieldWidget)
    bio = RichText(
        title=_(u'Biography'),
        required=False,
    )


class IZhkathauthor(IMember):
    """Marker interface for Zhkathauthor."""

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

    directives.widget(authortype='z3c.form.browser.checkbox.CheckBoxFieldWidget')
    authortype = schema.Set(
        title=_(u"label_authortype", default=u"Typ"),
        value_type=schema.Choice(values=['Autor', 'Kontakt']),
        required=True,
        )

    show_email = schema.Bool(
        title=_(u"show_email", default=u"Zeige Email in Kontaktkarte"),
        default=True
    )


@implementer(IZhkathauthor)
class Zhkathauthor(Item):
    """
    """
    def Title(self):
        return self.title

    @property
    def title(self):
        names = [
            self.first_name,
            self.last_name,
        ]
        return u' '.join([name for name in names if name])

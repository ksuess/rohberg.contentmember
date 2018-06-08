# coding: utf-8
from collective import dexteritytextindexer
from dexterity.membrane.behavior.user import INameFromFullName
from dexterity.membrane.content.member import IMember
from plone.dexterity.content import Item
from plone.supermodel import model
from rohberg.contentmember.fields import URI_noprotocol
from zope import schema
from zope.interface import implementer

from rohberg.contentmember import _

class IZhkathauthor(IMember):
    """ Marker interface for Zhkathauthor
    """

    # TODO: make membrane fields searchable
    dexteritytextindexer.searchable('first_name')
    dexteritytextindexer.searchable('last_name')
    dexteritytextindexer.searchable('companyposition')
    dexteritytextindexer.searchable('bio')
    
    website = URI_noprotocol(
        title=_(u"Website"),
        description = _(u"e.g. www.abcjazzz.com"),
        required = False,
    )
    companyposition = schema.TextLine(
        title=_(u'label_companyposition', default=u'Position'),
        description=_(u'help_companyposition', default=u''),
        required=False
    )


IZhkathauthor['homepage'].title = u"TODO: hide this field homepage"

@implementer(IZhkathauthor)
class Zhkathauthor(Item):
    """
    """
    def Title(self):
        return INameFromFullName(self).title

    @property
    def title(self):
        return INameFromFullName(self).title

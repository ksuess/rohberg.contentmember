# coding: utf-8
from dexterity.membrane.content.member import IMember
from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer


class IZhkathauthor(IMember):
    """ Marker interface for Zhkathauthor
    """


@implementer(IZhkathauthor)
class Zhkathauthor(Container):
    """
    """

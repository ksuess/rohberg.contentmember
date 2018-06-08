# -*- coding: utf-8 -*-
from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer


class IZhkathauthor(model.Schema):
    """ Marker interface for Zhkathauthor
    """


@implementer(IZhkathauthor)
class Zhkathauthor(Container):
    """
    """

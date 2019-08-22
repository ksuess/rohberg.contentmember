# -*- coding: utf-8 -*-
from plone import api
from plone.app.vocabularies.catalog import KeywordsVocabulary
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm


@implementer(IVocabularyFactory)
class AuthortypeVocabulary(KeywordsVocabulary):
    keyword_index = 'authortype'


AuthortypeVocabularyFactory = AuthortypeVocabulary()


def authorsVocabulary(context):

    catalog = api.portal.get_tool(name='portal_catalog')
    brains = catalog.searchResults(portal_type=["zhkathauthor"])
    items = [(item.id, item.Title) for item in brains]
    terms = [SimpleTerm(value=pair[0], token=pair[0], title=pair[1]) for pair in items ]
    return SimpleVocabulary(terms)

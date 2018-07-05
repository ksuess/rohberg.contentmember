# -*- coding: utf-8 -*-
from plone.app.vocabularies.catalog import KeywordsVocabulary
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory

@implementer(IVocabularyFactory)
class AuthortypeVocabulary(KeywordsVocabulary):
    keyword_index = 'authortype'

AuthortypeVocabularyFactory = AuthortypeVocabulary()

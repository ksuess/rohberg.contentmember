# coding: utf-8
from plone import api
from plone.dexterity.browser.view import DefaultView
from plone.memoize.view import memoize, memoize_contextless
from Products.Five import BrowserView
from zope.interface import alsoProvides

import logging
logger = logging.getLogger(__name__)
import pprint

try:
    from plone.protect.interfaces import IDisableCSRFProtection
    HAS_PLONE_PROTECT = True
except ImportError:
    HAS_PLONE_PROTECT = False


# @memoize_contextless
def getAuthors(brain):
    """Return MembraneUsers.

    args
    obj: brain

    return 
    MembraneUsers of creators list
    """
    creators = brain.listCreators
    if creators == []:
        return None
    membrane_tool = api.portal.get_tool("membrane_tool")
    membraneusers = [membrane_tool.getUserObject(user_id=crt) for crt in creators]
    return membraneusers


class ProfileView(DefaultView):
    """
    """
    @memoize
    def author_content(self):
        """Zeige Content der vom Autor erstellt wurde.
        
        returns tuple: items and number of items
        """
        results = []

        # plone_view = self.context.restrictedTraverse(
        #     '@@plone'
        # )

        brains = api.portal.get_tool("portal_catalog").searchResults(
            authors=(self.context.UID(),), # TODO
            sort_on='effective',
            sort_order='reverse',
            portal_type=['zhkathpage',],
            pagetype = ["Meinung"]
        )

        # print("** author_content for {} UID: {} count: {}".format(self.context.title, self.context.UID(), len(brains)))

        for brain in brains[:12]:
            data = {
                'title': brain.Title,
                # 'date': plone_view.toLocalizedTime(
                #     brain.Date
                # ),
                'url': brain.getURL(),
                # 'authors': getAuthors(brain),
                # 'label': brain.getObject().label,
                # 'description': brain.beschreibung_themenseite
            }
            results.append(data)

        return (results, len(brains))

    @memoize
    def getSubjectsContent(self):
        # show_tagged_news_and_blogposts
        if not getattr(self.context, 'show_tagged_news_and_blogposts', False):
            print("getSubjectsContent no subjects set.")
            return ([], 0)
        
        results = []

        # plone_view = self.context.restrictedTraverse(
        #     '@@plone'
        # )
        brains = api.portal.get_tool("portal_catalog").searchResults(
            Subject = getattr(self.context, 'show_tagged_news_and_blogposts', False),
            sort_on='effective',
            sort_order='reverse',
            portal_type=['zhkathpage',],
            pagetype = ["Beitrag", "Meinung"],
        )
        for brain in brains[:12]:
            data = {
                'title': brain.Title,
                # 'subjects': brain.Subject,
                # 'date': plone_view.toLocalizedTime(
                #     brain.Date
                # ),
                'url': brain.getURL(),
                # 'authors': getAuthors(brain),
                # 'label': brain.getObject().label,
                # 'description': brain.beschreibung_themenseite
            }
            results.append(data)

        # print("getSubjectsContent", results, len(brains))
        return (results, len(brains))
    def subjectsquery(self):
        subjects = getattr(self.context, 'show_tagged_news_and_blogposts', False)
        # print("subjectsquery subjects", subjects)
        if not subjects:
            return ''
        result = ''
        for subject in subjects:
            result += '&Subject=' + subject
        return result


class MembraneUserCreationView(BrowserView):
    """Show some data for debugging.

    Call with <path to folder>/createmembraneusers
    """

    def foo(self):
        """Foo."""
        return 'foo'

    def __call__(self):
        """Call TestView."""
        alsoProvides(self.request, IDisableCSRFProtection)
        context = self.context
        portal = api.portal.get()
        catalog = api.portal.get_tool('portal_catalog')

        logger.info("*** MembraneUserCreationView")
        
        # ~/Google Drive/Code/Snippets_Python/filesystem/read_membrane_data_csv 
        import csv
        from DateTime import DateTime
        now = DateTime()

        filename = '/Users/katjasuss/Google Drive/Code/Snippets_Python/filesystem/read_membrane_data_csv/membrane_data.csv'
        delimiter = ';'
        portal_type = 'zhkathauthor'

        with open(filename, newline='') as csvfile:
            myreader = csv.reader(csvfile, delimiter=delimiter, quotechar='|')
            for row in myreader:
                options = {
                    # 'description': len(row) > 5 and row[5] or ''
                    'email': row[2],
                    'first_name': row[0],
                    'last_name': row[1],
                    'companyposition': len(row) > 4 and row[4] or ''
                    # TODO subjects
                }
                obj = api.content.create(
                    type=portal_type,
                    container=context,
                    id=now.strftime("membraneuser_%Y%m%d_%H%M"),
                    safe_id=True,
                    **options)
                print('object created: ', obj)
                print(', '.join(row))

        print(f"MembraneUserCreationView done. {now}")
        return f"MembraneUserCreationView done. {now}"

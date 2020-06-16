# coding: utf-8
from plone import api
from plone.dexterity.browser.view import DefaultView
from plone.memoize.view import memoize, memoize_contextless
from Products.Five import BrowserView

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
    # @property
    def author_content(self):
        """Zeige Content der vom Autor erstellt wurde."""
        results = []

        plone_view = self.context.restrictedTraverse(
            '@@plone'
        )

        brains = api.portal.get_tool("portal_catalog").searchResults(
            authors=(self.context.UID(),), # TODO
            sort_on='effective',
            sort_order='reverse',
            portal_type=['zhkathpage',],
            pagetype = ["Meinung"]
        )

        # print("** author_content for {} UID: {} count: {}".format(self.context.title, self.context.UID(), len(brains)))

        for brain in brains[:10]:
            data = {
                'title': brain.Title,
                'date': plone_view.toLocalizedTime(
                    brain.Date
                ),
                'url': brain.getURL(),
                'authors': getAuthors(brain),
                'label': brain.getObject().label,
                'description': brain.beschreibung_themenseite
            }
            results.append(data)

        return (results, len(brains))

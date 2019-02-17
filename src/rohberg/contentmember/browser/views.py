# coding: utf-8
from plone import api
from plone.dexterity.browser.view import DefaultView
from Products.Five import BrowserView

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
            Creator=self.context.UID(),
            sort_on='created',
            sort_order='reverse',
            portal_type=['zhkathpage', 'zhkathcollection']
        )

        # print("author_content for {}".format(self.context.UID()))

        for brain in brains[:10]:
            # print("brain.id {}".format(brain.id))
            results.append({
                'title': brain.Title,
                'date': plone_view.toLocalizedTime(
                    brain.Date
                ),
                'url': brain.getURL()
            })

        return results

from Products.Archetypes.public import listTypes
from Products.Archetypes.Extensions.utils import installTypes, \
     install_subskin
from Products.CMFCore.utils import getToolByName
from Products.CMFCore import CMFCorePermissions
from cStringIO import StringIO

from Products.PloneAtom.config import *

def install(self):
    out = StringIO()
    installTypes(self, out, listTypes(PKG_NAME), PKG_NAME)
    install_subskin(self, out, GLOBALS)

    setupActions(self)
    
    print >> out, "Successfully installed %s." % PKG_NAME
    return out.getvalue()

def setupActions(obj):
    """ Add the atom action and actionicon. """
    at = getToolByName(obj, 'portal_actions')
    ait = getToolByName(obj, 'portal_actionicons')
    for action in at.listActions():
        if action.getId() == 'atom':
            break
    else:
        at.addAction(id = 'atom',
                     name = "Atom feed of this folder's contents",
                     action = "string:$object_url/ATOM",
                     condition = "python:portal.portal_syndication.isSyndicationAllowed(object)",
                     permission = CMFCorePermissions.View,
                     category = 'document_actions',
                     visible = True)
    for ai in ait.listActionIcons():
        if ai.getActionId() == 'atom':
            break
    else:
        ait.addActionIcon(category = 'plone',
                          action_id = 'atom',
                          icon_expr = 'atom.gif',
                          title = 'Atom Syndication')

PloneAtom

 This is a Plone product (that could probably be trivially modified for
 the CMF itself) which provides atom support for Plone.  Currently it
 provides the atom syndication format for folderish objects, in the same
 way as RSS syndication is implemented.

 Enabling Atom syndication

  Atom syndication is enabled in exactly the same way as RSS
  syndication.  To enable syndication on the site in general:
  
  * Login as an admin user.

  * Go to 'Plone Setup' and choose 'Zope Management Interface'

  * Select the 'Properties' tab in the 'portal_syndication' tool.

  * Click 'enable syndication'.

  Then, to enable syndication support for a particular folderish object:

  * Login as a user who has Owner/Manager permission for the folder.

  * Surf to that folder and select the 'syndication' tab.

  * Click 'Enable syndication'.  Don't worry about the syndication
    options it gives you -- they are not used by atom (and ignored in
    most RSS clients, from what I've seen).

 Using Atom syndication

  To access the Atom syndicated version of a particular folder, the URL
  is that folder with '/ATOM' appended.  For example, if you are looking
  for the syndicated version of 'http://www.example.com/plone/folder/',
  it would be at 'http://www.example.com/plone/folder/ATOM'.

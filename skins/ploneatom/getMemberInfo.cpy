## Script (Python) "getMemberInfo"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=memberId
##title=Get information for a member
##
return context.portal_membership.getMemberById(memberId)

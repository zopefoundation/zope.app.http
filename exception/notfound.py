##############################################################################
#
# Copyright (c) 2003 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.0 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""

$Id: notfound.py,v 1.3 2003/06/23 17:17:05 sidnei Exp $
"""
__metaclass__ = type

from zope.app.interfaces.http import IHTTPException
from zope.interface import implements

class NotFound:

    implements(IHTTPException)

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        if self.request.method in ['MKCOL'] and self.request.getTraversalStack():
            # MKCOL with non-existing parent.
            self.request.response.setStatus(409)
        else:
            self.request.response.setStatus(404)
        return ''

    __str__ = __call__
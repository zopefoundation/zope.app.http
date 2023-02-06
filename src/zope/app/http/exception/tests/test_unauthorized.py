##############################################################################
#
# Copyright (c) 2001, 2002 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Unauthorized Exception Test
"""
from unittest import TestCase
from unittest import makeSuite

from zope.publisher.browser import TestRequest
from zope.publisher.interfaces.http import IHTTPException


class Test(TestCase):

    def testbasicauth(self):
        from zope.app.http.exception.unauthorized import Unauthorized
        exception = Exception()
        try:
            raise exception
        except:  # noqa: E722 do not use bare 'except'
            pass
        request = TestRequest()
        u = Unauthorized(exception, request)

        # Chech that we implement the right interface
        self.assertTrue(IHTTPException.providedBy(u))

        # Call the view
        u()

        # Make sure the response status was set
        self.assertEqual(request.response.getStatus(), 401)
        self.assertTrue(request.response.getHeader(
            'WWW-Authenticate', '', True).startswith('basic'))


def test_suite():
    return makeSuite(Test)

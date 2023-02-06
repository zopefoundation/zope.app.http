##############################################################################
#
# Copyright (c) 2003 Zope Foundation and Contributors.
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
"""Zope-specific HTTP interfaces
"""
from zope.interface import Attribute
from zope.interface import Interface
# BBB import
from zope.publisher.interfaces.http import IHTTPException  # noqa: F401 unused


class INullResource(Interface):
    """Placeholder objects for new container items to be created via PUT
    """

    container = Attribute("The container of the future resource")
    name = Attribute("The name of the object to be created.")

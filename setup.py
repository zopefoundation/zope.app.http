##############################################################################
#
# Copyright (c) 2006 Zope Foundation and Contributors.
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
# This package is developed by the Zope Toolkit project, documented here:
# https://zopetoolkit.readthedocs.io/en/latest/
# When developing and releasing this package, please follow the documented
# Zope Toolkit policies as described by this documentation.
##############################################################################
"""Setup for zope.app.http package
"""
import os

from setuptools import find_packages
from setuptools import setup


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


setup(name='zope.app.http',
      version='5.1.dev0',
      author='Zope Foundation and Contributors',
      author_email='zope-dev@zope.dev',
      description='HTTP Behavior for the Zope Publisher',
      long_description=(
          read('README.txt')
          + '\n\n' +
          read('CHANGES.txt')
      ),
      keywords="zope3 http publisher view",
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Zope Public License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
          'Programming Language :: Python :: 3.11',
          'Programming Language :: Python :: 3.12',
          'Programming Language :: Python :: 3.13',
          'Programming Language :: Python :: Implementation',
          'Programming Language :: Python :: Implementation :: CPython',
          'Programming Language :: Python :: Implementation :: PyPy',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Topic :: Internet :: WWW/HTTP',
          'Framework :: Zope :: 3',
      ],
      url='https://github.com/zopefoundation/zope.app.http',
      license='ZPL-2.1',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['zope', 'zope.app'],
      python_requires='>=3.9',
      extras_require=dict(
          test=[
              'zope.app.wsgi[testlayer] >= 4.0',
              'zope.browserpage',
              'zope.component',
              'zope.login',
              'zope.password',
              'zope.principalregistry',
              'zope.securitypolicy >= 4.0.0a1',
              'zope.site >= 4.0.0a1',
              'zope.testrunner',
          ]),
      install_requires=[
          'setuptools',
          'zope.interface',
          'zope.publisher>=4.0.0a2',
          'zope.container >= 4.0.0a2',
          'zope.filerepresentation',
      ],
      include_package_data=True,
      zip_safe=False,
      )

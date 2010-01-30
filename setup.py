import sys, os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version='0.1dev'


setup(name = 'zojax.harvest.rss',
      version = version,
      author = 'Andrey Fedoseev',
      author_email = 'andrey.fedoseev@zojax.com',
      description = "Harvest RSS feeds and convert them to content objects.",
      long_description = (
          'Detailed Documentation\n' +
          '======================\n'
          + '\n\n' +
          read('CHANGES.txt')
          ),
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Framework :: Zope3'],
      license='ZPL 2.1',
      packages=find_packages('src'),
      package_dir = {'':'src'},
      namespace_packages=['zojax', 'zojax.harvest'],
      install_requires = ['setuptools', 'rwproperty',
                          'zope.app.publisher',
                          'zojax.product',
                          'zojax.controlpanel',
                          'zojax.layoutform',
                          'zojax.statusmessage',
                          'zojax.content.space',
                          'feedparser',
                          'beautifulsoup',
                          'scheduler',
                          'zojax.rating',
                          ],
      extras_require = dict(test=['zope.app.testing',
                                  'zope.app.zcmlfiles',
                                  'zope.testing',
                                  'zope.testbrowser',
                                  'zope.securitypolicy',
                                  'zojax.autoinclude',
                                  'zojax.security',
                                  ]),
      include_package_data = True,
      zip_safe = False,
      )

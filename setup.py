import os

from setuptools import setup, find_packages

from dbas.views.helper import version

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGELOG.md')) as f:
    CHANGES = f.read()

requires = []

setup(name='dbas',
      version=version,
      description='Novel prototype for a dialog-based online argumentation',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: NGINX :: Application",
      ],
      author='hhucn',
      author_email='dbas@cs.hhu.de',
      url='https://dbas.cs.hhu.de',
      keywords='web pyramid pylons dialog-based argumentation software',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="dbas",
      entry_points="""\
      [paste.app_factory]
      main = dbas:main
      [console_scripts]
      init_discussion_sql = dbas.database.initializedb:main_discussion
      init_field_test_sql = dbas.database.initializedb:main_field_test
      init_news_sql = dbas.database.initializedb:main_news
      init_empty_sql = dbas.database.initializedb:blank_file
      init_drop_sql = dbas.database.initializedb:drop_it
      init_dummy_votes = dbas.database.initializedb:init_dummy_votes
      promote_to_admin = dbas.console_scripts:promote_user
      demote_to_user = dbas.console_scripts:demote_user
      setup_decidotron = dbas.database.initializedb:init_budget_discussion
      """,
      )

from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='csv2opds',
      version=version,
      description="csv2opds generates OPDS Catalogs from a CSV template",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='csv opds',
      author='Keith Fahlgren',
      author_email='keith@threepress.org',
      url='http://code.google.com/p/opds-tools/',
      license='New BSD License',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )

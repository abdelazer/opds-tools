from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='pragle',
      version=version,
      description="Pragle is a Python library for validating OPDS Catalogs",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='opds',
      author='Keith Fahlgren',
      author_email='keith@threepress.org',
      url='http://code.google.com/p/opds-tools/',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      package_data={
                    'pragle': ['schemas/*.*'],
      },
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'lxml >= 2.2',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )

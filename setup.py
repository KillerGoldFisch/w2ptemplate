from setuptools import setup, find_packages
import sys, os

version = '1.0'

setup(name='w2ptemplate',
      version=version,
      description="Standalone Web2Py template engine",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='Web2Py Template-engine',
      author='Kevin Gliewe',
      author_email='kevingliewe@gmail.com',
      url='https://gliewe.net/',
      license='',
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

from setuptools import setup, find_packages
import os

VERSION = '0.1-dev'

setup(name='seleniumcontext',
      version=VERSION,
      description="Utilities to create/run Selenium tests in multiple " \
                  "environments",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Testing",
        ],
      keywords='selenium test testrunner',
      author='Benoit Bryon',
      author_email='benoit@marmelune.net',
      url='https://github.com/benoitbryon/seleniumcontext/',
      license='BSD',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir = {'': 'src'},
      namespace_packages=[],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      entry_points="""
      """,
      )

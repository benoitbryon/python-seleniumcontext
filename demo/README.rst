#####################
Selenium context demo
#####################

This demo runs one selenium test in 2 browsers: firefox and chrome. Make sure
you installed them.

::

  cd demo
  python bootstrap.py -d
  bin/buildout
  bin/nosetests tests/bitbucket.py

.. note:
  you need chromium webdriver to be able to run chrome (at least on linux).

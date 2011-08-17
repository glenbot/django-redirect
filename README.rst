Django Redirects
================

A slightly more robust version of the native django redirect.

Installation
------------

1. Download the package http://github.com/glenbot/django-redirect
2. Run "python setup.py install"
3. Add the following line to your INSTALLED_APPS::

  INSTALLED_APPS = (
      ...
      'redirect'
  )

4. Add the following lines to your middleware::

  MIDDLEWARE_CLASSES = (
      ...
      'redirect.middleware.RedirectMiddleware'
  )

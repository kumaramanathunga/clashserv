#!/usr/bin/python
import sys
sys.path[0:0] = [
  '/Users/hanxu/Documents/hanbox/clashserv',
    '/Users/hanxu/Documents/hanbox/clashserv/eggs/isotoma.recipe.django-3.1.5-py2.7.egg',
    '/Users/hanxu/Documents/hanbox/clashserv/eggs/Django-1.4.1-py2.7.egg',
    '/Users/hanxu/Documents/hanbox/clashserv/eggs/zc.recipe.egg-1.3.2-py2.7.egg',
    '/Users/hanxu/Documents/hanbox/clashserv/eggs/zc.buildout-1.6.3-py2.7.egg',
    '/Users/hanxu/Documents/hanbox/clashserv/eggs/pytz-2012c-py2.7.egg',
    '/Users/hanxu/Documents/hanbox/clashserv/eggs/django_extensions-0.8-py2.7.egg',
    '/Users/hanxu/Documents/hanbox/clashserv/eggs/South-0.7.4-py2.7.egg',
    '/Users/hanxu/Documents/hanbox/clashserv/eggs/boto-2.3.0-py2.7.egg',
    '/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python',
    '/Users/hanxu/Documents/hanbox/clashserv/src/project',
    '/Users/hanxu/Documents/hanbox/clashserv/shared_apps',
    '/Users/hanxu/Documents/hanbox/clashserv/apps',
    '/Users/hanxu/Documents/hanbox/clashserv/external_apps',
  ]

import project.local_settings as settings

import isotoma.recipe.django.wsgi

application = isotoma.recipe.django.wsgi.main(settings)
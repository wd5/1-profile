"""
A set of request processors that return dictionaries to be merged into a
template context. Each function takes the request object as its only parameter
and returns a dictionary to add to the context.

These are referenced from the setting TEMPLATE_CONTEXT_PROCESSORS and used by
RequestContext.
"""

from django.conf import settings
from django.middleware.csrf import get_token
from django.utils.functional import lazy

def auth(request):
    """
    DEPRECATED. This context processor is the old location, and has been moved
    to `django.contrib.auth.context_processors`.

    This function still exists for backwards-compatibility; it will be removed
    in Django 1.4.
    """
    import warnings
    warnings.warn(
        "The context processor at `django.core.context_processors.auth` is " \
        "deprecated; use the path `django.contrib.auth.context_processors.auth` " \
        "instead.",
        DeprecationWarning
    )
    #from django.contrib.auth.context_processors import auth as auth_context_processor
    return {}#auth_context_processor(request)

def csrf(request):
    """
    Context processor that provides a CSRF token, or the string 'NOTPROVIDED' if
    it has not been provided by either a view decorator or the middleware
    """
    def _get_val():
        token = get_token(request)
        if token is None:
            # In order to be able to provide debugging info in the
            # case of misconfiguration, we use a sentinel value
            # instead of returning an empty dict.
            return 'NOTPROVIDED'
        else:
            return token
    _get_val = lazy(_get_val, str)

    return {'csrf_token': _get_val() }

def debug(request):
    "Returns context variables helpful for debugging."
    context_extras = {}
    if settings.DEBUG and request.META.get('REMOTE_ADDR') in settings.INTERNAL_IPS:
        context_extras['debug'] = True
        from django.db import connection
        context_extras['sql_queries'] = connection.queries
    return context_extras

def i18n(request):
    from django.utils import translation

    context_extras = {}
    context_extras['LANGUAGES'] = settings.LANGUAGES
    context_extras['LANGUAGE_CODE'] = translation.get_language()
    context_extras['LANGUAGE_BIDI'] = translation.get_language_bidi()

    return context_extras

def static(request):
    """
    Adds static-related context variables to the context.

    """
    return {'STATIC_URL': settings.STATIC_URL}

def media(request):
    """
    Adds media-related context variables to the context.

    """
    return {'MEDIA_URL': settings.MEDIA_URL}

def request(request):
    return {'request': request}

# PermWrapper and PermLookupDict proxy the permissions system into objects that
# the template system can understand. They once lived here -- they have
# been moved to django.contrib.auth.context_processors.

#from django.contrib.auth.context_processors import PermLookupDict as RealPermLookupDict
#from django.contrib.auth.context_processors import PermWrapper as RealPermWrapper

## class PermLookupDict(RealPermLookupDict):
##     def __init__(self, *args, **kwargs):
##         import warnings
##         warnings.warn(
##             "`django.core.context_processors.PermLookupDict` is " \
##             "deprecated; use `django.contrib.auth.context_processors.PermLookupDict` " \
##             "instead.",
##             PendingDeprecationWarning
##         )
##         super(PermLookupDict, self).__init__(*args, **kwargs)

## class PermWrapper(RealPermWrapper):
##     def __init__(self, *args, **kwargs):
##         import warnings
##         warnings.warn(
##             "`django.core.context_processors.PermWrapper` is " \
##             "deprecated; use `django.contrib.auth.context_processors.PermWrapper` " \
##             "instead.",
##             PendingDeprecationWarning
##         )
##         super(PermWrapper, self).__init__(*args, **kwargs)

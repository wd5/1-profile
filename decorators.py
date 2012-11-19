from django.http import HttpResponseRedirect
from google.appengine.api import users


def check_user(original_function):
    def new_function(*args, **kwargs):
        user = users.get_current_user()
        if user:
            if user.email().lower()=='barauskasalex@gmail.com':
                return original_function(*args, **kwargs)
        return HttpResponseRedirect(users.create_login_url(args[0].META.get('PATH_INFO','/edie/')))
    return new_function

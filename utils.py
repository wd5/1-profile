from google.appengine.api import users


def get_user_name():
    user = users.get_current_user()
    return user.nickname()

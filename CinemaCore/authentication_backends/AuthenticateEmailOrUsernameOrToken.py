from django.contrib.auth.backends import ModelBackend
# from django.core.exceptions import DoesNotExist
from CinemaCore.models import User, Employee, Client
from django.db.models import Q


class SettingsBackend(ModelBackend):
    """
    Authenticate against the settings ADMIN_LOGIN and ADMIN_PASSWORD.

    Use the login name and a hash of the password. For example:

    ADMIN_LOGIN = 'admin'
    ADMIN_PASSWORD = 'pbkdf2_sha256$30000$Vo0VlMnkR4Bk$qEvtdyZRWTcOsCnI/oQ7fVOu1XAURIZYoOZ3iq8Dr4M='
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(email=username))
        except User.DoesNotExist:
            return None
        try:
            user = user.client
        except Client.DoesNotExist:
            try:
                user = user.employee
            except Employee.DoesNotExist:
                pass
        return user if user.check_password(password) else None
        # user = User.objects.get(Q(username=username) | Q(email=username))
        # if user:
        #     try:
        #         user = user.cashier
        #     except Cashier.DoesNotExist:
        #         pass
        # return user if user and not user.deleted else None

    # def authenticate(self, request, username=None, password=None,  **kwargs):
    #     # login_valid = (settings.ADMIN_LOGIN == username)
    #     # pwd_valid = check_password(password, settings.ADMIN_PASSWORD)
    #     if login_valid and pwd_valid:
    #         try:
    #             # user = User.objects.get(username=username)
    #             user = User.objects.get(Q(username=username) | Q(email=username))
    #         except User.DoesNotExist:
    #             # Create a new user. There's no need to set a password
    #             # because only the password from settings.py is checked.
    #             # user = User(username=username)
    #             # user.is_staff = True
    #             # user.is_superuser = True
    #             # user.save()
    #             return None
    #         return user
    #     return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

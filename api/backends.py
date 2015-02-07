__author__ = 'Greg Ziegan'
from .models import User


class PhoneAuthBackend(object):

    def authenticate(self, phone, password):
        try:
            user = User.objects.get(phone=phone)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, phone):
        user = User.objects.get(phone=phone)
        if user.is_active:
            return user
        return None

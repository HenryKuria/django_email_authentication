from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


# Authenticate user using email and password
class EmailAuthenticationBackend(ModelBackend):

    def authenticate(self, request, email=None, password=None, **kwargs):
        UserModel = get_user_model()

        if email is None or password is None:
            return
        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            UserModel().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user

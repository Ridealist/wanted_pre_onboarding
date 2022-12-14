from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = None
    last_name = None

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"
        abstract = False

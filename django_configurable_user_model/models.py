from .meta import AbstractConfigurableUser
from django.contrib.auth.models import AbstractUser


class ConfigurableUser(AbstractConfigurableUser):

    class Meta(AbstractConfigurableUser.Meta):
        # db_table = 'auth_user'
        verbose_name = "User"
        verbose_name_plural = "User's"

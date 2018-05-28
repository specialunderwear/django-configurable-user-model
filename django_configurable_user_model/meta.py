import json

from django.db.models.base import ModelBase
from django.db.models.fields import __all__ as fieldnames
from django.contrib.auth.models import AbstractUser


import django.db.models.fields as fields

field_mapping = {
    str(fieldname).lower():getattr(fields, fieldname) for fieldname in fieldnames
}


class ConfigurableUserMetaClass(ModelBase):
    def __new__(cls, name, bases, attrs):
        path = attrs.pop('path', 'config.json')
        try:
            extrafields = {}
            with open(path) as config_file:
                loaded_attrs = json.load(config_file)
                userfields = loaded_attrs['userfields'].items()
                for field_name, field_props in userfields:
                    field_type = field_props.pop('type', 'charfield')
                    extrafields[str(field_name)] = field_mapping[field_type](**field_props)
            extrafields['extra_fields_set'] = extrafields.keys()
            attrs.update(extrafields)
        except IOError:
            pass
        except Exception as e:
            raise

        return ModelBase.__new__(cls, name, bases, attrs)


class AbstractConfigurableUser(AbstractUser):
    __metaclass__ = ConfigurableUserMetaClass

    class Meta(AbstractUser.Meta):
        db_table = 'auth_user'
        abstract = True

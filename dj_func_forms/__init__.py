from django.forms import BaseForm, Field
from django.forms import fields
from django.forms.widgets import MediaDefiningClass

import inspect


def field_for_type(type):
    if type == int:
        return fields.IntegerField()
    if type == bool:
        return fields.BooleanField()


def field_for_param(param):
    if param.annotation == inspect.Signature.empty:
        return fields.CharField()
    elif isinstance(param.annotation, Field):
        return param.annotation
    elif isinstance(param.annotation, type):
        return field_for_type(param.annotation)

    return CharField()


class FuncForm(BaseForm):
    def __init_subclass__(cls):
        params = inspect.signature(cls.function).parameters.values()
        cls.base_fields = cls.declared_fields = []
        for param in params:
            field = field_for_param(param)
            cls.base_fields.append(field)
            setattr(cls, param.name, field)

    def return_value(self):
        return self.function.__func__(**self.cleaned_data)

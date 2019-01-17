from django.forms import BaseForm, Field
from django.forms import fields
from django.forms.widgets import MediaDefiningClass
from collections import OrderedDict

import inspect


def field_for_type(type):
    if type == int:
        return fields.IntegerField()
    elif type == bool:
        return fields.BooleanField()
    elif type == str:
        return fields.CharField()


def field_for_param(param):
    if param.annotation == inspect.Signature.empty:
        return fields.CharField()
    elif isinstance(param.annotation, Field):
        return param.annotation
    elif isinstance(param.annotation, type):
        return field_for_type(param.annotation)

    return CharField()


class FuncForm(BaseForm):
    '''FuncForm allows you to specify a function as a class attribute,
    and it will infer fields from the function parameters.

    If the parameter:
        - doesn't have an annotation, it will infer CharField.
        - has a Field as an annotation, the annotation field will be used.
        - has a simple builtin type as an annotation,
          it will infer the simple corresponding field
              int -> IntegerField
              bool -> BooleanField
              etc...
    '''

    def __init_subclass__(cls):
        params = inspect.signature(cls.function).parameters.values()
        cls.base_fields = cls.declared_fields = OrderedDict()
        for param in params:
            field = field_for_param(param)
            cls.base_fields[param.name] = field
            setattr(cls, param.name, field)

    def return_value(self):
        return self.function.__func__(**self.cleaned_data)

from django.forms import BaseForm, CharField, Field, IntegerField
from django.forms.widgets import MediaDefiningClass

import inspect


def field_for_type(type):
    if type == int:
        return IntegerField()


def field_for_arg(arg):
    if isinstance(arg.annotation, Field):
        return arg.annotation
    elif isinstance(arg.annotation, type):
        return field_for_type(arg.annotation)

    return CharField()


def fields_for_function_args(function):
    args = inspect.signature(function).parameters.values()
    return {arg.name: field_for_arg(arg) for arg in args}


class FuncForm(BaseForm):
    def __init_subclass__(cls):
        arg_fields = fields_for_function_args(cls.function)
        cls.base_fields = cls.declared_fields = arg_fields

    def return_value(self):
        return self.function.__func__(**self.cleaned_data)

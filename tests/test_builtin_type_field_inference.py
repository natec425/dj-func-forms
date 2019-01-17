from django.forms import fields
from dj_func_forms import field_for_type

def test_int_returns_IntegerField():
    assert isinstance(field_for_type(int), fields.IntegerField)

def test_bool_returns_BooleanField():
    assert isinstance(field_for_type(bool), fields.BooleanField)
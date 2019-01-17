from django.forms import fields
from dj_func_forms import field_for_type
from datetime import date, datetime

def test_int_returns_IntegerField():
    assert isinstance(field_for_type(int), fields.IntegerField)

def test_bool_returns_BooleanField():
    assert isinstance(field_for_type(bool), fields.BooleanField)

def test_str_returns_CharField():
    assert isinstance(field_for_type(str), fields.CharField)

def test_float_returns_FloatField():
    assert isinstance(field_for_type(float), fields.FloatField)

def test_date_returns_DateField():
    assert isinstance(field_for_type(date), fields.DateField)
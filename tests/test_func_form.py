from dj_func_forms import FuncForm
from django.forms import CharField, IntegerField
from django.conf import settings


def test_FuncForm_generates_CharField_for_params_without_annotations():
    def add(x, y):
        return x + y

    class AddForm(FuncForm):
        function = add

    assert isinstance(AddForm.x, CharField)
    assert isinstance(AddForm.y, CharField)


def test_FuncForm_will_use_Field_parameter_annotations():
    def add(x: IntegerField(), y: IntegerField()):
        return x + y

    class AddForm(FuncForm):
        function = add

    assert isinstance(AddForm.x, IntegerField)
    assert isinstance(AddForm.y, IntegerField)

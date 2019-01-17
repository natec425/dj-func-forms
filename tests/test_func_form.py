from dj_func_forms import FuncForm
from django.forms import CharField, IntegerField, BooleanField
from django.conf import settings

# This is needed to allow Form instances to be created.
# I was getting exceptions for django not being configured.
settings.configure(USE_I18N=False)


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


def test_FuncForm_infers_field_for_python_builtin_types():
    def add(x: int, y: bool):
        return x + y

    class AddForm(FuncForm):
        function = add

    assert isinstance(AddForm.x, IntegerField)
    assert isinstance(AddForm.y, BooleanField)

def test_a_valid_FuncForm_exposes_a_return_value_method():
    def add(x: int, y: int):
        return x + y

    class AddForm(FuncForm):
        function = add

    form = AddForm({'x': '3', 'y': '12'})
    form.is_valid()
    assert form.return_value() == 15


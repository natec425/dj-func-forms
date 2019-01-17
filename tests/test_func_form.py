from dj_func_forms import FuncForm
from django.forms import CharField
from django.conf import settings


def test_FuncForm_generates_CharField_for_params_without_annotations():
    def add(x, y):
        return x + y

    class AddForm(FuncForm):
        function = add

    assert isinstance(AddForm.x, CharField)
    assert isinstance(AddForm.y, CharField)

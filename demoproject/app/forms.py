from func_forms import FuncForm


def add(x: int, y: int):
    return x + y


class AddForm(FuncForm):
    function = add


form = AddForm({'x': 2, 'y': 7})
form.is_valid()
print(form.return_value())

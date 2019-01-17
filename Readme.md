# dj_func_forms

`FuncForm` allows you to specify a function as a class attribute,
    and it will infer fields from the function parameters.

If the parameter:

- doesn't have an annotation, it will infer CharField.
- has a Field as an annotation, the annotation field will be used.
- has a simple builtin type as an annotation,
  it will infer the simple corresponding field
      int -> IntegerField
      bool -> BooleanField
      etc...
      
For example

```python
from django.forms import IntegerField
from dj_func_forms import FuncForm

def add(x: int, y: IntegerField()):
    return x + y
    
class AddForm(FuncForm):
    function = add
```

would produce a form with two fields `x`, and `y`. Both fields would
be `IntegerField`s.

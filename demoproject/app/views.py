from django.views.generic import FormView

from .forms import AddForm


# Create your views here.
class AddView(FormView):
    form_class = AddForm

from django.views.generic import ListView
from .models import UserPersona

class UserPersonaListView(ListView):
    model = UserPersona
    template_name = 'userpersona_list.html'  # Template to render the list
    context_object_name = 'personas'  # Name of the variable in the template
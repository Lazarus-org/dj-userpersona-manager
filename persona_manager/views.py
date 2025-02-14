from django.views.generic import ListView

from .models import UserPersona


class UserPersonaListView(ListView):
    model = UserPersona
    template_name = "userpersona_list.html"  # Template to render the list
    context_object_name = "personas"  # Name of the variable in the template

    def get_queryset(self):
        """Optionally filter the queryset based on query parameters."""
        queryset = super().get_queryset()

        # Filter by active status (optional)
        is_active = self.request.GET.get("is_active", None)
        if is_active in ["true", "false"]:
            queryset = queryset.filter(is_active=is_active == "true")

        return queryset

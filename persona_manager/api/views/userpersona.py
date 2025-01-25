from rest_framework import mixins, viewsets
from persona_manager.models import UserPersona
from persona_manager.api.serializers.userpersona import UserPersonaSerializer

class UserPersonaListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    A viewset for listing UserPersona instances.
    """
    queryset = UserPersona.objects.all()  # Default queryset
    serializer_class = UserPersonaSerializer  # Serializer for UserPersona

    def get_queryset(self):
        """
        Optionally filter the queryset based on query parameters.
        """
        queryset = super().get_queryset()

        # Filter by active status (optional)
        is_active = self.request.query_params.get('is_active', None)
        if is_active in ['true', 'false']:
            queryset = queryset.filter(is_active=is_active == 'true')

        # Search by persona name or description (optional)
        search_query = self.request.query_params.get('q', None)
        if search_query:
            queryset = queryset.filter(
                models.Q(persona_name__icontains=search_query) |
                models.Q(description__icontains=search_query)
            )

        # Ordering (optional)
        ordering = self.request.query_params.get('ordering', '-created_at')
        if ordering in ['created_at', '-created_at', 'persona_name', '-persona_name']:
            queryset = queryset.order_by(ordering)

        return queryset
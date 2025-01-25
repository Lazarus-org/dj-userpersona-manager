from django.urls import path, include
from rest_framework.routers import DefaultRouter
from persona_manager.api.views.userpersona import UserPersonaListViewSet

# Create a router and register the viewset
router = DefaultRouter()
router.register(r'user-personas', UserPersonaListViewSet, basename='userpersona')

urlpatterns = router.urls

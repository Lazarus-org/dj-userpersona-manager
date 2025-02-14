from django.contrib import admin
from django.urls import include, path

from persona_manager.views import UserPersonaListView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("personas/", UserPersonaListView.as_view(), name="user-persona-list"),
    path("api/", include("persona_manager.api.routers.main")),
]

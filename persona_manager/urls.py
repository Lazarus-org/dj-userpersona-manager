from django.urls import path
from .views import UserPersonaListView

urlpatterns = [
    path('personas/', UserPersonaListView.as_view(), name='userpersona-list'),
]


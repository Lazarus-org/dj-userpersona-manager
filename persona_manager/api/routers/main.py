from rest_framework.routers import DefaultRouter

from persona_manager.api.views.userpersona import UserPersonaViewSet

router = DefaultRouter()
router.register("userpersona", UserPersonaViewSet, basename="user-persona")

urlpatterns = router.urls

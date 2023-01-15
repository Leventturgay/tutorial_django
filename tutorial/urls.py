
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TutorialMVS

router = DefaultRouter()
router.register(r'tutorials', TutorialMVS)

urlpatterns = router.urls

# urlpatterns = [
#     path()
# ]

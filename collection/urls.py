from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ShirtViewSet, PantViewSet, ShoeViewSet

router = DefaultRouter()
router.register(r'shirts', ShirtViewSet)
router.register(r'pants', PantViewSet)
router.register(r'shoes', ShoeViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

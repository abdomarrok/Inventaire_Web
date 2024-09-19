from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet, CategoryViewSet, ServiceViewSet, LocationViewSet, EmployerViewSet, UserViewSet, InventaireItemViewSet

router = DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'employers', EmployerViewSet)
router.register(r'users', UserViewSet)
router.register(r'inventaire-items', InventaireItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
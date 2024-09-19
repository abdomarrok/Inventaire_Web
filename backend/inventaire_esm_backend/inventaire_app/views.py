# inventaire_app/views.py
from rest_framework import viewsets
from .models import Article, Category, Service, Location, Employer, User, InventaireItem
from .serializers import ArticleSerializer, CategorySerializer, ServiceSerializer, LocationSerializer, EmployerSerializer, UserSerializer, InventaireItemSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class EmployerViewSet(viewsets.ModelViewSet):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class InventaireItemViewSet(viewsets.ModelViewSet):
    queryset = InventaireItem.objects.all()
    serializer_class = InventaireItemSerializer

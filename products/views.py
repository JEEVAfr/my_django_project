from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from .models import Category, Subcategory, Product
from .serializers import CategorySerializer, SubcategorySerializer, ProductSerializer

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id', 'category_name']
    search_fields = ['category_name']


class SubcategoryViewSet(viewsets.ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category'] 
    search_fields = ['sub_category_name']  


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(is_active=True) 
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category', 'sub_category'] 
    search_fields = ['product_name'] 


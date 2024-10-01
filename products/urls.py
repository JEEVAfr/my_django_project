from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products.views import CategoryViewSet, SubcategoryViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'subcategories', SubcategoryViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
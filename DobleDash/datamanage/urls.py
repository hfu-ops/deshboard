from django.urls import path
from datamanage import views
from django.urls import include

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.ProductListView.as_view(), name='products'),
    path('products/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('vendors/', views.VendorListView.as_view(), name='vendors'),
    path('vendors/<int:pk>', views.VendorDetailView.as_view(), name='vendor-detail'),
]


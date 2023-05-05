"""
URL configuration for ecommercesite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from orders import views
from orders.views import ProductListView, OrderCreateView, VehicleDetailView, OrderDetailView, OrderHistoryView
from accounts.views import LoginView, HomeView, logout_view

app_name = 'orders'

urlpatterns = [
    path('login/', LoginView.as_view(),name ='login'),
    path('logout/', logout_view, name='logout'),  
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('compare/', views.compare, name='compare'),
    path('vehicle_list/', ProductListView.as_view(), name='product_list'),
    path('vehicle/<int:pk>/', VehicleDetailView.as_view(), name='vehicle_details'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('create_order/', OrderCreateView.as_view(), name='create_order'),
    path('orders/order_history/', OrderHistoryView.as_view(), name='order_history'),

]

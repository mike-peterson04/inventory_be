"""inventory_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URL conf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.RequestHandler.as_view(), name='handle_request'),
    path('modify/<request_id>/', views.RequestApprover.as_view(), name='approve_request'),
    path('register/', views.UserCreate.as_view(), name='register_user'),
    path('employee/', views.EmployeeHandler.as_view(), name='handle_employee'),
    path('employee/<employee_id>/', views.EmployeeHandler.as_view(), name='handle_specific_employee'),
    path('initial/', views.EmployeeUnprotected.as_view(), name='unprotected_employee'),
    path('product/', views.ProductsHandler.as_view(), name='handle_product'),
    path('product/<product_id>/', views.ProductHandler.as_view(), name= 'individual_product'),
    path('products/<filter_type>/<filter_value>', views.ProductHandler.as_view(), name='bulk_product'),
    path('myproducts/<employee_id>/', views.EmployeeActions.as_view(), name='Employee_actions'),
    path('stock/<store_id>', views.StockHandler.as_view(), name='stock_handler'),
    path('store/<manager_id>', views.StoreHandler.as_view(), name='store_handler'),
    path('assign/<employee_id>/', views.AssignProduct.as_view(), name='product_assignment'),
    path('role/', views.RoleHandler.as_view(), name='role_handler')
]

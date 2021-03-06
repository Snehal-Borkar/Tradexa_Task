"""my_grocery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from users import views
from products import views as v1
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.log),
    path('', v1.show_product),
    path('loginuser/', views.handlelogin),
    path('loginuser/post/', views.post),
    path('update/post/<int:id>/', views.handleupdatepost,name="update_post"),
    path('product_details/<int:id>/', v1.product_details,name="product_details"),
]

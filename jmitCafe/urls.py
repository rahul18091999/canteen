"""jmitCafe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from rest_framework import routers
from itemdetails import views
from cartdetail.views import CartUpate
from django.conf import settings
from django.conf.urls.static import static  
router = routers.DefaultRouter()
router.register(r'itemdetail', views.ItemViewSet),
router.register('cartupdate',CartUpate),
router.register('itemimage',views.ImageView)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('admindetails.urls')),
    path('router/',include(router.urls)),
    path('userdetail/',include('userdetails.urls')),
    path('cartdetail/',include('cartdetail.urls'),),
    path('orderdetail/',include('orderdetails.urls'))
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
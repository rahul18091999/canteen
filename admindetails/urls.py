from django.urls import path
from .views import AdminAuthenticateList
urlpatterns = [
    
    path('',AdminAuthenticateList.as_view())
]

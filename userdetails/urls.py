from django.urls import path
from .views import RegUser
urlpatterns = [
    path(r'user',RegUser.as_view())
]

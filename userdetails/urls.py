from django.urls import path
from .views import RegUser,UserAuthentication
urlpatterns = [
    path(r'user',RegUser.as_view()),
    path('login/',UserAuthentication.as_view())
]

from django.urls import path
from .views import setcookie, getcookie, deletecookie

urlpatterns = [
    path('sc/', setcookie),
    path('gc/', getcookie),
    path('dc/', deletecookie)
]
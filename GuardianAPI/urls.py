from django.urls import path
from . import views

app_name='GuardianAPI'

urlpatterns = [
    path('search/', views.search, name='search'),
]

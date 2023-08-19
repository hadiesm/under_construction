from django.urls import path
from . import views

app_name = 'under_construction'

urlpatterns = [
    path('', views.main_page, name='banner')
]

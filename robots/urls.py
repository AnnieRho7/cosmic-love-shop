from django.urls import path
from . import views

app_name = 'robots'

urlpatterns = [
    path('', views.robots_txt, name='robots_txt'),
]
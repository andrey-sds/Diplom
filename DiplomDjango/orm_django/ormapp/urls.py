from django.urls import path
from .views import main, sign_up

app_name = 'ormapp'

urlpatterns = [
    path('', main, name='main'),
    path('sign/', sign_up, name='register'),
]

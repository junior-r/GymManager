from django.urls import path

from Apps.Home.views import index

app_name = 'Home'

urlpatterns = [
    path('', index, name='index'),
]

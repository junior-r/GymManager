from django.urls import path

from Apps.Users.views import check_available_field

app_name = 'Users'

urlpatterns = [
    path('check_available_field/', check_available_field, name='check_available_field'),
]

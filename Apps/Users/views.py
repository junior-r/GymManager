from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

from Apps.Users.models import CustomUser


def check_available_field(request):
    global unavailable_message, available_message, user
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if request.method == 'POST' and is_ajax:
        field = request.POST.get('field')
        field_indicator = request.POST.get('fieldIndicator')
        if field_indicator == 'username':
            user = CustomUser.objects.filter(username=field)
            available_message = 'Nombre de usuario disponible'
            unavailable_message = 'Nombre de usuario ya registrado'
        elif field_indicator == 'email':
            user = CustomUser.objects.filter(email=field)
            available_message = 'Correo electrónico disponible'
            unavailable_message = 'Correo electrónico ya registrado'
        elif field_indicator == 'identification':
            user = CustomUser.objects.filter(email=field)
            available_message = 'Número de identificación disponible'
            unavailable_message = 'Número de identificación ya registrado'

        if user.exists():
            data = {'available': False, 'message': unavailable_message}
        else:
            data = {'available': True, 'message': available_message}
        return JsonResponse(data)
    else:
        return redirect('account_signup')

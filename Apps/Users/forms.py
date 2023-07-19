from allauth.account.forms import SignupForm
from django import forms
from django.core.validators import FileExtensionValidator
from django_countries.fields import CountryField
from Apps.Users.models import CustomUser

identification_type_options = [
    ('Pasaporte', 'Pasaporte'),
    ('Cédula', 'Cédula')
]

GENDER_OPTIONS = (
    ('M', 'Masculino'),
    ('F', 'Femenino'),
)


class CustomUserCreationForm(SignupForm):
    image = forms.ImageField(label='Foto de Perfil', required=False, widget=forms.FileInput(attrs={
        'accept': 'image/png, image/jpg, image/jpeg, image/webp',
    }), validators=[FileExtensionValidator(['png', 'jpg', 'jpeg', 'webp'])])
    email = forms.EmailField(label='Correo electrónico*', required=True, widget=forms.EmailInput(attrs={
        'placeholder': 'example@email.com',
    }))
    username = forms.CharField(label='Nombre de usuario*', required=True, widget=forms.TextInput(attrs={
        'placeholder': 'John123',
    }))
    first_name = forms.CharField(label='Nombres*', required=True, widget=forms.TextInput(attrs={
        'placeholder': 'John',
    }))
    last_name = forms.CharField(label='Apellidos*', required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Doe',
    }))
    password1 = forms.CharField(label='Contraseña*', required=True, widget=forms.PasswordInput(attrs={
        'placeholder': '**********',
    }))
    password2 = forms.CharField(label='Contraseña (de nuevo)*', required=True, widget=forms.PasswordInput(attrs={
        'placeholder': '**********',
    }))
    address = forms.CharField(label='Dirección matriz*', required=True, widget=forms.Textarea(attrs={
        'placeholder': '',
        'rows': 4,
    }))
    country = CountryField()
    phone = forms.CharField(label='Número de teléfono*', required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Número de teléfono',
    }))
    identification_number = forms.CharField(label='Número de Identificación', required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Número de identificación',
    }))
    identification_type = forms.ChoiceField(label='Tipo de Identificación', required=True, widget=forms.Select(attrs={

    }), choices=identification_type_options)
    gender = forms.ChoiceField(label='Género', required=True, widget=forms.Select(attrs={

    }), choices=GENDER_OPTIONS)
    birth_date = forms.DateField(label='Fecha de Nacimiento', required=True, widget=forms.DateInput(attrs={
        'type': 'text',
        'placeholder': 'Fecha de nacimiento (Día/Mes/Año)',
    }))

    def save(self, request):
        user = super().save(request)
        user.image = self.cleaned_data['image']
        user.save()
        return user

    class Meta:
        model = CustomUser
        fields = ['image', 'email', 'username', 'first_name', 'last_name', 'password1', 'password2', 'address',
                  'country', 'phone', 'identification_number', 'identification_type', 'gender', 'birth_date']


class DateInput(forms.DateInput):
    input_type = 'date'

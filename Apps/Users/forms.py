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

    }))
    username = forms.CharField(label='Nombre de usuario*', required=True, widget=forms.TextInput(attrs={

    }))
    first_name = forms.CharField(label='Nombres*', required=True, widget=forms.TextInput(attrs={

    }))
    last_name = forms.CharField(label='Apellidos*', required=True, widget=forms.TextInput(attrs={

    }))
    password1 = forms.CharField(label='Contraseña*', required=True, widget=forms.PasswordInput(attrs={

    }))
    password2 = forms.CharField(label='Contraseña (de nuevo)*', required=True, widget=forms.PasswordInput(attrs={

    }))
    address = forms.CharField(label='Dirección matriz*', required=True, widget=forms.Textarea(attrs={

    }))
    country = CountryField()
    phone = forms.CharField(label='Número de teléfono*', required=True, widget=forms.TextInput(attrs={

    }))
    identification = forms.CharField(label='Número de Identificación', required=True, widget=forms.TextInput(attrs={

    }))
    identification_type = forms.ChoiceField(label='Tipo de Identificación', required=True, widget=forms.Select(attrs={

    }), choices=identification_type_options)
    gender = forms.ChoiceField(label='Género', required=True, widget=forms.Select(attrs={

    }), choices=GENDER_OPTIONS)
    birth_date = forms.DateField(label='Fecha de Nacimiento', required=True, widget=forms.DateInput(attrs={

    }))

    class Meta:
        model = CustomUser
        fields = ['image', 'email', 'username', 'first_name', 'last_name', 'password1', 'password2', 'address',
                  'country', 'phone', 'identification', 'identification_type', 'gender', 'birth_date']


class DateInput(forms.DateInput):
    input_type = 'date'

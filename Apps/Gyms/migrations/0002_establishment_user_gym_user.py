# Generated by Django 4.2.3 on 2023-07-09 03:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Users', '0001_initial'),
        ('Gyms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='establishment',
            name='user',
            field=models.ForeignKey(default=None, limit_choices_to={'user_type': ['staff', 'manager']}, on_delete=django.db.models.deletion.CASCADE, related_name='user_gyms', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gym',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user_gyms', to='Users.manager'),
            preserve_default=False,
        ),
    ]
# Generated by Django 4.1.7 on 2023-04-04 13:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite1', '0003_chucvu1_user_groups_user_is_superuser_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employess',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]

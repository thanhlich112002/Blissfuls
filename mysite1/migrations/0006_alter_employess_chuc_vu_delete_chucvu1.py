# Generated by Django 4.1.7 on 2023-04-06 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite1', '0005_alter_employess_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employess',
            name='chuc_vu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nhan_viens', to='mysite1.chucvu'),
        ),
        migrations.DeleteModel(
            name='ChucVu1',
        ),
    ]

# Generated by Django 3.2.7 on 2021-12-27 11:52

from django.db import migrations, models
import django.db.models.deletion
from django.utils import timezone
from django.contrib.auth import get_user_model
import os



def create_superuser(apps, schema_editor):
    superuser = get_user_model()(
        is_active=True,
        is_superuser=True,
        is_staff=True,
        username=os.environ['ADMIN_USERNAME'],
        email=os.environ['ADMIN_EMAIL'],
        last_login=timezone.now(),
    )
    superuser.set_password(os.environ['ADMIN_PASSWORD'])
    superuser.save()


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
##        migrations.RunPython(create_superuser),
        migrations.CreateModel(
            name='UtilFields',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniqueId', models.CharField(blank=True, max_length=100, null=True)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FaClerkInformation',
            fields=[
                ('utilfields_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='faform.utilfields')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('dept_number', models.CharField(blank=True, max_length=3, null=True)),
                ('dept_name', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
            ],
            bases=('faform.utilfields',),
        ),
    ]

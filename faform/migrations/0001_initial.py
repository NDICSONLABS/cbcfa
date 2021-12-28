# Generated by Django 3.2.7 on 2021-12-27 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
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

# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-05 09:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ('first_name', 'last_name'),
            },
        ),
        migrations.CreateModel(
            name='UserAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserAttributeClassifier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(max_length=200, unique=True, verbose_name='Kind')),
                ('value_type', models.CharField(choices=[('int', 'Integer'), ('float', 'Float'), ('str', 'String'), ('bool', 'Boolean'), ('date', 'Date'), ('datetime', 'Date time')], max_length=20, verbose_name='Type of value')),
                ('value_validator', models.CharField(blank=True, help_text='Regex to validate value', max_length=500, null=True, verbose_name='Value validator')),
                ('only_one_required', models.BooleanField(default=False, verbose_name='only one of available labels is required')),
                ('category', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('category',),
            },
        ),
        migrations.CreateModel(
            name='UserAttributeClassifierLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=200, verbose_name='Label')),
                ('required', models.BooleanField(default=False, verbose_name='required')),
                ('slug', models.CharField(blank=True, max_length=100, null=True)),
                ('classifier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='labels', to='account.UserAttributeClassifier')),
            ],
            options={
                'ordering': ('label',),
            },
        ),
        migrations.AddField(
            model_name='userattribute',
            name='label',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='account.UserAttributeClassifierLabel'),
        ),
        migrations.AddField(
            model_name='userattribute',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attributes', to=settings.AUTH_USER_MODEL),
        ),
    ]
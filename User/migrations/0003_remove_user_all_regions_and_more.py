# Generated by Django 4.2.9 on 2024-02-06 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_delete_userregions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='all_regions',
        ),
        migrations.RemoveField(
            model_name='user',
            name='auth0_connection_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='auth0_user_id',
        ),
    ]

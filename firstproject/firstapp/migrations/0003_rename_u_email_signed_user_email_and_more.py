# Generated by Django 4.0 on 2022-01-02 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_signed_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signed_user',
            old_name='u_email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='signed_user',
            old_name='u_name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='signed_user',
            old_name='u_pass',
            new_name='Password',
        ),
    ]

# Generated by Django 4.2.11 on 2024-05-11 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_user_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='reset_password_expire',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='reset_password_token',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
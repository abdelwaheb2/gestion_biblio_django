# Generated by Django 4.2.2 on 2024-04-04 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borrowing', '0002_alter_borrowing_date_borrowing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowing',
            name='date_borrowing',
            field=models.DateTimeField(),
        ),
    ]

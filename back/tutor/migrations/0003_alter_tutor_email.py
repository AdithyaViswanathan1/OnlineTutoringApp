# Generated by Django 4.2.5 on 2023-10-27 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0002_alter_tutor_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]
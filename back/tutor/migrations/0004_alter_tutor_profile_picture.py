# Generated by Django 4.2.6 on 2023-11-10 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0003_remove_tutor_subject_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='profile_picture',
            field=models.FileField(blank=True, null=True, upload_to='media/', verbose_name='Profile Picture'),
        ),
    ]
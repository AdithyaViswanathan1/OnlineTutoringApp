# Generated by Django 4.2.6 on 2023-11-28 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0006_alter_tutor_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='total_hours',
            field=models.FloatField(blank=True, default=0.0, verbose_name='Total Hours Completed'),
        ),
    ]

# Generated by Django 4.2.6 on 2023-11-03 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='about_me',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='tutor',
            name='available',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='tutor',
            name='background_checked',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='tutor',
            name='hours',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='tutor',
            name='profile_picture',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='tutor',
            name='subject_list',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='total_hours',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
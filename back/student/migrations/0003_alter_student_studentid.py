# Generated by Django 4.2.5 on 2023-10-27 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_student_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='studentid',
            field=models.AutoField(db_column='studentID', editable=False, primary_key=True, serialize=False),
        ),
    ]
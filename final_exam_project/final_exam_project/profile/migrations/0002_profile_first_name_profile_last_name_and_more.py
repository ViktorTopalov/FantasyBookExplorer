# Generated by Django 5.0.3 on 2024-03-26 13:27

import django.core.validators
import final_exam_project.profile.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(help_text='Age requirement: 21 years and above.', validators=[django.core.validators.MinValueValidator(21)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(3, message='Username must be at least 3 chars long!'), final_exam_project.profile.validators.validate_username]),
        ),
    ]
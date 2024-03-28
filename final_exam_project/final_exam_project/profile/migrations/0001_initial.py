# Generated by Django 5.0.3 on 2024-03-25 13:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(3)])),
                ('email', models.EmailField(max_length=254)),
                ('age', models.PositiveIntegerField(help_text='Age requirement: 21 years and above.', validators=[django.core.validators.MinValueValidator(21)])),
                ('password', models.CharField(max_length=20)),
                ('profile_picture', models.URLField(blank=True, null=True)),
            ],
        ),
    ]

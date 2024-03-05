# Generated by Django 5.0 on 2024-03-05 10:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_person_bits_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blog.plans')),
            ],
        ),
    ]

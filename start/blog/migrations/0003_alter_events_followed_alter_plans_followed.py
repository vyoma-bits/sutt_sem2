# Generated by Django 5.0 on 2024-03-11 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_events_followed_plans_followed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='followed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='plans',
            name='followed',
            field=models.BooleanField(default=False),
        ),
    ]
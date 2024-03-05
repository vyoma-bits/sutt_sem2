# Generated by Django 5.0 on 2024-03-05 10:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_rename_expense_trip3_expense1_expense_description_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='expense1',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Trip_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.trip3')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Group',
        ),
    ]

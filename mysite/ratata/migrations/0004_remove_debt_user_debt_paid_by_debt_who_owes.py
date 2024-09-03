# Generated by Django 5.1 on 2024-08-29 14:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratata', '0003_debt'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='debt',
            name='user',
        ),
        migrations.AddField(
            model_name='debt',
            name='paid_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='paid_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='debt',
            name='who_owes',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='who_owes', to=settings.AUTH_USER_MODEL),
        ),
    ]
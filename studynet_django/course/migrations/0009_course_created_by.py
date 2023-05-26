# Generated by Django 4.0.4 on 2022-05-24 16:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0008_auto_20220427_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='courses', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.0.1 on 2022-01-18 12:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('steps', '0006_goals_user_steps_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goals',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
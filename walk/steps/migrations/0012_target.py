# Generated by Django 4.0.1 on 2022-01-19 15:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('steps', '0011_alter_steps_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='steps.goals')),
                ('step', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='steps.steps')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
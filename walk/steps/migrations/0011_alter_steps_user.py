# Generated by Django 4.0.1 on 2022-01-19 12:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('steps', '0010_alter_steps_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='steps',
            name='user',
            field=models.EmailField(default=django.utils.timezone.now, max_length=254),
            preserve_default=False,
        ),
    ]

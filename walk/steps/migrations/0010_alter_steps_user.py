# Generated by Django 4.0.1 on 2022-01-18 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steps', '0009_alter_steps_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='steps',
            name='user',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]

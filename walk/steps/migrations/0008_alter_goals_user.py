# Generated by Django 4.0.1 on 2022-01-18 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steps', '0007_alter_goals_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goals',
            name='user',
            field=models.EmailField(max_length=254),
        ),
    ]

# Generated by Django 4.0.1 on 2022-01-19 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steps', '0015_delete_steps_rename_step_target_steps_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='target',
            name='steps',
            field=models.IntegerField(default=0, null=True),
        ),
    ]

# Generated by Django 4.0.1 on 2022-01-20 15:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0006_remove_userprofile_goal'),
        ('steps', '0017_alter_target_goal_submitted'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailySteps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('steps', models.IntegerField(default=0, null=True)),
                ('date', models.DateTimeField(null=True, verbose_name='Date')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Goals',
        ),
        migrations.AlterField(
            model_name='target',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
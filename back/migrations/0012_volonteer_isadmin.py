# Generated by Django 2.2.1 on 2019-10-22 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0011_task_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='volonteer',
            name='isAdmin',
            field=models.BooleanField(default=False),
        ),
    ]

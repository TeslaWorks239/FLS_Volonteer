# Generated by Django 2.2.1 on 2019-10-22 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0010_auto_20191022_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='user_id',
            field=models.IntegerField(default=0),
        ),
    ]

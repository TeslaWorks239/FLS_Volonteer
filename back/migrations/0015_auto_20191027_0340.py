# Generated by Django 2.2.1 on 2019-10-27 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0014_auto_20191026_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='exp',
            field=models.IntegerField(default=0),
        ),
    ]

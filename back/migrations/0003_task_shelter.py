# Generated by Django 2.2.1 on 2019-10-21 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0002_auto_20191021_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='shelter',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
    ]

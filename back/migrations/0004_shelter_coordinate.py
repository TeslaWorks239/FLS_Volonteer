# Generated by Django 2.2.1 on 2019-10-21 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0003_task_shelter'),
    ]

    operations = [
        migrations.AddField(
            model_name='shelter',
            name='coordinate',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
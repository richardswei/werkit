# Generated by Django 3.0.4 on 2020-03-24 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
    ]

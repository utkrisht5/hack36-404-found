# Generated by Django 4.0.4 on 2022-04-23 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authority',
            name='field',
            field=models.TextField(default='All', null=True),
        ),
        migrations.AddField(
            model_name='complain',
            name='type',
            field=models.TextField(null=True),
        ),
    ]
# Generated by Django 4.0.4 on 2022-04-23 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_authority_field_complain_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='complain',
            name='scope',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='complain',
            name='type',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
# Generated by Django 2.0.7 on 2018-07-26 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfume', '0002_auto_20180725_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selectscent',
            name='scent',
            field=models.CharField(max_length=300),
        ),
    ]
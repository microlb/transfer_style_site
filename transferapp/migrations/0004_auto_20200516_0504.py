# Generated by Django 3.0.5 on 2020-05-16 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transferapp', '0003_imagepic_result_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageresult',
            name='result',
            field=models.CharField(max_length=100),
        ),
    ]

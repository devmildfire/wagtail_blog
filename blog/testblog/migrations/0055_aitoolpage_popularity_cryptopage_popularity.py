# Generated by Django 4.2.4 on 2023-08-05 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testblog', '0054_delete_tagssection'),
    ]

    operations = [
        migrations.AddField(
            model_name='aitoolpage',
            name='popularity',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='cryptopage',
            name='popularity',
            field=models.IntegerField(default=1),
        ),
    ]

# Generated by Django 4.2.3 on 2023-07-08 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testblog', '0009_alter_blogpagetag_content_object'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpage',
            name='tags',
        ),
        migrations.DeleteModel(
            name='BlogPageTag',
        ),
    ]
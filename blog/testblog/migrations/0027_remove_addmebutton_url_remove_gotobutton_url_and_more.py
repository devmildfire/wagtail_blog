# Generated by Django 4.2.3 on 2023-07-19 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testblog', '0026_addmebutton_gotobutton'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addmebutton',
            name='url',
        ),
        migrations.RemoveField(
            model_name='gotobutton',
            name='url',
        ),
        migrations.AddField(
            model_name='addmebutton',
            name='link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='gotobutton',
            name='link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
# Generated by Django 4.2.3 on 2023-07-19 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testblog', '0024_rename_footerlinks_navlinks'),
    ]

    operations = [
        migrations.AddField(
            model_name='footer',
            name='undertext',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='footer',
            name='text',
            field=models.CharField(max_length=400),
        ),
    ]

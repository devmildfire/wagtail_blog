# Generated by Django 4.2.3 on 2023-07-24 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_homepage_options_homepage_intro_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homepage',
            options={'verbose_name': 'Home Catalog Index Page', 'verbose_name_plural': 'Home Catalog Index Pages'},
        ),
    ]
# Generated by Django 4.2.3 on 2023-07-24 15:59

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_body'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homepage',
            options={'verbose_name': 'Catalog Index Page', 'verbose_name_plural': 'Catalog Index Pages'},
        ),
        migrations.AddField(
            model_name='homepage',
            name='intro',
            field=wagtail.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.RichTextField(blank=True, null=True),
        ),
    ]

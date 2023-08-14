# Generated by Django 4.2.4 on 2023-08-11 08:45

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('testblog', '0058_alter_cryptopage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cryptopage',
            name='content',
            field=wagtail.fields.StreamField([('text', wagtail.blocks.TextBlock())], default=[('text', 'hello world!')], use_json_field=True),
        ),
    ]
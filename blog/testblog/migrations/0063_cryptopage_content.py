# Generated by Django 4.2.4 on 2023-08-11 09:31

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('testblog', '0062_remove_cryptopage_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='cryptopage',
            name='content',
            field=wagtail.fields.StreamField([('text', wagtail.blocks.CharBlock(help_text='add a char block', required=True))], default=[('text', 'hello world!')], use_json_field=True),
        ),
    ]

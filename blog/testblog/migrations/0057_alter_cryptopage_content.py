# Generated by Django 4.2.4 on 2023-08-11 08:34

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('testblog', '0056_cryptopage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cryptopage',
            name='content',
            field=wagtail.fields.StreamField([('title_and_text', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(default='default title', help_text='Add your title', required=True)), ('text', wagtail.blocks.TextBlock(default='default text', help_text='Add your text', required=True))]))], default=[('title_and_text', {'text': 'Tang', 'title': 'Ting'}), ('title_and_text', {'text': 'Tang 2', 'title': 'Ting 2'})], use_json_field=True),
        ),
    ]

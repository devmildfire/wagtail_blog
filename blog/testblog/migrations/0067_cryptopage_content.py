# Generated by Django 4.2.4 on 2023-08-11 09:40

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('testblog', '0066_remove_cryptopage_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='cryptopage',
            name='content',
            field=wagtail.fields.StreamField([('title_and_text', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(default='default title', help_text='Add your title', required=True)), ('text', wagtail.blocks.TextBlock(default='default text', help_text='Add your text', required=True))]))], blank=True, default=[('title_and_text', {'text': 'Tang', 'title': 'Ting'}), ('title_and_text', {'text': 'Tang 2', 'title': 'Ting 2'})], null=True, use_json_field=True),
        ),
    ]

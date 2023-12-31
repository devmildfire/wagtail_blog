# Generated by Django 4.2.4 on 2023-08-11 14:10

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('testblog', '0077_remove_cryptopage_default_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cryptopage',
            name='content',
            field=wagtail.fields.StreamField([('TitleText', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(default='default title', help_text='Add your title', required=True)), ('text', wagtail.blocks.TextBlock(default='default text', help_text='Add your text', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(default=1, help_text='Add your Image', required=False))], help_text='add you char block', required=True))], blank=True, default=[('TitleText', {'image': 1, 'text': 'Here is the default text', 'title': 'Here is the default Title '}), ('TitleText', {'image': 2, 'text': 'Here is the default text', 'title': 'Here is the default Title'}), ('TitleText', {'image': 3, 'text': 'Here is the default text', 'title': 'Here is the default Title'}), ('TitleText', {'image': 4, 'text': 'Here is the default text', 'title': 'Here is the default Title'}), ('TitleText', {'image': 5, 'text': 'Here is the default text', 'title': 'Here is the default Title'})], null=True, use_json_field=True),
        ),
    ]

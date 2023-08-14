# Generated by Django 4.2.4 on 2023-08-12 18:38

from django.db import migrations
import wagtail.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('testblog', '0081_alter_cryptopage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cryptopage',
            name='content',
            field=wagtail.fields.StreamField([('TitleText', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(default='default title', help_text='Add your title', required=True)), ('text', wagtail.blocks.TextBlock(default='default text', help_text='Add your text', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(default=7, help_text='Add your Image', required=False))], help_text='add you char block', required=True)), ('GalleryBlock', wagtail.blocks.StructBlock([('mainImage', wagtail.images.blocks.ImageChooserBlock(default=7, help_text='Add your Main Image', required=True)), ('thumbNails', wagtail.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock(default=8, max_num=4)))], help_text='add you Gallery block', required=True)), ('ImageAndVideo', wagtail.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='Add your Image', required=False)), ('video', wagtail.embeds.blocks.EmbedBlock(help_text='Add your Video', required=False))], equired=False, help_text='add you images and videos to a block'))], blank=True, default=[('GalleryBlock', {'mainImage': 7, 'thumbNails': [8, 9, 10, 11]}), ('TitleText', {'image': 7, 'text': 'Here is the default text', 'title': 'Here is the default Title '}), ('TitleText', {'image': 8, 'text': 'Here is the default text', 'title': 'Here is the default Title'}), ('TitleText', {'image': 9, 'text': 'Here is the default text', 'title': 'Here is the default Title'}), ('TitleText', {'image': 10, 'text': 'Here is the default text', 'title': 'Here is the default Title'}), ('TitleText', {'image': 11, 'text': 'Here is the default text', 'title': 'Here is the default Title'})], null=True, use_json_field=True),
        ),
    ]
# Generated by Django 4.2.4 on 2023-08-13 10:42

from django.db import migrations
import wagtail.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('testblog', '0092_alter_cryptopage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cryptopage',
            name='content',
            field=wagtail.fields.StreamField([('ImageWithCaption', wagtail.blocks.StructBlock([('image_width', wagtail.blocks.ChoiceBlock(choices=[('50%', '50%'), ('60%', '60%'), ('70%', '70%'), ('80%', '80%'), ('90%', '90%'), ('100%', '100%')], help_text='Set image width in percent', icon='cogs')), ('image', wagtail.images.blocks.ImageChooserBlock(default=7, help_text='Add your Image', required=True)), ('caption', wagtail.blocks.TextBlock(default='default text', help_text='Add your caption', required=False))], help_text='add you char block', required=False)), ('ImageAndVideo', wagtail.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='Add your Image', required=False)), ('video', wagtail.embeds.blocks.EmbedBlock(help_text='Add your Video', required=False))], help_text='add you images and videos to a block', required=False)), ('RichText', wagtail.blocks.RichTextBlock(help_text='add you Rich Text block', required=False))], blank=True, default=[], null=True, use_json_field=True),
        ),
    ]

"""StreamFields live in here"""

from wagtail import blocks
# from wagtail.images.blocks import ImageChooserBlock
from wagtail.images import blocks as image_blocks
from wagtail.images.models import Image
from wagtail.embeds.blocks import EmbedBlock


class ImageWithCaptionBlock(blocks.StructBlock):
    """Image with optional caption text """

    default_block_image = Image.objects.all()[0]

    image_width = blocks.ChoiceBlock(choices=[
        ('50%', '50%'),
        ('60%', '60%'),
        ('70%', '70%'),
        ('80%', '80%'),
        ('90%', '90%'),
        ('100%', '100%'),
    ], icon='cogs', required=True, help_text='Set image width in percent', default='50%')

    image = image_blocks.ImageChooserBlock(
        required=True, help_text='Add your Image', default=default_block_image.id)
    caption = blocks.TextBlock(
        required=False, help_text='Add your caption', default='default text')

    class Meta:  # noqa
        template = "streams/image_and_caption_block.html"
        icon = "image"
        label = "Image & caption"


class ImageAndVideoBlock(blocks.StreamBlock):
    """Select an Image or a Video """
    image = image_blocks.ImageChooserBlock(
        required=False, help_text='Add your Image')
    video = EmbedBlock(required=False, help_text='Add your Video')

    class Meta:
        template = "streams/video_and_images_block.html"
        icon = 'media'
        label = "Images and Videos block"

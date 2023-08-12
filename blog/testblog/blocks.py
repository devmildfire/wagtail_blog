"""StreamFields live in here"""

from wagtail import blocks
# from wagtail.images.blocks import ImageChooserBlock
from wagtail.images import blocks as image_blocks
from wagtail.images.models import Image
from wagtail.embeds.blocks import EmbedBlock


class TitleAndTextBlock(blocks.StructBlock):
    """Title and Text and an image """

    default_block_image = Image.objects.all()[0]

    title = blocks.CharBlock(
        required=True, help_text='Add your title', default='default title')
    text = blocks.TextBlock(
        required=True, help_text='Add your text', default='default text')
    image = image_blocks.ImageChooserBlock(
        required=False, help_text='Add your Image', default=default_block_image.id)
    # required=True, help_text='Add your text', default=default_block_image)

    class Meta:  # noqa
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"


class GalleryBlock(blocks.StructBlock):
    """Main image and 4 preview thumbnails to switch to"""

    default_block_images = Image.objects.all().filter(
        title="The Default Image")

    imageIDs = []

    for image in default_block_images:
        imageIDs.append(image.id)

    mainImage = image_blocks.ImageChooserBlock(
        required=True, help_text='Add your Main Image', default=imageIDs[0])
    thumbNails = blocks.ListBlock(
        image_blocks.ImageChooserBlock(max_num=4, default=imageIDs[1]))

    class Meta:  # noqa
        template = "streams/gallery_block.html"
        icon = "image"
        label = "Gallery of Images"


class ImageAndVideoBlock(blocks.StreamBlock):
    """Select an Image or a Video """
    image = image_blocks.ImageChooserBlock(
        required=False, help_text='Add your Image')
    video = EmbedBlock(required=False, help_text='Add your Video')

    class Meta:
        template = "streams/video_and_images_block.html"
        icon = 'media'
        label = "Images and Videos block"

"""StreamFields live in here"""

from wagtail import blocks


class TitleAndTextBlock(blocks.StructBlock):
    """Title and Text and nothing else"""

    title = blocks.CharBlock(
        required=True, help_text='Add your title', default='default title')
    text = blocks.TextBlock(
        required=True, help_text='Add your text', default='default text')

    class Meta:  # noqa
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"

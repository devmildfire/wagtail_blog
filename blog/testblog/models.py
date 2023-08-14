from django.db import models
from django.shortcuts import render

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.models import ClusterableModel
from taggit.models import TaggedItemBase

from wagtail.models import Page
from wagtail.models import Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel

from wagtail.search import index

from wagtail.contrib.routable_page.models import RoutablePageMixin, route

from wagtail.snippets.models import register_snippet
from wagtail.fields import StreamField
from testblog import blocks

from wagtail.images.models import Image

from wagtail.blocks import RichTextBlock
from wagtail.admin.panels import PageChooserPanel


class NavLinks(Orderable):
    footer = ParentalKey(
        "Footer", related_name="footer_links", null=True, blank=True)
    header = ParentalKey(
        "Header", related_name="header_links", null=True, blank=True)
    hero_section = ParentalKey(
        "HeroSection", related_name="hero_links", null=True, blank=True)
    # footer_link = models.URLField(null=True, blank=True)
    link_name = models.CharField(max_length=255)
    link_text = models.CharField(max_length=255)
    link_image = models.ImageField(null=True, blank=True)

    panels = [
        FieldPanel('link_name'),
        FieldPanel('link_text'),
        FieldPanel('link_image'),
    ]


class FeatureCards(Orderable):
    AboutUs = ParentalKey(
        "AboutUs", related_name="feature_cards", null=True, blank=True)

    # footer_link = models.URLField(null=True, blank=True)
    card_name = models.CharField(max_length=255)
    card_text = models.CharField(max_length=255)
    card_link = models.CharField(max_length=255, null=True, blank=True)
    card_image = models.ImageField(null=True, blank=True)

    panels = [
        FieldPanel('card_name'),
        FieldPanel('card_text'),
        FieldPanel('card_link'),
        FieldPanel('card_image'),
    ]


@register_snippet
class CardsSection(ClusterableModel):
    title = models.CharField(max_length=255)

    panels = [
        FieldPanel('title'),
    ]

    def __str__(self):
        return self.title


@register_snippet
class OpenForAdWork(ClusterableModel):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255, null=True, blank=True)
    button_text = models.CharField(max_length=255, null=True, blank=True)
    button_link = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True)
    texture_image = models.ImageField(null=True, blank=True)

    panels = [
        FieldPanel('title'),
        FieldPanel('text'),
        FieldPanel('button_text'),
        FieldPanel('button_link'),
        FieldPanel('image'),
        FieldPanel('texture_image'),
    ]

    def __str__(self):
        return self.title


@register_snippet
class YourAdHere(ClusterableModel):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255, null=True, blank=True)
    link_text = models.CharField(max_length=255, null=True, blank=True)
    text = models.CharField(max_length=255)

    panels = [
        FieldPanel('title'),
        FieldPanel('link'),
        FieldPanel('link_text'),
        FieldPanel('text'),
    ]

    def __str__(self):
        return self.title


@register_snippet
class Footer(ClusterableModel):
    ToS_link = models.CharField(max_length=255, null=True, blank=True)
    PP_link = models.CharField(max_length=255, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    text = models.CharField(max_length=400)
    undertext = models.CharField(max_length=255, null=True, blank=True)

    panels = [
        FieldPanel('ToS_link'),
        FieldPanel('PP_link'),
        FieldPanel('url'),
        FieldPanel('text'),
        FieldPanel('undertext'),
        InlinePanel('footer_links'),
    ]

    def __str__(self):
        return self.text


@register_snippet
class AboutUs(ClusterableModel):
    title = models.CharField(max_length=255, null=True, blank=True)
    bigText = models.CharField(max_length=255, null=True, blank=True)
    subText = models.CharField(max_length=255, null=True, blank=True)

    panels = [
        FieldPanel('title'),
        FieldPanel('bigText'),
        FieldPanel('subText'),
        InlinePanel('feature_cards'),
    ]

    def __str__(self):
        return self.title

    class Meta:

        verbose_name = 'About Us section'
        verbose_name_plural = 'About Us sections'


@register_snippet
class Header(ClusterableModel):
    url = models.URLField(null=True, blank=True)
    text = models.CharField(max_length=255)

    panels = [
        FieldPanel('url'),
        FieldPanel('text'),
        InlinePanel('header_links'),
    ]

    def __str__(self):
        return self.text


@register_snippet
class AddMeButton(ClusterableModel):
    link = models.CharField(max_length=255, null=True, blank=True)
    text = models.CharField(max_length=255)

    panels = [
        FieldPanel('link'),
        FieldPanel('text'),
    ]

    def __str__(self):
        return self.text


@register_snippet
class GoToButton(ClusterableModel):
    link = models.CharField(max_length=255, null=True, blank=True)
    text = models.CharField(max_length=255)

    panels = [
        FieldPanel('link'),
        FieldPanel('text'),
    ]

    def __str__(self):
        return self.text


class AdsItems(Orderable):
    AdvertiseHere = ParentalKey(
        "AdvertiseHere", related_name="ads_items", null=True, blank=True)

    # footer_link = models.URLField(null=True, blank=True)
    item_name = models.CharField(max_length=255)
    item_link = models.CharField(max_length=255, null=True, blank=True)
    item_image = models.ImageField(null=True, blank=True)

    panels = [
        FieldPanel('item_name'),
        FieldPanel('item_link'),
        FieldPanel('item_image'),
    ]


@register_snippet
class AdvertiseHere(ClusterableModel):
    title = models.CharField(max_length=1024)
    main_text = models.CharField(max_length=1024)

    panels = [
        FieldPanel('title'),
        FieldPanel('main_text'),
        InlinePanel('ads_items'),
    ]

    def __str__(self):
        return self.title


@register_snippet
class HeroSection(ClusterableModel):
    blackText = models.CharField(max_length=1024)
    blueText = models.CharField(max_length=1024)
    subText = models.CharField(max_length=1024)

    panels = [
        FieldPanel('blackText'),
        FieldPanel('blueText'),
        FieldPanel('subText'),
        InlinePanel('hero_links'),
    ]

    def __str__(self):
        return self.blackText


class CryptoPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'CryptoPage',
        related_name='tagged_items',
        on_delete=models.CASCADE,
    )


class AIToolPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'AIToolPage',
        related_name='tagged_items',
        on_delete=models.CASCADE,
    )


class CryptoPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    path_string = "/crypto/"
    template = 'testblog/product_page.html'

    product_link = models.URLField(default='https://a-ads.com')

    defaultImages = Image.objects.all().filter(title="The Default Image")

    imageIDs = []

    for image in defaultImages:
        imageIDs.append(image.id)

    content = StreamField(
        [
            ("ImageWithCaption", blocks.ImageWithCaptionBlock(
                required=False, help_text='add you char block')),

            ("ImageAndVideo", blocks.ImageAndVideoBlock(
                required=False, help_text='add you images and videos to a block')),

            ("RichText", RichTextBlock(required=False,
             help_text='add you Rich Text block'))


        ],
        default=[
            # ("RichText", {"dfjasfsafsafsakfnsakfnlnf"})
            # ("ImageAndVideo",
            #  {"image": imageIDs[0]})
        ],
        use_json_field=True,
        null=True,
        blank=True,
    )

    popularity = models.IntegerField(default=1)

    preview_image = models.ImageField(blank=True, null=True)

    open_for_ads = models.BooleanField(blank=True, null=True)

    tags = ClusterTaggableManager(through=CryptoPageTag, blank=True)

    related_page_1 = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    related_page_2 = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    related_page_3 = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('product_link'),
        FieldPanel('tags'),
        PageChooserPanel('related_page_1', 'testblog.CryptoPage'),
        PageChooserPanel('related_page_2', 'testblog.CryptoPage'),
        PageChooserPanel('related_page_3', 'testblog.CryptoPage'),
        FieldPanel('popularity'),
        FieldPanel('open_for_ads'),
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body'),
        FieldPanel('content'),
        FieldPanel('preview_image'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField("body"),
        index.SearchField("intro"),
    ]

    class Meta:

        verbose_name = 'Crypto Product Page'
        verbose_name_plural = 'Crypto Product Pages'


class AIToolPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    path_string = "/ai-tools/"
    template = 'testblog/product_page.html'

    product_link = models.URLField(default='https://a-ads.com')

    defaultImages = Image.objects.all().filter(title="The Default Image")

    imageIDs = []

    for image in defaultImages:
        imageIDs.append(image.id)

    content = StreamField(
        [
            ("ImageWithCaption", blocks.ImageWithCaptionBlock(
                required=False, help_text='add you char block')),

            ("ImageAndVideo", blocks.ImageAndVideoBlock(
                required=False, help_text='add you images and videos to a block')),

            ("RichText", RichTextBlock(required=False,
             help_text='add you Rich Text block'))


        ],
        default=[
            # ("RichText", {"dfjasfsafsafsakfnsakfnlnf"})
            # ("ImageAndVideo",
            #  {"image": imageIDs[0]})
        ],
        use_json_field=True,
        null=True,
        blank=True,
    )

    popularity = models.IntegerField(default=1)

    preview_image = models.ImageField(blank=True, null=True)

    open_for_ads = models.BooleanField(blank=True, null=True, default=False)

    tags = ClusterTaggableManager(through=AIToolPageTag, blank=True)

    related_page_1 = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    related_page_2 = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    related_page_3 = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('product_link'),
        FieldPanel('tags'),
        PageChooserPanel('related_page_1', 'testblog.AIToolPage'),
        PageChooserPanel('related_page_2', 'testblog.AIToolPage'),
        PageChooserPanel('related_page_3', 'testblog.AIToolPage'),
        FieldPanel('popularity'),
        FieldPanel('open_for_ads'),
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body'),
        FieldPanel('content'),
        FieldPanel('preview_image'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField("body"),
        index.SearchField("intro"),
    ]

    class Meta:

        verbose_name = 'AI Tool Page'
        verbose_name_plural = 'AI Tools Pages'

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

    preview_image = models.ImageField(blank=True, null=True)

    tags = ClusterTaggableManager(through=CryptoPageTag, blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('tags'),
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body'),
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

    preview_image = models.ImageField(blank=True, null=True)

    tags = ClusterTaggableManager(through=AIToolPageTag, blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('tags'),
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body'),
        FieldPanel('preview_image'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField("body"),
        index.SearchField("intro"),
    ]

    class Meta:

        verbose_name = 'AI Tool Page'
        verbose_name_plural = 'AI Tools Pages'

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


# class CatalogIndexPage(RoutablePageMixin, Page):
#     intro = RichTextField(blank=True)

#     content_panels = Page.content_panels + [
#         FieldPanel('intro')
#     ]

#     def get_context(self, request, *args, **kwargs):
#         context = super().get_context(request, *args, **kwargs)
#         blogpages = CryptoPage.objects.live().order_by('-first_published_at')
#         Post_pages = CryptoPage.objects.child_of(self)

#         def listify(value):
#             return [tag.name for tag in value.all()]

#         tags = []

#         for post_page in Post_pages:
#             tags_list = listify(post_page.tags)
#             tags = tags + tags_list

#         tags = list(set(tags))

#         if request.GET.get('tag', None):
#             tag = request.GET.get('tag')
#             blogpages = blogpages.filter(tags__slug__in=[tag])

#         print('the blogpages are reset')
#         context['blogpages'] = blogpages
#         context['tags'] = tags
#         return context

#     @route(r'^search/$')
#     def post_search(self, request, *args, **kwargs):
#         context = self.get_context(request, *args, **kwargs)
#         context['a_special_test'] = 'Test of Routable Page for search'

#         search_query = request.GET.get('q', None)

#         self.posts = CryptoPage.objects.child_of(self)

#         if search_query:
#             self.posts = self.posts.search(search_query)

#         # context['blogpages'] = []
#         context['blogpages'] = self.posts
#         context['search_query'] = search_query

#         print('post_search method worked')
#         print(self.posts)

#         print('blogpages are equal to...')
#         print(context['blogpages'])

#         return render(request, "testblog/search.html", context)
#         # return self.render(request, context)

#     @route(r'^add-me/$')
#     def add_me(self, request, *args, **kwargs):
#         context = self.get_context(request, *args, **kwargs)
#         return render(request, "testblog/add-me.html", context)

#     @route(r'^crypto/$')
#     def crypto(self, request, *args, **kwargs):
#         context = self.get_context(request, *args, **kwargs)
#         return render(request, "testblog/crypto.html", context)

#     @route(r'^ai-tools/$')
#     def ai_tools(self, request, *args, **kwargs):
#         context = self.get_context(request, *args, **kwargs)
#         return render(request, "testblog/ai-tools.html", context)

#     class Meta:

#         verbose_name = 'Catalog Index Page'
#         verbose_name_plural = 'Catalog Index Pages'


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

        verbose_name = 'AI Tool Page'
        verbose_name_plural = 'AI Tools Pages'

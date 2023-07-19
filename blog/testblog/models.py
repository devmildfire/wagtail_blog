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
    # footer_link = models.URLField(null=True, blank=True)
    link_name = models.CharField(max_length=255)
    link_text = models.CharField(max_length=255)

    panels = [
        FieldPanel('link_name'),
        FieldPanel('link_text'),
    ]


@register_snippet
class Footer(ClusterableModel):
    url = models.URLField(null=True, blank=True)
    text = models.CharField(max_length=400)
    undertext = models.CharField(max_length=255, null=True, blank=True)

    panels = [
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


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE,
    )


class BlogIndexPage(RoutablePageMixin, Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        blogpages = BlogPage.objects.live().order_by('-first_published_at')
        Post_pages = BlogPage.objects.child_of(self)

        def listify(value):
            return [tag.name for tag in value.all()]

        tags = []

        for post_page in Post_pages:
            tags_list = listify(post_page.tags)
            tags = tags + tags_list

        tags = list(set(tags))

        if request.GET.get('tag', None):
            tag = request.GET.get('tag')
            blogpages = blogpages.filter(tags__slug__in=[tag])

        print('the blogpages are reset')
        context['blogpages'] = blogpages
        context['tags'] = tags
        return context

    @route(r'^search/$')
    def post_search(self, request, *args, **kwargs):
        context = self.get_context(request, *args, **kwargs)
        context['a_special_test'] = 'Test of Routable Page for search'

        search_query = request.GET.get('q', None)

        self.posts = BlogPage.objects.child_of(self)

        if search_query:
            self.posts = self.posts.search(search_query)

        # context['blogpages'] = []
        context['blogpages'] = self.posts
        context['search_query'] = search_query

        print('post_search method worked')
        print(self.posts)

        print('blogpages are equal to...')
        print(context['blogpages'])

        return render(request, "testblog/search.html", context)
        # return self.render(request, context)

    class Meta:

        verbose_name = 'Blog Index Page'
        verbose_name_plural = 'Blog Index Pages'


class BlogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('tags'),
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField("body"),
        index.SearchField("intro"),
    ]

    class Meta:

        verbose_name = 'Blog Page'
        verbose_name_plural = 'Blog Pages'
from django.db import models

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

from wagtail.search import index


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE,
    )


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]

    def get_context(self, request, *args, **kwargs):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request, *args, **kwargs)
        # blogpages = self.get_children().live().order_by('-first_published_at')
        blogpages = BlogPage.objects.live().order_by('-first_published_at')
        Post_pages = BlogPage.objects.child_of(self)

        def listify(value):
            return [tag.name for tag in value.all()]

        tags = []

        for post_page in Post_pages:
            # tags = post_page.tags.all
            tags_list = listify(post_page.tags)
            tags = tags + tags_list

        tags = list(set(tags))

        # print(type(tags))
        # print(tags)
        # print(type(tags_list))
        # print(tags_list)

        if request.GET.get('tag', None):
            tag = request.GET.get('tag')
            blogpages = blogpages.filter(tags__slug__in=[tag])
        context['blogpages'] = blogpages
        context['tags'] = tags
        return context


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

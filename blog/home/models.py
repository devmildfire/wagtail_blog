from django.db import models
from django.shortcuts import render
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from taggit.models import TaggedItemBase
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.fields import RichTextField
from wagtail.models import Orderable, Page
from wagtail.search import index
from wagtail.snippets.models import register_snippet
from testblog.models import *
import json
from django.http import JsonResponse
from random import randint


class HomePage(RoutablePageMixin, Page):
    intro = RichTextField(null=True, blank=True)
    body = RichTextField(null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('body'),
    ]

    # for AJAX post requests handling

    def serve(self, request, view=None, args=None, kwargs=None):
        if request.method == 'POST':
            data = json.loads(request.body)
            if 'number' in data:

                float_number = float(data['number'])

                return JsonResponse({'float': f'You got: {float_number}'})

        # if request.method == 'GET' and request.headers.get('X-Requested_With') == 'XMLHttpRequest':

        #     number = randint(1, 10)

        #     return JsonResponse({'number': number})

        return super().serve(request, view, args, kwargs)

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        blogpages = CryptoPage.objects.live().order_by('-first_published_at')
        aitoolspages = AIToolPage.objects.child_of(self)
        # aitoolspages = AIToolPage.objects
        # aitoolspages = AIToolPage.objects.live().order_by('-first_published_at')
        Post_pages = CryptoPage.objects.child_of(self)

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
        context['aitoolspages'] = aitoolspages
        context['tags'] = tags
        return context

    @route(r'^search/$')
    def post_search(self, request, *args, **kwargs):
        context = self.get_context(request, *args, **kwargs)
        self.title = "Search"
        context['a_special_test'] = 'Test of Routable Page for search'

        search_query = request.GET.get('q', None)

        self.posts = CryptoPage.objects.child_of(self)

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

    @route(r'^add-me/$')
    def add_me(self, request, *args, **kwargs):
        context = self.get_context(request, *args, **kwargs)
        self.title = "Add project to catalog"
        return render(request, "testblog/add-me.html", context)

    @route(r'^crypto/$')
    def crypto(self, request, *args, **kwargs):
        context = self.get_context(request, *args, **kwargs)
        self.title = "Crypto Services"
        # context['isPost'] = True

        # def serve(self, request, view=None, args=None, kwargs=None):
        if request.method == 'POST':
            context = self.get_context(request, *args, **kwargs)

            data = json.loads(request.body)

            if 'sortby' in data:

                sortby = (data['sortby'])

            print(data)
            sorted = 'the sorted answer string'
            
            context['blogpages'] = CryptoPage.objects.live().order_by(sortby)
            context['isPost'] = sortby

            print('returning POST page')
            print(context['blogpages'])
            print(context)
            return render(request, "testblog/crypto.html", context)
            
            # return JsonResponse({'sorted': f'You got: {sorted}'})

        if request.method == 'GET' and request.headers.get('X-Requested_With') == 'XMLHttpRequest':
            context['pages'] = CryptoPage.objects.live().order_by('title')
            context['isGet'] = True

            print('returning GET page')
            return render(request, "testblog/crypto.html", context)

        context['blogpages'] = CryptoPage.objects.live().order_by(
            '-first_published_at')
        context['isGet'] = False

        # return super().serve(request, view, args, kwargs)
        isPost = False
        print('returning regular page')
        return render(request, "testblog/crypto.html", context)

    @route(r'^ai-tools/$')
    def ai_tools(self, request, *args, **kwargs):
        context = self.get_context(request, *args, **kwargs)
        self.title = "AI Tools"
        return render(request, "testblog/ai-tools.html", context)

    class Meta:

        verbose_name = 'Home Catalog Index Page'
        verbose_name_plural = 'Home Catalog Index Pages'

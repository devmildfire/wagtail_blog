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
    # selectedTags = ArrayField

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('body'),
    ]

    # for AJAX post requests handling

    # def serve(self, request, view=None, args=None, kwargs=None):
    #     if request.method == 'POST':
    #         data = json.loads(request.body)
    #         if 'number' in data:

    #             float_number = float(data['number'])

    #             return JsonResponse({'float': f'You got: {float_number}'})

    #         if 'addTag' in data:

    #             tagToAdd = data['addTag']

    #             # if tagToAdd not in selectedTags

    #             return JsonResponse({'addedTag': f'You added a tag: {tagToAdd}'})

    #     return super().serve(request, view, args, kwargs)

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        blogpages = CryptoPage.objects.live().order_by('-first_published_at')
        aitoolspages = AIToolPage.objects.child_of(self)
        # aitoolspages = AIToolPage.objects
        # aitoolspages = AIToolPage.objects.live().order_by('-first_published_at')
        Post_pages = CryptoPage.objects.child_of(self)

        # selectedTags = []
        # context['selectedTags'] = selectedTags

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
            aitoolspages = aitoolspages.filter(tags__slug__in=[tag])

        print('the blogpages are reset')
        context['blogpages'] = blogpages
        context['aitoolspages'] = aitoolspages
        context['tags'] = tags
        return context

    def serve(self, request, view=None, args=None, kwargs=None):
        if request.method == 'POST':
            data = json.loads(request.body)
            if 'number' in data:

                float_number = float(data['number'])

                return JsonResponse({'float': f'You got: {float_number}'})

            # if 'addTag' in data:
            #     # context = self.get_context(request, *args, **kwargs)

            #     tagToAdd = data['addTag']

            #     selectedTags = context['selectedTags']
            #     print('cselectedTags...', selectedTags)
            #     if tagToAdd not in selectedTags:
            #         selectedTags.append(tagToAdd)
            #         context['added_tag'] = tagToAdd
            #         context['selectedTags'] = selectedTags
            #         print('context after adding a tag...', context)

            #         print('cselectedTags after adding...', selectedTags)

            #         return JsonResponse({'addedTag': f'You added a tag: {tagToAdd}'})

            #     return JsonResponse({'addedTag': f'Allready have a tag: {tagToAdd}'})

        return super().serve(request, view, args, kwargs)

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
        context['thispagesuffix'] = "crypto/"

        blogpages = CryptoPage.objects.live().order_by('-first_published_at')

        if request.GET.get('tag', None):
            tag = request.GET.get('tag')
            print("there is a tag present... ", tag)
            print("request full path is... ", request.get_full_path())
            context['presenttag'] = tag

        else:
            tag = None
            print("there is NO tag present... ", tag)
            print("request full path is... ", request.get_full_path())
            context['presenttag'] = 'trading'

        print("the old context is... ", context)
        # context['isPost'] = True

        # def serve(self, request, view=None, args=None, kwargs=None):
        if request.method == 'POST':
            # context = self.get_context(request, *args, **kwargs)
            print("the new context is... ", context)

            data = json.loads(request.body)

            if 'sortby' in data:

                sortby = (data['sortby'])

                # blogpages = CryptoPage.objects.live().order_by(sortby)
                blogpages = blogpages.order_by(sortby)

                print("the new request for POST is... ", request)
                print("the tag for POST is... ", tag)

                # if request.GET.get('tag', None):
                #     tag = request.GET.get('tag')
                tag = context['presenttag']

                if tag is not None:
                    print("the cards will be filtered by tag... ", tag)
                    blogpages = blogpages.filter(
                        tags__slug__in=[tag])

                context['blogpages'] = blogpages
                context['isPost'] = sortby

                return render(request, "testblog/crypto.html", context)

            if 'addTag' in data:
                # context = self.get_context(request, *args, **kwargs)

                tagToAdd = data['addTag']

                selectedTags = context['selectedTags']
                print('cselectedTags...', selectedTags)
                if tagToAdd not in selectedTags:
                    selectedTags.append(tagToAdd)
                    context['added_tag'] = tagToAdd
                    context['selectedTags'] = selectedTags
                    print('context after adding a tag...', context)

                    print('cselectedTags after adding...', selectedTags)

                    return JsonResponse({'addedTag': f'You added a tag: {tagToAdd}'})

                return JsonResponse({'addedTag': f'Allready have a tag: {tagToAdd}'})

            # return JsonResponse({'sorted': f'You got: {sorted}'})

        if request.method == 'GET' and request.headers.get('X-Requested_With') == 'XMLHttpRequest':
            context['pages'] = CryptoPage.objects.live().order_by('title')
            context['isGet'] = True

            print('returning GET page')
            return render(request, "testblog/crypto.html", context)

        # blogpages = CryptoPage.objects.live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        context['isGet'] = False

        if request.GET.get('tag', None):
            tag = request.GET.get('tag')
            blogpages = blogpages.filter(
                tags__slug__in=[tag])
            print("tag filtered pages are...", blogpages)
            context['blogpages'] = blogpages

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

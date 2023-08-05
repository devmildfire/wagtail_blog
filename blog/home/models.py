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

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        if 'selected_tags' in request.session:
            print('the session variable "selected_tags" is ALLREADY present...', request.session['selected_tags'])
        else:
            request.session['selected_tags'] = []
            print('the session variable "selected_tags" is set to...', request.session['selected_tags'])

        selected_tags = request.session['selected_tags']
        print('selected tags for Crypto page TagsList set to...', selected_tags)

        blogpages = CryptoPage.objects.live().order_by('-first_published_at')
        aitoolspages = AIToolPage.objects.child_of(self)
        # aitoolspages = AIToolPage.objects
        # aitoolspages = AIToolPage.objects.live().order_by('-first_published_at')
        Post_pages = CryptoPage.objects.child_of(self)

        def listify(value):
            return [tag.name for tag in value.all()]

        tags = []

        for post_page in blogpages:
            tags_list = listify(post_page.tags)
            tags = tags + tags_list

        tags = list(set(tags))
 
        print('the blogpages are reset')
        context['blogpages'] = blogpages
        context['aitoolspages'] = aitoolspages
        context['tags'] = tags
        context['selected_tags'] = selected_tags
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
        print("blogpages are RESET by CRYPTO... !!!", blogpages)

        def FilterCardsByTags(cardslist):
            # context = self.get_context(request, *args, **kwargs)
            """
                фкнция фильтрует набор карточек по набору тэгов этих карточек
            """
            if len(request.session['selected_tags']) == 0:
                print("there are NO TAGS to filter by... ", request.session['selected_tags'])
                return cardslist

            print("there are tags to filter by... ", request.session['selected_tags'])

            filterTags = [x.lower() for x in request.session['selected_tags']]
            
            print("the cards will be filtered by tag(s)... ", filterTags)

            for filterTag in filterTags:
                print("filtering Tag is... ", filterTag)
                cardslist = cardslist.filter(tags__slug__in=[filterTag])    
                print("the filtered Cardslist for this tag is... .... ....  ", cardslist)

            print("the new filtered Cards list is... ",  cardslist )
            
            return cardslist

        if request.method == 'POST':

            print("Detected POST method request")    
            data = json.loads(request.body)
            print("POST method data is...", data)    
            print("the new request for POST is... ", request)

            if 'sortby' in data:

                sortby = data['sortby']
                print("It is a sorting request. Sort by...", sortby) 
            
                blogpages = blogpages.order_by(sortby)

                blogpages = FilterCardsByTags(blogpages)

                context['blogpages'] = blogpages

                return render(request, "testblog/crypto.html", context)

            if 'addTag' in data:
                
                tagToAdd = data['addTag']
                print("It is a tag adding/removing request. ",) 

                print('tag to add...', tagToAdd)

                selectedTags = request.session['selected_tags']
                print('selected tags from session', request.session['selected_tags'])

                print('selectedTags...', selectedTags)

                if tagToAdd not in selectedTags:
                    selectedTags.append(tagToAdd)
                    print('selectedTags = ', selectedTags)
                    request.session['selected_tags'] = selectedTags
                    print('the session variable is set BY POST ADD TAG to...', request.session['selected_tags'])
                else :
                    taggToRemove = tagToAdd
                    selectedTags.remove(taggToRemove)
                    print('selectedTags = ', selectedTags)
                    request.session['selected_tags'] = selectedTags
                    print('the session variable is set BY POST REMOVE TAG to...', request.session['selected_tags'])

                context['blogpages'] = FilterCardsByTags(blogpages)
                context['selected_tags'] = selectedTags

                return render(request, "testblog/crypto.html", context)       

            if 'showAll' in data:
                
                # tagToAdd = data['addTag']
                print("It is a SHOW ALL tags request. ",) 

        

                selectedTags = request.session['selected_tags']
                print('selected tags from session', request.session['selected_tags'])

                print('selectedTags...', selectedTags)

                selectedTags = []
                print('selectedTags = ', selectedTags)
                request.session['selected_tags'] = selectedTags
                print('the session variable is set BY POST to...', request.session['selected_tags'])

               

                context['blogpages'] = FilterCardsByTags(blogpages)
                context['selected_tags'] = selectedTags

                return render(request, "testblog/crypto.html", context)    

        
        # context['blogpages'] = FilterCardsByTags(blogpages)

        print('regular GET page context is...', context)
        print('session variable for Selected Tags...', request.session['selected_tags'])

        context['selected_tags'] = request.session['selected_tags']
        context['blogpages'] = FilterCardsByTags(blogpages)

        print('regular GET page context AFTER FILTER is...', context)

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
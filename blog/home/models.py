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
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.utils.text import slugify

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




        if 'selected_sortBy' in request.session:
            print('the session variable "selected_sortBy" is ALLREADY present...', request.session['selected_sortBy'])
        else:
            request.session['selected_sortBy'] = '-popularity'
            print('the session variable "selected_sortBy" is set to...', request.session['selected_sortBy'])

        selected_sortBy = request.session['selected_sortBy']
        print('selected sorting field for Crypto page cards is set to...', selected_sortBy)

        
        
        if 'sortBy_OptionsList' in request.session:
            print('the session variable "sortBy_OptionsList" is ALLREADY present...', request.session['sortBy_OptionsList'])
        else:
            request.session['sortBy_OptionsList'] = [
                '-popularity',
                '-first_published_at',
                '-date',
                'title'
            ]
            print('the session variable "sortBy_OptionsList" is set to...', request.session['sortBy_OptionsList'])

        sortBy_OptionsList = request.session['sortBy_OptionsList']
        print('selected sorting order for SELECT is set to...', sortBy_OptionsList)


        optionsToTitlesDict = {
          "-popularity": "sort by popularity",
          "title": "sort by title",
          "-date": "sort by date",
          "-first_published_at": "sort by default"
        }




        blogpages = CryptoPage.objects.live().order_by(selected_sortBy)
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
 
        print('the context is reset')

        context['blogpages'] = blogpages
        context['aitoolspages'] = aitoolspages
        context['tags'] = tags
        context['selected_tags'] = selected_tags
        context['selected_sortBy'] = selected_sortBy
        context['sortBy_OptionsList'] = sortBy_OptionsList
        context['optionsToTitlesDict'] = optionsToTitlesDict

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
        # context['thispagesuffix'] = "crypto/"

        selected_sortBy = request.session['selected_sortBy']
        

        blogpages = CryptoPage.objects.live().order_by(selected_sortBy)
        print("blogpages are RESET by CRYPTO... !!!", blogpages)


        def FilterCardsByTags(cardslist):
            """
                фкнция фильтрует набор карточек по набору тэгов этих карточек
            """
            if len(request.session['selected_tags']) == 0:
                print("there are NO TAGS to filter by... ", request.session['selected_tags'])
                return cardslist

            print("there are tags to filter by... ", request.session['selected_tags'])

            # filterTags = [x.lower() for x in request.session['selected_tags']]
            filterTags = [slugify(x) for x in request.session['selected_tags']]
            
            print("the cards will be filtered by tag(s)... ", filterTags)

            for filterTag in filterTags:
                print("filtering Tag is... ", filterTag)
                cardslist = cardslist.filter(tags__slug__in=[filterTag])    
                print("the filtered Cardslist for this tag is... .... ....  ", cardslist)

            print("the new filtered Cards list is... ",  cardslist )
            
            return cardslist
        
        def ApplyPagination(ListToPaginate_String, num_per_page=5):
                
            print('starting Paginator')

            allItems = context[ListToPaginate_String]
            print('QuerySet to Paginate', allItems)

            num_per_page = num_per_page

            paginator = Paginator(allItems, num_per_page) # @todo change to 10 per page

            print('Paginator will show' , num_per_page, ' cards per page')

            page = request.GET.get("page", 1)
            page_range = paginator.get_elided_page_range(number=page, on_each_side=1, on_ends=1)
            print('Paginator page_range is ' , page_range)

            try: 
                cardsOnPage = paginator.page(page)
                print('Paginator worked regularly, cards for page are...', cardsOnPage)
            except PageNotAnInteger:
                cardsOnPage = paginator.page(1)
                print('Paginator got NOT AN INTEGER page number, cards for page are...', cardsOnPage)
            except EmptyPage:
                cardsOnPage = paginator.page(paginator.num_pages)
                print('Paginator got NOT AN EMPTY page number, cards for page are...', cardsOnPage)

            context[ListToPaginate_String] = cardsOnPage
            context['page_range'] = page_range
            print('New list of cards for this page is...', context[ListToPaginate_String])

            return None
        

        if request.method == 'POST':

            print("Detected POST method request")    
            data = json.loads(request.body)
            print("POST method data is...", data)    
            print("the new request for POST is... ", request)

            if 'sortby' in data:

                selected_sortBy = data['sortby']

               
                request.session['selected_sortBy'] = selected_sortBy


                sortBy_OptionsList = request.session['sortBy_OptionsList']
                sortBy_OptionsList.insert(0, sortBy_OptionsList.pop(sortBy_OptionsList.index(selected_sortBy)))
                request.session['sortBy_OptionsList'] = sortBy_OptionsList

                print("It is a sorting request. Sort by...", selected_sortBy) 
            
                blogpages = blogpages.order_by(selected_sortBy)

                blogpages = FilterCardsByTags(blogpages)

                context['blogpages'] = blogpages
                context['selected_sortBy'] = selected_sortBy

                ApplyPagination('blogpages', 2)

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

                ApplyPagination('blogpages', 2)

                return render(request, "testblog/crypto.html", context)       

            if 'showAll' in data:
                
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

                ApplyPagination('blogpages', 2)

                return render(request, "testblog/crypto.html", context)    

        print('regular GET page context is...', context)
        print('session variable for Selected Tags...', request.session['selected_tags'])

        context['selected_tags'] = request.session['selected_tags']
        context['blogpages'] = FilterCardsByTags(blogpages)

        ApplyPagination('blogpages', 2)

        print('regular GET page context AFTER FILTER and AFTER PAGINATION is...', context)

        print('returning regular PAGINATED page')
        return render(request, "testblog/crypto.html", context)

    @route(r'^ai-tools/$')
    def ai_tools(self, request, *args, **kwargs):
        context = self.get_context(request, *args, **kwargs)
        self.title = "AI Tools"
        return render(request, "testblog/ai-tools.html", context)

    class Meta:

        verbose_name = 'Home Catalog Index Page'
        verbose_name_plural = 'Home Catalog Index Pages'
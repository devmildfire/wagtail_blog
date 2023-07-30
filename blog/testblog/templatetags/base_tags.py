# from testblog.models import Footer, Header, AddMeButton, GoToButton, HeroSection, AboutUs, YourAdHere
from testblog.models import *
from home.models import HomePage
from django import template


register = template.Library()


@register.inclusion_tag("testblog/tags/OpenForAdWork.html", takes_context=True)
def open_for_ad_work_tag(context):

    return {
        'request': context['request'],
        'open_for_ad_work': OpenForAdWork.objects.first(),
    }


@register.inclusion_tag("testblog/tags/YourAdHere.html", takes_context=True)
def your_add_here_tag(context):

    return {
        'request': context['request'],
        'your_ad_here': YourAdHere.objects.first(),
    }


@register.inclusion_tag("testblog/tags/AboutUs.html", takes_context=True)
def about_us_tag(context):

    return {
        'request': context['request'],
        'about_us': AboutUs.objects.first(),
    }


@register.inclusion_tag("testblog/tags/footer.html", takes_context=True)
def footer_tag(context):

    return {
        'request': context['request'],
        'footer': Footer.objects.first(),
        'home_page': HomePage.objects.first(),
    }


@register.inclusion_tag("testblog/tags/header.html", takes_context=True)
def header_tag(context):

    return {
        'request': context['request'],
        'header': Header.objects.first(),
        'home_page': HomePage.objects.first(),
    }


@register.inclusion_tag("testblog/tags/AddMe.html", takes_context=True)
def AddMe_tag(context):

    return {
        'request': context['request'],
        'AddMe': AddMeButton.objects.first(),
        'home_page': HomePage.objects.first(),
    }


@register.inclusion_tag("testblog/tags/GoTo.html", takes_context=True)
def GoTo_tag(context):

    return {
        'request': context['request'],
        'GoTo': GoToButton.objects.first(),
    }


@register.inclusion_tag("testblog/tags/Hero.html", takes_context=True)
def Hero_tag(context):

    return {
        'request': context['request'],
        'Hero': HeroSection.objects.first(),
    }


@register.inclusion_tag("testblog/tags/Card.html", takes_context=True)
def Card_tag(context):

    return {
        'request': context['request'],
    }

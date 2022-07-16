from django.contrib import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.db.models import Count
from django.core.paginator import Paginator 
from django.db.models import Q
from django.http import JsonResponse
from django.conf import settings
from django.core.mail import send_mail

#home page index loading
def commondata():
    navigation_menu = NavigationMenu.objects.filter(status=True).all() 
    contacts = Contact.objects.get()
    social_media = SocialMedia.objects.filter(disable=False).all()
    bloginfo = Bloginfo.objects.get()
    footermenu = FooterMenu.objects.all()
    data = {
        "navigation":navigation_menu,
        "contacts":contacts,
        "socialmedia":social_media,
        "bloginfo":bloginfo,
        "footermenu":footermenu
    } 
    return data
def index(request):
    record = Recipe.objects.filter(premium=True).all().order_by('-id')
    recentpost = Recipe.objects.all().order_by('-id')[:5]
    posts = Recipe.objects.all()[:8]
    userinfo = User.objects.filter(is_superuser=True).all()[0]
    userid = userinfo.id
    userinfo = ProfileSettings.objects.select_related("user").get(id=userid)
    common  = commondata()
    ads = Ads.objects.order_by("?").first()
    categories = Recipe.objects.values("category").annotate(Count('category')).distinct()
    data = {
        "record":record,
        "recent_post":recentpost,
        "posts":posts,
        "categories":categories,
        "userinfo":userinfo,
        "ads":ads
    }
    data.update(common)
    return render(request,'frontend/index.html',data)

def singlepage(request,id):
    record = Recipe.objects.get(id=id)
    data = {
        "record" :record
    }
    data.update(commondata())
    return render(request,'frontend/singlepage.html',data)

def category(request,category):
    
    record = Recipe.objects.filter(category=category).all()
    book_paginator = Paginator(record,4)

    page_num = request.GET.get('page')
    
    page = book_paginator.get_page(page_num)

    context = {
        'count' : book_paginator.count,
        'records' : page
    }
    context.update(commondata())
    return render(request, 'frontend/category.html', context)

def aboutus(request):
    return render(request,'frontend/about.html')

def search(request):
    param = request.GET.get('q')
    if param:
        posts = Recipe.objects.filter(Q(title__icontains=param) | Q(description__icontains=param) | Q(category__icontains=param) )
        book_paginator = Paginator(posts,4)

        page_num = request.GET.get('page')
    
        page = book_paginator.get_page(page_num)

    context = {
        'count' : book_paginator.count,
        'records' : page,
         "query" :"/search?q={0}".format(param)
    }
    context.update(commondata())
    return render(request,'frontend/search.html',context)

def subscribe(request):
        email_id = request.POST.get("email_id")
        subscribe = Subscribe()
        subscribe.email = email_id
        subscribe.save()
        if(Subscribe.objects.latest('id').id>0):
            response = {'msg':'SubScribed' }
        else:
            response = {' msg':'Failed' }
        return JsonResponse(response)
        
def contact(request):
    data = commondata()
    return render(request,'frontend/contact.html',data)

def addquery(request):
   enquiry  = Enquiry()
   enquiry.name = request.POST.get("name")
   enquiry.email = request.POST.get("email")
   enquiry.subject = request.POST.get("subject")
   enquiry.phone = request.POST.get("phone")
   enquiry.message = request.POST.get("message")
   enquiry.save()
   response = redirect('/contact')
   messages.add_message(request,messages.SUCCESS,"Message Send")
   return(response)

def recipies(request):
    record = Recipe.objects.all()
    book_paginator = Paginator(record,6)

    page_num = request.GET.get('page')
    
    page = book_paginator.get_page(page_num)

    context = {
        'count' : book_paginator.count,
        'records' : page,
        "url":'/recipies'
    }
    context.update(commondata())
    return render(request,'frontend/recipies.html',context)
def sendemail(request):
    send_mail(
            subject="test",
            message="test",
            from_email="hithindevelopertester@gmail.com",
            recipient_list=["hithindeveloper@gmail.com"],
            fail_silently = False,
        )
   
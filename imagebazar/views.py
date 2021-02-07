from email.mime import image

from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import *


def show_about_page(request):
    print("about page request ")
    name = 'learncode with NIRMAL '
    link = 'https://www.youtube.com/watch?v=Bapkj53UJiQ'
    # this below dictionary use for to take the data to acess it to other file using the key name (name,
    # or link) which ever u want to use
    data = {
        'name': name,
        'link': link
    }
    return render(request, "about.html", data)


def show_home_page(request):
    cats = Category.objects.all()

    images = Image.objects.all()
    data = {'images': images, 'cats': cats}

    return render(request, "home.html", data)


def show_category_page(request, cid):
    print(cid)
    cats = Category.objects.all()

    cat = Category.objects.get(pk=cid)
    print(cat)

    images = Image.objects.filter(cat=cat)
    data = {'images': images, 'cats': cats}

    return render(request, "home.html", data)

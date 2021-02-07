""" below the function use for handling the request from the user can get to view http response  """

from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import *
def show_about_page(request):
    print("about page request ")
    name='learncode with NIRMAL '
    link='https://www.youtube.com/watch?v=Bapkj53UJiQ'
    #this below dictionary use for to take the data to acess it to other file using the key name (name, or link) which ever u want to use
    data={
        'name':name,
        'link':link
    }
    return render(request,"about.html",data)
    """here the render is used to synchonising the content that we will write in 
                                     about.html page show that each time it get refresh it will collect all this from that
                                     file only using request for requesting and the file and the dictionary data that we need 
                                     to get show , so here we will passed {} empty dictionary
                                     """
def show_home_page(request):
    acts=Category.objects.all()

    data={'images':image,'cats':cat}
    images=Image.objects.all()



    return render(request,"home.html",data)


def show_category_page(request,cid):
    print(cid)
    cats= Category.objects.all()

    category=Category,object.get(pk=cid)
    print(cat)

    images = Image.objects.filter(cat=category)
    data = {'images': images, 'cats': cats}

    return render(request, "home.html", data)
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from .models import Item
from django.template import loader
# Create your views for food/ here.

##index view 
def index(request):
    item_list= Item.objects.all()
    # template= loader.get_template('food/index.html')
    ##template needs a context from the db
    context={
        'item_list': item_list, ##item_list is passed to the html
    }
    # return HttpResponse('Hello World')
    # return HttpResponse(item_list)
    #return HttpResponse(template.render(context,request))
    ##OR
    return render(request, 'food/index.html', context) ## pass the path to templaye and context to the render

def item(request):
    return HttpResponse("<h1>This is an item view</h1>")


def detail(request,item_id):
    item= Item.objects.get(pk=item_id)
    context= {
        'item':item,
    }
    return render(request,'food/detail.html', context)

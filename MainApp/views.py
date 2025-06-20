from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, HttpResponse
from MainApp.models import Item
from django.http import HttpResponseNotFound
items = [...]




# Create your views here.

def home(request):
    context = {"name" : "Roman",
               "surname" : "Erm"
    }
    return render(request, 'index.html', context)


def about(request):
    text = "<h1>About Page</h1>"
    return HttpResponse(text)

def items_list(request):
    items = Item.objects.all()
    context = {"items": items}
    return render(request, 'items.html',context )

def item_page(request , id):
    try:
        item =Item.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponse("Item not found")

    context = {
        "item": item

    }
    return render(request, 'item.html', context)









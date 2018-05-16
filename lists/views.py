from django.shortcuts import render, redirect
from lists.models import Item, List

def home_page(request):
    return render(request, 'lists/home.html')

def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    items = Item.objects.filter(list=list_)
    return render(request, 'lists/list.html', {'items': items})

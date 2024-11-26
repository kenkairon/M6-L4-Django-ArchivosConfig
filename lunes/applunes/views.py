from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from django.db import DatabaseError
from .models import Item

# Create your views here.

def item_list(request: HttpRequest) -> HttpResponse:
    try:
        items = Item.objects.all()
    except DatabaseError:
        items = []

    paginator = Paginator(items, 10)  # 10 ítems por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'applunes/item_list.html', {'items': page_obj})

"""
from django.views.generic import ListView
from .models import Item

class ItemListView(ListView):
    model = Item
    template_name = 'item_list.html'
    context_object_name = 'items'
    paginate_by = 10
"""

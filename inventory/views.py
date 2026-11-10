from django.shortcuts import render, get_object_or_404
from .models import Item
# Create your views here.

def item_list(request):
    """view to display items."""
    items = Item.objects.all().order_by('-created_at')
    context = {
        'items': items,
        'page_title': 'All Catalog Items'
    }
    return render(request, 'inventory/item_list.html', context)

def item_detail(request, pk):
    """view to display details of each item."""
    item = get_object_or_404(Item, pk=pk)
    context = {
        'item': item,
        'page_title': item.title
    }
    return render(request, 'inventory/item_detail.html', context)

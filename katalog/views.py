from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_catalog(request):
    data_barang_katalog = CatalogItem.objects.all()
    context = {
        'Name' : 'Symphony Cellis Zaana Saraaya',
        'StudentID' : '2106752060',
        'list_barang' : data_barang_katalog
    }
    return render(request, "katalog.html", context)
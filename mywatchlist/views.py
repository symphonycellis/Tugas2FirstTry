from django.shortcuts import render
from mywatchlist.models import barangMyWatchList

from django.http import HttpResponse
from django.core import serializers

# Create your views here.

def show_mywatchlist(request):
    data_barang_mywatchlist = barangMyWatchList.objects.all()
    context = {
        'list_movies': data_barang_mywatchlist,
        'Name': 'Symphony',
        'StudentID' : '2106752060'
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = barangMyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = barangMyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
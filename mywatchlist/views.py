from django.shortcuts import render
from mywatchlist.models import BarangMywatchlist
from django.http import HttpResponse
from django.core import serializers

def show_mywatchlist_html(request):
    data_barang_mywatchlist = BarangMywatchlist.objects.all()
    context = {
        "nama" : "Amanda Nurul Izzah",
        "student_id" : "2106634080",
        "list_barang" : data_barang_mywatchlist,
    }

    return render(request, "mywatchlist.html", context)

def show_mywatchlist_json(request):
    data = BarangMywatchlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_mywatchlist_xml(request):
    data = BarangMywatchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

from django.shortcuts import render, redirect, HttpResponse
from .models import donat


def index(request):
    don = donat.objects.order_by()
    data = {"d": don}
    return render(request, 'main/1.html', context=data)
def termini(request):
    return render(request, 'main/html/termini.html')
def obzhie_pravila(request):
    return render(request, 'main/html/obzhie_pravila.html')
def pravila_dla_donaterov(request):
    return render(request, 'main/html/pravila_dla_donaterov.html')
def pravila_stroitelstva(request):
    return render(request, 'main/html/pravila_stroitelstva.html')
def pravila_administrirovania(request):
    return render(request, 'main/html/pravila_administrirovania.html')
def pravila_obzhenia(request):
    return render(request, 'main/html/pravila_obzhenia.html')
def murdermystery(request):
    return render(request, 'main/html/murdermystery.html')
def bedwars(request):
    return render(request, 'main/html/bedwars.html')
def rules(request):
    return render(request, 'main/html/rules.html')
def podderzhka(request):
    return render(request, 'main/html/podderzhka.html')
def razban(request):
    return render(request, 'main/html/razban.html')
def keysi(request):
    return render(request, 'main/html/keysi.html')
def zuzcoin(request):
    return render(request, 'main/html/zuzcoin.html')



from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from webapp.models import Place
from webapp.models import Team


def demo(request):
    obj = Place.objects.all()

    return render(request, "index.html", {'result': obj})


def demo(request):
    obj = Team.objects.all()
    return render(request, "index.html", {'result': obj})

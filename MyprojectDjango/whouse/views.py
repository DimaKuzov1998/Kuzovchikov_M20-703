from django.http import HttpResponse
from .models import Pr
from .models import Client
from .models import Rack
from .models import Room
from django.shortcuts import render

def index(request):
    bbs = Pr.objects.order_by('-recdate')
    return render(request, "whouse/index.html", {'bbs': bbs})

from .models import Bb
from django.shortcuts import render

def index(request):
    bbs = Bb.objects.all()
    return render(request, "btest/index.html", {'bbs': bbs})

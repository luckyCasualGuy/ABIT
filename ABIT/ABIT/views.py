# This file is just for testing perpose

from django.http import request
from django.shortcuts import render

def homeView(request):
    return render(request, "base.html")
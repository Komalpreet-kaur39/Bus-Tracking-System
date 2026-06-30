from django.shortcuts import render, redirect

# def home1(request):
#     return render(request, 'base.html')
import os
from django.conf import settings

def home1(request):
    # print(f"Template directories: {settings.TEMPLATES[0]['DIRS']}")
    return render(request, 'base.html')

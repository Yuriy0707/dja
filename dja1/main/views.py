from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')

def index2(request):
    return render(request, 'main/index2.html')
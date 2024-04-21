from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def info(request):
    return render(request, 'info.html')


def test(request):
    return render(request, 'test.html')
def oppo(request):
    return render(request, 'oppo.html')





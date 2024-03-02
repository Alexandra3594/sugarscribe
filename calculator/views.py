from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def submit_data(request):
    if request.method == 'POST':
        data = request
        print(data)
        print(type(data))
    return HttpResponse('Success', status=200)

from django.shortcuts import render
from django.http import  HttpResponse
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def index(request):
    return render(request, 'urlconvert/index.html')

def convert(request):
    request.encoding='utf-8'
    print(request.body)
    print(request.body)
    if request.method == 'POST':
        if request.POST:
            print("POST OK!!!!!!!")
            return HttpResponse("POST OK!!!!!!!")
        else:
            print("POST Failed!!!!!!!")
            return HttpResponse("POST Failed!!!!!!!")
    elif request.method == "GET":
        return HttpResponse("Get OK")
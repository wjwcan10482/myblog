from django.shortcuts import render
from django.http import  HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests
@csrf_exempt
def index(request):
    return render(request, 'urlconvert/index.html')

def convert(request):
    request.encoding='utf-8'
    if request.method == 'POST':
        if request.POST:
            sourceurl = str(request.body, encoding = "utf-8")
            print(sourceurl)
            print(sourceurl.split('/')[-1])
            sourcesoftname= sourceurl.split('/')[-1]
            r = requests.get(sourceurl)
            with open("/usr/share/nginx/html/soft/"+sourcesoftname, "wb") as code:
                code.write(r.content)
            return HttpResponse("POST OK!!!")
        else:
            print("POST Failed!!!!!!!")
            return HttpResponse("POST Failed!!!!!!!")
    elif request.method == "GET":
        return HttpResponse("Get OK")
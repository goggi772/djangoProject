from django.shortcuts import render

# Create your views here.
def company_intro(request):  #회사 소개
    return render(request, 'mysite/about/company.html')

def service_intro(request):  #서비스 소개
    return render(request, 'mysite/about/service.html')

def directions(request):  #오시는길
    return render(request, 'mysite/about/directions.html')
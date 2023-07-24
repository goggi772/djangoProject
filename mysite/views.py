from django.http import HttpResponse
from django.shortcuts import render

from mysite.models import News


# Create your views here.
def index(request):
    # return HttpResponse("Hello, World!")

    # content_list = MainContent.objects.order_by('-pub_date')
    # context = {'content_list': content_list}
    return render(request, 'mysite/home.html')


def about(request):

    news_list = News.objects.order_by('-pub_date')
    context = {'news_list': news_list}
    return render(request, 'mysite/about.html', context)


def contact(request):
    return render(request, 'mysite/recruitment.html')


def post(request):
    return render(request, 'mysite/inquiry.html')

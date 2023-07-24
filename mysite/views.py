from django.http import HttpResponse
from django.shortcuts import render

from mysite.models import News, recruitment


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
    recru_list = recruitment.objects.order_by('-pub_date')
    context = {'recru_list': recru_list}
    return render(request, 'mysite/recruitment.html', context)


def post(request):
    return render(request, 'mysite/inquiry.html')

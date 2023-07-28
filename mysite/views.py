from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from mysite.models import News, recruitment


# Create your views here.
def index(request):  #홈
    return render(request, 'mysite/home.html')


def news(request):  #새소식

    news_list = News.objects.order_by('-pub_date')
    context = {'news_list': news_list}
    return render(request, 'mysite/news.html', context)


def recru(request): #채용
    recru_list = recruitment.objects.order_by('-pub_date')
    context = {'recru_list': recru_list}
    return render(request, 'mysite/recruitment.html', context)

def recru_view(request, recru_id):
    recruit = get_object_or_404(recruitment, id=recru_id)
    return render(request, 'mysite/recru_view.html', {'recru': recruit})

def inquiry(request):  #문의
    return render(request, 'mysite/inquiry/inquiry.html')






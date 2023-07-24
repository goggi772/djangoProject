from django.http import HttpResponse
from django.shortcuts import render

from mysite.models import MainContent


# Create your views here.
def index(request):
    # return HttpResponse("Hello, World!")

    # content_list = MainContent.objects.order_by('-pub_date')
    # context = {'content_list': content_list}
    return render(request, 'mysite/home.html')


def about(request):
    return render(request, 'mysite/about.html')


def contact(request):
    return render(request, 'mysite/contact.html')


def post(request):
    return render(request, 'mysite/post.html')

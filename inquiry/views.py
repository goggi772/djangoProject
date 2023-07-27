import datetime

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from inquiry import models
from inquiry.models import writing

# Create your views here.
def customer_comments(request):  #고객의견
    com_list = writing.objects.order_by('-pub_date')
    return render(request, 'mysite/inquiry/comments.html', {'com_list': com_list})

def comments_view(request, id):
    comment = get_object_or_404(writing, id=id)
    return render(request, 'mysite/inquiry/comments_view.html', {'comment': comment})

def comments_writing(request):  #고객의견 글쓰기
    # if not request.user.is_authenticated:
    #     messages.info(request, "로그인해주세요.")
    #     return redirect("/inquiry/comments")
    if request.method == "POST":
        if request.POST["title"] == "":
            messages.info(request, "제목을 입력해주십시오.")
            return redirect("/inquiry/writing")
        elif request.POST["content"] == "":
            messages.info(request, "내용을 입력해주십시오.")
            return redirect("/inquiry/writing")

        post = models.writing()
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        post.writer = request.user.username
        post.pub_date = datetime.datetime.now()
        post.save()
        return HttpResponseRedirect(reverse('inquiry:comments'))
    else:
        return render(request, 'mysite/inquiry/writing.html')

def customer_center(request):  #고객센터
    return render(request, 'mysite/inquiry/cus_center.html')
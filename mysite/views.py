from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from mysite.forms import RecruCreateCommentForm
from mysite.models import News, recruitment, Comment


# Create your views here.
def index(request):  # 홈
    return render(request, 'mysite/home.html')


def news(request):  # 새소식

    news_list = News.objects.order_by('-pub_date')
    context = {'news_list': news_list}
    return render(request, 'mysite/news.html', context)


def recru(request):  # 채용
    recru_list = recruitment.objects.order_by('-pub_date')
    context = {'recru_list': recru_list}
    return render(request, 'mysite/recruitment.html', context)


def recru_view(request, recru_id):
    recruit = get_object_or_404(recruitment, id=recru_id)
    return render(request, 'mysite/recru_view.html', {'recru': recruit})


def inquiry(request):  # 문의
    return render(request, 'mysite/inquiry/inquiry.html')


@login_required(login_url='accounts:login')
def recru_comment_create(request, recru_id):
    recru_list = get_object_or_404(recruitment, pk=recru_id)

    if request.method == 'POST':
        form = RecruCreateCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.content_list = recru_list
            comment.author = request.user
            comment.save()
            return redirect('recru_view', recru_id=recru_list.id)
    else:
        form = RecruCreateCommentForm()

    context = {'recru': recru_list, 'form': form}
    return render(request, 'mysite/recru_view.html', context)


@login_required(login_url='accounts:login')
def recru_comment_update(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        raise PermissionDenied
    if request.method == 'POST':
        form = RecruCreateCommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('recru_view', recru_id=comment.content_list.id)
    else:
        form = RecruCreateCommentForm(instance=comment)

    context = {'comment_': comment, 'form': form}
    return render(request, 'mysite/recru_comment.html', context)


@login_required(login_url='accounts:login')
def recru_comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user != comment.author:
        raise PermissionDenied
    else:
        comment.delete()
    return redirect('recru_view', recru_id=comment.content_list.id)

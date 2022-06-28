from django.shortcuts import get_object_or_404, redirect, render

from .models import New, Comment
from .forms import NewForm, NewFormMine, CommentForm

def news_list(request):
    news = New.objects.all().order_by('-created')
    return render(request, 'new/news_list.html', {'news': news})

def news_detail(request, id):
    new = get_object_or_404(New, id=id)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = new
            if request.user.is_authenticated:
                comment.author = request.user
            comment.save()
            return redirect("new:detail", id=id)
    return render(request, 'new/news_detail.html', {'new': new, 'form': form})

def create(request):
    form = NewForm()
    if request.method == "POST":
        form = NewForm(request.POST, request.FILES)
        if form.is_valid:
            new = form.save()
            return redirect("new:list")
    return render(request, 'new/create.html', {"form": form})

def remove(request, id):
    new = get_object_or_404(New, id=id)
    new.delete()
    return redirect("new:list")


def my_news(request,):
    news = New.objects.filter(author=request.user).order_by('-created')
    return render(request, 'new/my_news.html', {'news':news})


def my_create(request):
    form = NewFormMine()
    if request.method == "POST":
        form = NewFormMine(request.POST, request.FILES)
        if form.is_valid:
            new = form.save(commit=False)
            new.author = request.user
            new.save()
            return redirect("new:my_news")
    return render(request, 'new/create.html', {"form": form})

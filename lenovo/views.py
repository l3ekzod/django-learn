# from django.shortcuts import HttpResponse, redirect, render
# from django.contrib.auth.models import UserUpdateForm
# from django.contrib.auth.models import User, Group

from django.shortcuts import render
from new.models import New
from extra.models import Carousel

def home(request):
    news = New.objects.all()[:4]
    carousel = Carousel.objects.all()
    return render(request, 'pages/home.html', {"home": home, 'carousel': carousel, "news": news})

# def users_view(request):
#     users = User.objects.all()
#     return render(request, 'users.html', {"users": users})

# def update_view(request, pk):
#     user = User.objects.get(pk=pk)
#     if request.method == 'GET':
#         user.username = request.GET.get('username')
#         user.email = request.GET.get('email')
#         user.save()
#         return redirect('users')

#     form = UserUpdateForm(Initial)


# def groups_view(request):
#     groups = Group.objects.all()
#     return render(request, 'groups.html', {"groups": groups})

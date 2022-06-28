from django.shortcuts import render, get_object_or_404, redirect
from .models import Choice, Question
from django.contrib.auth.models import User, Group
from .forms import ChoiceForm
# Create your views here.


def users_view(request):
    users = User.objects.all()
    return render(request, 'accounts/users.html', {"users": users})

def groups_view(request):
    groups = Group.objects.all()
    return render(request, 'accounts/groups.html', {"groups": groups})


def savollar(request):
    savollar = Question.objects.all()
    return render(request, 'question/savollar.html', {'savollar': savollar})



def savol_detail(request, id):
    # bu yerda Question modelidan id si parametrda kelayotgan
    # id ga teng bo'lgan object olinadi
    savol = get_object_or_404(Question, id=id)
    return render(request, 'question/savol.html', {'savol':savol})


def check_answer(request, variant_id):
    # bu yerda Choice modelidan id si parametrda kelayotgan 
    # variant id ga teng bo'lgan object olinadi
    javob = get_object_or_404(Choice, id=variant_id)
    correct = javob.is_correct
    return render(request, 'question/checked.html', {'correct': correct})


def create_question(request):
    if request.method == "POST":
        question = request.POST.get('question')
        Question.objects.create(question=question)
        return redirect('poll:savollar')
    return render(request, 'question/create_question.html')


# def create_group(request):
#     if request.method == "POST":
#         groups = request.POST.get('groups')
#         Group.objects.create(groups=groups)
#         return redirect('poll:groups')
#     return render(request, 'accounts/create_group.html')


def delete_question(request, id):    
    question = Question.objects.get(id=id)
    question.delete()
    return redirect('poll:savollar')

# def delete_group(request, id):
#     group = Group.objects.get(id=id)
#     group.delete()
#     return render(request, 'groups.html')


def create_choice(request):
    form = ChoiceForm()
    if request.method == "POST":
        form = ChoiceForm(data=request.POST)
        if form.is_valid():
            choice = form.save()
            return redirect("poll:savollar")
    return render(request, 'question/create_choice.html', {"form": form})

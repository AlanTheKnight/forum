from django.shortcuts import render, redirect
from .forms import MessageCreationForm
from .models import JoinTeamMessages



def homepage(request):
    return render(request, 'homepage.html')


def join_us(request):
    form = MessageCreationForm()
    if request.method == "POST":
        form = MessageCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    context = {'form':form}
    return render(request, 'join.html', context)
    
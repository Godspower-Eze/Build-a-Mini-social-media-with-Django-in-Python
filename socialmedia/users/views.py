from django.shortcuts import render, redirect
from .forms import CreationForm


def user_creation(request):
    form = CreationForm()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = CreationForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            form.save()
            return redirect('home')
    elif request.method == 'GET':
        form = CreationForm()
    return render(request, 'users/creation_form.html', context)

from django.shortcuts import render, redirect
from .forms import UserForm


def index(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin:login')

    context = {'form': form}
    return render(request, 'user_form.html', context)

# Create your views here.

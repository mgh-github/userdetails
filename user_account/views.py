from django.shortcuts import render
from .forms import UserForm



def index(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

    context = {'form' : form}
    return render(request, 'user_form.html', context)

# Create your views here.

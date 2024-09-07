from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


#Z defaultu wszystkie requesty są jako GET, dlatego musimy dodać zapytanie IF by uwzględnić POST request
def register(request):
    if request.method == 'POST':
        register_form=UserCreationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,('Nowe konto zostało utworzone. Miłej pracy!'))
            return redirect('register')

    else:
        register_form = UserCreationForm()
    return render(request,'register.html',{'register_form':register_form})

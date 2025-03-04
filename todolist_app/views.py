from django.shortcuts import render, redirect
from django.http import HttpResponse
from todolist_app.models import Tasklist
from todolist_app.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required



# Umieszczamy tutaj dekorator (login_required) dla całej aplikacji todolist, by zarządzac co moga widzieć nie zalogowani userzy.
# Sam dekorator, bez sciezki bedzie pokazywal error. Potrzebny jest odnosnik do "login" w settings.py
# Zabezpieczamy się nadpisując na każdą funkcją poniższy dekorator, w ten sposób NIE zalogowany user nie bedzie widział danych na pod stronach, dopóki sie nie zaloguje.

@login_required
def todolist(request):
    if request.method == "POST":
        form= TaskForm(request.POST or None)
        if not form.is_valid():
            messages.error(request, (
                'Upsss... nazwa zadania jest za długa, spróbuj ponownie.'))  # zwraca info w przypadku gdy nazwa taska jest za długa > 300 znaków
            return redirect('todolist')

        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
        messages.success(request,('Added new task.'))
        return redirect('todolist')
    else:
        all_tasks= Tasklist.objects.filter(owner=request.user) # user bedzie widzial tylko swoje taski, ale mozna to zmienic zawsze.
        # jesli w all_tasks chcemy by taski byly widoczne dla wszystkich to zmieniamy na all_tasks = Tasklist.objects.all()- dodanie nawiasów jest wymagane by Paginator działał

        paginator= Paginator(all_tasks,5) # ile tasków ma się pojawiac na 1 stronie.
        page = request.GET.get('page') # w zależnosci jak to nazwiemy, po tej nazwie odnosnik URL sie odwoływal do strony np. page = 2
        all_tasks = paginator.get_page(page)

        return render(request, 'todolist.html', {'all_tasks': all_tasks})

@login_required
def complete_task(request,task_id):
    task = Tasklist.objects.get(pk=task_id)
    if task.owner == request.user:
        task.done = True
        task.save()
    else:
        messages.error(request,('Brak dostępu, skontaktuj się z Task Ownerem'))
    return redirect('todolist')

@login_required
def pending_task(request,task_id):
    task = Tasklist.objects.get(pk=task_id)
    task.done = False
    task.save()
    return redirect('todolist')

@login_required
def delete_task(request,task_id):
    task = Tasklist.objects.get(pk=task_id)
    if task.owner == request.user:
        task.delete()
    else:
        messages.error(request, ('Brak dostępu, skontaktuj się z Task Ownerem'))

    return redirect('todolist')

@login_required
def edit_task(request,task_id):
    if request.method == "POST":
        task = Tasklist.objects.get(pk=task_id)
        form= TaskForm(request.POST or None, instance= task)
        if form.is_valid():
            form.save()

        messages.success(request,('Task Edited.'))
        return redirect('todolist')
    else:
        task_obj= Tasklist.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task_obj': task_obj})

@login_required
def contact(request):
    context = {
        'contact_text':'Strona kontaktowa'}
    return render(request, 'contact.html', context)

@login_required
def about(request):
    context = {
        'about_text':'Witaj na Naszej stronie'}
    return render(request, 'about.html', context)

@login_required
def index(request):
    context = {
        'index_text':'Welcome to the Home Page'}
    return render(request, 'index.html', context)
from django.shortcuts import render, redirect
from .models import Todo
from django.http import HttpResponse
def index(request):
    todos = Todo.objects.all()[:10]
    context = {
        'todos' : todos
    }
    return  render(request, 'index.html', context)

def details(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        'todo' : todo
    }
    return  render(request, 'detail.html', context)

def add(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']
        todo = Todo(title=title, text=text)
        todo.save()
        return redirect('/todos')
    else:
        return render(request, 'add.html')

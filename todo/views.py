from django.shortcuts import render
from django.http import HttpResponse

from . import models


from django.forms import ModelForm

class AddTodoForm(ModelForm):
    class Meta:
        model = models.TodoItem
        fields = ["title"]


class EditTodoForm(ModelForm):
    class Meta:
        model = models.TodoItem
        fields = ["title", "description", "due_date", "completed"]


def index(request):
    todos = models.TodoItem.objects.all()
    form = AddTodoForm()
    return render(request, "todo/index.html", {"todo_items": todos, 'add_form': form})


def action_add_new_todo(request):
    if request.method == "POST":
        form = AddTodoForm(request.POST)
        if form.is_valid():
            instance = form.save()
            return render(request, "todo/partial_todo_item.html", {"item": instance})
        else:
            return todo


def action_toggle_todo(request, item_id):
    item = models.TodoItem.objects.get(id=item_id)
    item.completed = not item.completed 
    item.save()
    return render(request, "todo/partial_todo_item.html", {"item": item})


def action_delete_todo(request, item_id):
    item = models.TodoItem.objects.get(id=item_id)
    item.delete() 
    return HttpResponse("")
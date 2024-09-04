from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

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


@require_http_methods(["GET"])
def index(request):
    todos = models.TodoItem.objects.all()
    form = AddTodoForm()
    return render(request, "todo/index.html", {"todo_items": todos, "add_form": form})


@require_http_methods(["POST"])
def action_add_new_todo(request):
    form = AddTodoForm(request.POST)
    if form.is_valid():
        instance = form.save()
        return render(request, "todo/partial_todo_item.html", {"item": instance})
    else:
        return render(
            request,
            "todo/partial_alert.html",
            {
                "heading": f"Error adding item",
                "message": f"Error adding item: {form.errors}",
            },
        )


@require_http_methods(["PUT"])
def action_toggle_todo(request, item_id):
    item = models.TodoItem.objects.get(id=item_id)
    item.completed = not item.completed
    item.save()

    if item.completed:
        return render(
            request,
            "todo/partial_alert.html",
            {
                "heading": f"Item completed",
                "message": f"Marked item '{item.title}' as completed",
            },
        )
    else:
        return render(
            request,
            "todo/partial_alert.html",
            {
                "heading": f"Item marked as incomplete",
                "message": f"Marked item '{item.title}' as incomplete",
            },
        )


@require_http_methods(["DELETE"])
def action_delete_todo(request, item_id):
    item = models.TodoItem.objects.get(id=item_id)
    item.delete()
    return render(
        request,
        "todo/partial_alert.html",
        {
            "heading": f"Item deleted successfully",
            "message": f"Deleted item '{item.title}' successfully",
        },
    )

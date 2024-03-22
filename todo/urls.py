from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    
    # POST 
    path("action_add_new_todo", views.action_add_new_todo, name="action_add_new_todo"),
    path("action_toggle_todo/<int:item_id>", views.action_toggle_todo, name="action_toggle_todo"),
    
    
    
    # DELETE
    path("action_delete_todo/<int:item_id>", views.action_delete_todo, name="action_delete_todo"),

    
]

from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    
    # POST 
    path("action_add_new_todo", views.action_add_new_todo, name="action_add_new_todo"),
    path("action_toggle_todo/<int:item_id>", views.action_toggle_todo, name="action_toggle_todo"),
    
    
    
    # DELETE
    path("action_delete_todo/<int:item_id>", views.action_delete_todo, name="action_delete_todo"),

    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.urls import path
from .views import TodoListView, TodoCreateView, TodoUpdateView, TodoDeleteView, TodoDeleteAllView, TodoDeleteSelectedView
# from .views import TodoListView, ToDoCreateView, ToDoUpdateView, ToDoDeleteView


urlpatterns = [
    path('', TodoListView.as_view(), name='todo_list_view'),
    path('create/', TodoCreateView.as_view(), name='todo_create_view'),
    path('update/<int:pk>/', TodoUpdateView.as_view(), name='todo_update_view'), 
    path('delete/<int:pk>/', TodoDeleteView.as_view(), name='todo_delete_view'),  
    path('delete', TodoDeleteAllView, name="delete_all_view"),
    path('delete-selected', TodoDeleteSelectedView, name='delete_selected_view'),
]

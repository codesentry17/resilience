from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import Todos
from django.contrib import messages


# Create your views here.


class TodoListView(ListView):
    model = Todos
    template_name = 'todoMVC/listTaskPage.html'
    context_object_name = 'todos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks_count"] = Todos.objects.all().count()
        return context



from django.views.generic.edit import CreateView, UpdateView, DeleteView

class TodoCreateView(CreateView):
    model = Todos
    template_name = 'todoMVC/formPage.html'
    fields = ["title","task"]

    success_url = reverse_lazy('todo_list_view')

    def form_valid(self, form):
        response = super().form_valid(form)
        
        # Add a success message after creating the Todo
        messages.success(self.request, f"Task {self.object.title} created successfully.")
        
        # Return the response
        return response



class TodoUpdateView(UpdateView):
    model = Todos
    template_name = 'todoMVC/formPage.html'
    fields = ["title","task"]
    success_url = reverse_lazy('todo_list_view')

    def form_valid(self, form):
        task = self.get_object()

        messages.success(self.request, f"Task: {task.title} Updated Successfully")
        return super().form_valid(form)



class TodoDeleteView(DeleteView):
    model = Todos
    success_url = reverse_lazy('todo_list_view')
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Task Deleted")
        return super(TodoDeleteView, self).delete(request, *args, **kwargs)



def TodoDeleteAllView(request):
    if request.method == "POST":
        print("delete called")
        Todos.objects.all().delete()
        messages.success(request, "All Tasks have been deleted")
        return redirect('todo_list_view')
    


def TodoDeleteSelectedView(request):
    if request.method == "POST":
        selected_task_ids = request.POST.getlist('selected_rows')
        # print(selected_task_ids)
        Todos.objects.filter(id__in=selected_task_ids).delete()
        messages.success(request, "All selected tasks have been deleted")
        return redirect('todo_list_view')
    
    else:
        return HttpResponse(status=404)


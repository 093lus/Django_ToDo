from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.db.models import Q

# Create your views here.
from django.urls import reverse
from django.views import generic
from django.views.generic import ListView, CreateView, DeleteView, DetailView

from task.forms import TaskForm
from task.models import Task


class TaskList(ListView):
    model = Task
    template_name = 'templates/task/list.html'


class TaskCreate(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'templates/task/create.html'
    success_url = '..'


class TaskDelete(DeleteView):
    model = Task

    def delete(self, request, pk):
        Task.objects.get(id=pk).delete()
        return JsonResponse(pk, safe=False)


class TaskSearch(DetailView):
    model = Task

    def get(self, request, key):
        searched_task_ids = Task.objects.filter(Q(name__contains=key) | Q(description__contains=key)).values_list('id',
                                                                                                                  flat=True)
        return JsonResponse(list(searched_task_ids), safe=False)


class TaskReorder(generic.View):
    model = Task

    def post(self, request):
        newIndex = int(self.request.POST.get('newIndex', 1))+1
        oldIndex = int(self.request.POST.get('oldIndex', 1))+1
        moved_object = Task.objects.get(order=oldIndex)
        Task.objects.move(moved_object, newIndex)
        return HttpResponse('ok')

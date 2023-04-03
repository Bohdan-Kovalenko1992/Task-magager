from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from todo.forms import TaskForm, TagForm
from todo.models import Task, Tag


def index(request):
    """View function for the home page of the site."""

    num_tasks = Task.objects.count()
    num_tags = Tag.objects.count()

    context = {
        "num_tasks": num_tasks,
        "num_tags": num_tags,
    }

    return render(request, "todo/index.html", context=context)


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "todo/index.html"
    queryset = Task.objects.prefetch_related("tags")


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:index")


class TagListView(generic.ListView):
    model = Tag
    context_object_name = 'tag_list'
    template_name = "todo/tags_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")
    template_name = "todo/tag_form.html"


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")


class TaskToggleView(generic.View):
    def post(self, request, pk):
        task = Task.objects.get(id=pk)
        task.is_done = not task.is_done
        task.save()

        return redirect(reverse_lazy('todo:index'), permanent=True)

    def get(self, request):
        return redirect(reverse_lazy('todo:index'), permanent=True)

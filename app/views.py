from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, View

from apps.tasks.models import Task

from .tasks import schedule_notification_task


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "task_list.html"
    context_object_name = "tasks"

    def get_queryset(self):

        return Task.objects.filter(user=self.request.user)


class TaskCreateView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "create_task.html")

    def post(self, request):
        title = request.POST.get("title")
        description = request.POST.get("description")
        due_at = request.POST.get("due_at")
        user = request.user

        task = Task.objects.create(
            title=title, description=description, due_at=due_at, user=user
        )

        schedule_notification_task(task.id)

        return redirect("task_list")


def mark_task_done(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.status = "completed"
    task.save()
    return redirect("task_list")

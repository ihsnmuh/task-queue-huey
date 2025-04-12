from django.shortcuts import redirect, render
from django.views.generic import ListView, View

from apps.tasks.models import Task

from .tasks import schedule_notification_task


class TaskListView(ListView):
    model = Task
    template_name = "task_list.html"
    context_object_name = "tasks"

    def get_queryset(self):

        return Task.objects.filter(user=self.request.user)


class TaskCreateView(View):
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

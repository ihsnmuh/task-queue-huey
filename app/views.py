from django.views.generic import ListView, View
from apps.tasks.models import Task
from apps.notifications.models import Notification
from django.shortcuts import render, redirect
from .tasks import task_do_something

class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):

        return Task.objects.filter(user=self.request.user)

class TaskCreateView(View):
    def get(self, request):
        return render(request, "create_task.html")

    def post(self,request):
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_at = request.POST.get('due_at')
        user = request.user
        
        task_do_something()

        Task.objects.create(title=title, description=description, due_at=due_at, user=user)
        return redirect('task_list')
    
class NotificationListView(ListView):
    model = Notification
    template_name = 'notification_list.html'
    context_object_name = 'notifications'

    def get_queryset(self):
        return Notification.objects.filter(task__user=self.request.user).order_by('-sent_at')
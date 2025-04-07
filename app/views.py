from django.views.generic import ListView
from apps.tasks.models import Task

class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):

        return Task.objects.filter(user=self.request.user)
from django.urls import path

from tasks.views import TaskView

app_name = 'tasks'
urlpatterns = [
    path('<uuid:task_id>/', TaskView.as_view(), name='view'),
]
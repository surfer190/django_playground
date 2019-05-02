from django.urls import path

from waiting import views

app_name = 'waiting'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index')
]

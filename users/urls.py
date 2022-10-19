from django.urls import re_path as url
from users import views
urlpatterns = [
    url(r'^api/users$', views.todo_list, name='todo_list'),
    url(r'^api/users/(?P<id>[0-9]+)$',
        views.todo_detail, name='todo_detail'),
]

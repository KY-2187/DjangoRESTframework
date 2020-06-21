from django.conf.urls import url, include

from rest_framework import routers

from .views import (
	HomeView, TaskDetailView, TaskListView, 
	TaskCreateView, ItemViewSet, home_page
)

router = routers.DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
	url(r'^$', HomeView.as_view(), name='home'),
	url(r'^tasks$', TaskListView.as_view(), name='task-list'),
	url(r'^tasks/new$', TaskCreateView.as_view(), name='task_create')
	url(r'^task/(?P<id>[0-9]+)$', TaskDetailView.as_view(), name='task_detail'), #invalid syntax
	url(r'', include(router.urls)),
]
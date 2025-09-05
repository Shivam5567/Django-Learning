from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter

from .views_auth import SignUpView
from .views import (
    TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView
)
from .views_api import TaskViewSet

router = DefaultRouter()
router.register(r"api/tasks", TaskViewSet, basename="task")

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("create/", TaskCreateView.as_view(), name="task_create"),
    path("update/<int:pk>/", TaskUpdateView.as_view(), name="task_update"),
    path("delete/<int:pk>/", TaskDeleteView.as_view(), name="task_delete"),
   
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", auth_views.LoginView.as_view(template_name="tasks/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("", include(router.urls)),
]

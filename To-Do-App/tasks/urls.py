from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_api import TaskViewSet
from . import views
from .views_auth import SignUpView
from django.contrib.auth import views as auth_views

# REST API routing
router = DefaultRouter()
router.register(r'api/tasks', TaskViewSet, basename="task")

urlpatterns = [
    path("", views.TaskListView.as_view(), name="task_list"),
    path("create/", views.TaskCreateView.as_view(), name="task_create"),
    path("update/<int:pk>/", views.TaskUpdateView.as_view(), name="task_update"),
    path("delete/<int:pk>/", views.TaskDeleteView.as_view(), name="task_delete"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", auth_views.LoginView.as_view(template_name="tasks/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    # default api
    path("", include(router.urls)),
]

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views_auth import signup_view

urlpatterns = [
    path("", views.task_list, name="task_list"),
    path("create/", views.task_create, name="task_create"),
    path("update/<int:pk>/", views.task_update, name="task_update"),
    path("delete/<int:pk>/", views.task_delete, name="task_delete"),
    # Auth
    path("signup/", signup_view, name="signup"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="tasks/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]

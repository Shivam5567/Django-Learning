from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (   # <-- import CBV views
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
)
from .views_auth import SignUpView

urlpatterns = [
    # Tasks
    path("", TaskListView.as_view(), name="task_list"),
    path("create/", TaskCreateView.as_view(), name="task_create"),
    path("update/<int:pk>/", TaskUpdateView.as_view(), name="task_update"),
    path("delete/<int:pk>/", TaskDeleteView.as_view(), name="task_delete"),

    # Auth
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", auth_views.LoginView.as_view(template_name="tasks/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
]

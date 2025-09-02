from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib import messages


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "tasks/signup.html"
    success_url = reverse_lazy("task_list")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, "Account created successfully! 🎉")
        return super().form_valid(form)

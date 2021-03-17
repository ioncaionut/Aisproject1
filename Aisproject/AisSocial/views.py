from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import forms

from django.contrib.auth.decorators import login_required
from django.shortcuts import render


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "AisSocial/signup.html"


@login_required
def home(request):
    return render(request, 'AisSocial/home.html')
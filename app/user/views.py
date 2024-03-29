from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from  django.template.backends.jinja2 import Jinja2



class RegisterView(CreateView):
	template_name = 'user/register.html'
	form_class = UserCreationForm
	success_url = reverse_lazy('core:movie_ls')
	

from django.shortcuts import render
from .models import Relief
from . forms import ReliefForm
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


# Create your views here.
@method_decorator(login_required,name='dispatch')
class ReliefCreateView(CreateView):
    form_class = ReliefForm
    template_name='myapp/home.html'
    success_url='/thanx/'
@method_decorator(login_required, name='dispatch')   
class ReliefTemplateView(TemplateView):
    template_name='myapp/thanx.html'
@method_decorator(login_required, name='dispatch')
class ReliefListView(ListView):
    model=Relief
    form_class = ReliefForm
    template_name = 'myapp/list.html'
@method_decorator(login_required, name='dispatch')
class ReliefUpdateView(UpdateView):
    model=Relief
    form_class = ReliefForm
    template_name='myapp/home.html'
    success_url='/updatethanx/'
@method_decorator(staff_member_required, name='dispatch')
class TemplateUpdateView(TemplateView):
    template_name = 'myapp/update.html'
    success_url='/updatethanx/'
@method_decorator(staff_member_required, name='dispatch')
class ReliefDeleteView(DeleteView):
    model=Relief
    template_name='myapp/delete.html'
    success_url='/list/'
@method_decorator(staff_member_required, name='dispatch')
class TemplateDelete(TemplateView):
    template_name='myapp/itemdelete.html'





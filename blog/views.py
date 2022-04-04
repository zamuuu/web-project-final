from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import ListView
from .models import Page
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class PagesList(ListView):
    model = Page
    template_name = 'blog/pages_list.html'

class PageCreate(LoginRequiredMixin, CreateView):
        model = Page
        fields = ['title', 'subtitle', 'author', 'image_page', 'content']
        success_url = '/pages/'

class PageDetail(DetailView):
    model = Page
    template_name = 'blog/detail_page.html'

class PageEdit(LoginRequiredMixin, UpdateView):
    model = Page
    success_url = '/pages/'
    fields = ['title', 'subtitle', 'author', 'image_page', 'content']
    template_name = 'blog/edit_page.html'
    
class PageDelete(LoginRequiredMixin, DeleteView):
    model = Page
    success_url = '/pages/'

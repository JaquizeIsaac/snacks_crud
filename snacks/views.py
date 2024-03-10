from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Snack
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.

class SnackListView(ListView):
    template_name = 'snacks_list.html'
    model = Snack
    context_object_name = 'snacks'

class SnackDetailView(DetailView):
    template_name = 'snacks_detail.html'
    model = Snack
    context_object_name = 'snack'
    
class SnackCreateView(CreateView):
    template_name = 'snacks_create.html'
    model = Snack
    context_object_name = 'snack'
    fields = ['name', 'rating', 'reviewer']
    success_url = reverse_lazy('snacks_list')
    
class SnackUpdateView(UpdateView):
    template_name = 'snacks_update.html'
    model = Snack
    context_object_name = 'snack'
    fields = ['name', 'rating', 'reviewer']
    
    def get_success_url(self):
        return reverse_lazy('snacks_detail', kwargs={'pk': self.object.pk})
    
class SnackDeleteView(DeleteView):
    template_name = 'snacks_delete.html'
    model = Snack
    context_object_name = 'snack'
    success_url = reverse_lazy('snacks_list')
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Feedback
from django.urls import reverse_lazy


class FeedbackListView(ListView):
    model = Feedback
    template_name = 'feedback_list.html'


class FeedbackUpdateView(UpdateView):
    model = Feedback
    fields = ('feedback',)
    template_name = 'feedback_edit.html'


class FeedbackDeleteView(DeleteView):
    model = Feedback
    template_name = 'feedback_delete.html'
    success_url = reverse_lazy('feedback_list')


class FeedbackDetailView(DetailView):
    model = Feedback
    template_name = 'feedback_detail.html'

class FeedbackCreateView(CreateView):
    model = Feedback
    fields = ('feedback','user',)
    template_name = 'feedback_new.html'
    

# Create your views here.

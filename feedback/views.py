from django.shortcuts import render
from django.views.generic import ListView
from .models import Feedback


class FeedbackListView(ListView):
    model = Feedback
    template_name = 'feedback_list.html'

# Create your views here.

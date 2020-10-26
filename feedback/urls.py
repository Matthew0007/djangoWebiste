from django.urls import path
from .views import FeedbackListView



urlpatterns = [

    path('', FeedbackListView.as_view(), name='feedback_list'),
]

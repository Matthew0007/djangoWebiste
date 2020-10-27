from django.urls import path
from .views import (

    FeedbackListView,
    FeedbackUpdateView,
    FeedbackDetailView,
    FeedbackDeleteView,
    FeedbackCreateView,
    
)


urlpatterns = [

    path('<int:pk>/edit/', FeedbackUpdateView.as_view(), name='feedback_edit'),
    path('<int:pk>/', FeedbackDetailView.as_view(), name='feedback_detail'),
    path('<int:pk>/delete/', FeedbackDeleteView.as_view(), name='feedback_delete'),
    path('', FeedbackListView.as_view(), name='feedback_list'),
    path('new/', FeedbackCreateView.as_view(), name='feedback_new'),


]

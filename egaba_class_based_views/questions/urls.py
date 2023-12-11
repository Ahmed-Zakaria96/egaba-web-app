from django.urls import path
from .views import (
    QuestionDetailView, QuestionCreateView, QuestionEditView, QuestionDeleteView,
    AnswerCreateView, AnswerEditView, AnswerDeleteView,
)

app_name = 'questions'

urlpatterns = [
    path('<int:pk>/', QuestionDetailView.as_view(), name='question'),

    # questions
    path('ask/', QuestionCreateView.as_view(), name='ask'),
    path('edit/<int:pk>/', QuestionEditView.as_view(), name='edit'),
    path('delete/<int:pk>/', QuestionDeleteView.as_view(), name='delete'),

    # answers
    path('answer/<int:pk>/', AnswerCreateView.as_view(), name='answer'),
    path('answer/delete/<int:pk>/', AnswerDeleteView.as_view(), name='delete_answer'),
    path('answer/edit/<int:pk>/', AnswerEditView.as_view(), name='edit_answer'),
]

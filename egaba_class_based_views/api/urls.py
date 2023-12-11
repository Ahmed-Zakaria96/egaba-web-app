from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    path('notification_read/<int:id>/', NotificationRead.as_view(), name='notification_read'),
    path('follow/', Follow.as_view(), name='follow'),

    # question votes
    path('q_up_vote/<int:q_id>/', QuestionUpVote.as_view(), name='question_upvote'),
    path('q_down_vote/<int:q_id>/', QuestionDownVote.as_view(), name='question_downvote'),

    # answer votes
    path('a_up_vote/<int:q_id>/', AnswerUpVote.as_view(), name='answer_upvote'),
    path('a_down_vote/<int:q_id>/', AnswerDownVote.as_view(), name='answer_downvote'),

    # option views
    path('subj_options/<int:dep_id>/', SubjectOptions.as_view(), name='subj_options'),

]

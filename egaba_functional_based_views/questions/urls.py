from django.urls import path
from . import views

app_name = 'questions'

urlpatterns = [
    path('search', views.search, name="search"),
    path('<int:id>', views.question_details, name="question"),


    # adding/editing/deleting/marking solved a question
    path('ask', views.ask, name="ask"),
    path('edit/<int:id>', views.edit_question, name="edit_question"),
    path('delete/<int:id>', views.delete_question, name="delete_question"),
    path('answer/<int:id>', views.answer_question, name="answer_question"),


    # form options ajax
    path('university_faculty_options/<int:id>', views.faculty_options, name="faculty_options"),
    path('faculty_department_options/<int:id>', views.department_options, name="departments_options"),
    path('department_level_options/<int:id>', views.level_options, name="level_options"),
    path('level_subject_options/<int:id>', views.subject_options, name="subject_options"),
]

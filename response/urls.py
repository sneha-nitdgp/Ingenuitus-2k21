
from django.urls import path,include
from . import views

urlpatterns = [
   path('index.html/', views.get_question, name="get_question"),
   path('index2/',views.get_question_not_logged,name="get_question_not_logged")
]

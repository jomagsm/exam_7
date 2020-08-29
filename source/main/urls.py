"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from webapp.views.answer_views import AnswerCreateView, AnswerUpdateView, AnswerDeleteView
from webapp.views.quiz_views import QuizCreateView, QuizDetailView, QuizUpdateView, QuizDeleteView, QuizIndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', QuizIndexView.as_view(), name='index'),
    path('quiz_create/', QuizCreateView.as_view(), name='quiz_create'),
    path('quiz_view/<int:pk>/', QuizDetailView.as_view(), name='quiz_view'),
    path('quiz_update/<int:pk>',QuizUpdateView.as_view(), name='quiz_update'),
    path('quiz_delete/<int:pk>',QuizDeleteView.as_view(), name='quiz_delete'),
    path('answer_create/<int:pk>',AnswerCreateView.as_view(), name='answer_create'),
    path('answer_update/<int:pk>',AnswerUpdateView.as_view(), name='answer_update'),
    path('answer_delete/<int:pk>',AnswerDeleteView.as_view(), name='answer_delete')
]

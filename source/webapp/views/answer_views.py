from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, CreateView, View, UpdateView
from django.urls import reverse, reverse_lazy

from webapp.forms import AnswerForm
from webapp.models import Answer, Quiz


class AnswerCreateView(CreateView):
    model = Answer
    template_name = 'answer/answer_create.html'
    form_class = AnswerForm

    def form_valid(self, form):
        quiz = get_object_or_404(Quiz, pk=self.kwargs.get('pk'))
        answer = form.save(commit=False)
        answer.poll = quiz
        answer.save()
        return redirect('quiz_view', pk=quiz.pk)

class AnswerUpdateView(UpdateView):
    model = Answer
    template_name = 'answer/answer_update.html'
    form_class = AnswerForm

    def get_success_url(self):
        return reverse('index')
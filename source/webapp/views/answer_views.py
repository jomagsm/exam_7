from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, CreateView, View, UpdateView, DeleteView
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
        return reverse('quiz_view',kwargs={'pk':self.object.poll.pk})

    # object = self.get_object()
    # # answer = get_object_or_404(Answer, pk=self.kwargs.get('pk'))
    # print(object.poll.pk)
    # return redirect('quiz_view', pk=object.poll.pk)
    # def form_valid(self, form):
    #     quiz = get_object_or_404(Quiz, pk=self.kwargs.get('pk'))
    #     print(quiz)
    #     return redirect('quiz_view', pk=quiz.pk)


# class AnswerDeleteView(DeleteView):
#     template_name = ''
#     model = Answer
#
#     def get(self, request, *args, **kwargs):
#         return self.delete(request, *args, **kwargs)
#
#     def get_success_url(self):
#         return reverse('index')

class AnswerDeleteView(DeleteView):
    template_name = 'answer/answer_delete.html'
    model = Answer
    success_url = reverse_lazy('index')

    def get_success_url(self):
        return reverse('quiz_view',kwargs={'pk':self.object.poll.pk})
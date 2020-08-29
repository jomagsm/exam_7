from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView
from django.urls import reverse, reverse_lazy

from webapp.models import Collecting, Quiz, Answer


# class CollectingTemplateView(View):
#
#    def get(self, request, *args, **kwargs):
#        collecting = Collecting.objects.all()
#        context = {
#            'collecions': collecions
#        }
#        return render(request, 'collecting/collecting_index.html', context)
#
class CollectingTemplateView(TemplateView):
    template_name = 'collecting/collecting_view.html'
    form_class = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        quiz = get_object_or_404(Quiz,pk=pk)
        answers = Answer.objects.all()
        answers= answers.filter(poll=quiz)
        context['quiz'] = quiz
        context['answers'] = answers
        return context

    def post(self, request, *args, **kwargs):
        quiz = request.POST['select']
        answers = Answer.objects.all()
        answers = answers.filter(pk=int(quiz))
        collecting = Collecting.objects.create(quiz=answers[0].poll, answer=answers[0])
        return redirect('index')
from django.shortcuts import render
from django.views.generic import ListView

from webapp.models import Quiz


class QuizIndexView(ListView):
    template_name = 'quiz/index.html'
    context_object_name = 'quizs'
    paginate_by = 5
    paginate_orphans = 0

    def get_queryset(self):
        data = Quiz.objects.all()
        # http://localhost:8000/?search=ygjkjhg
        # form = SimpleSearchForm(data=self.request.GET)
        # if form.is_valid():
        #     search = form.cleaned_data['search']
        #     if search:
        #         data = data.filter(Q(title__icontains=search) | Q(author__icontains=search))

        return data
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse, reverse_lazy

from webapp.forms import QuizForm
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


class QuizCreateView(CreateView):
    template_name = 'quiz/quiz_create.html'
    model = Quiz
    form_class = QuizForm

    def get_success_url(self):
        return reverse('index')


class QuizDetailView(DetailView):
    template_name = 'quiz/quiz_view.html'

    def get_queryset(self):
        return Quiz.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = QuizForm
        return context


from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from webapp.forms import QuizForm
from webapp.models import Quiz, Answer


class QuizIndexView(ListView):
    template_name = 'quiz/index.html'
    context_object_name = 'quizs'
    paginate_by = 5
    paginate_orphans = 0

    def get_queryset(self):
        data = Quiz.objects.all()
        data= data.order_by('-created_at')
        # http://localhost:8000/?search=ygjkjhg
        # form = SimpleSearchForm(data=self.request.GET)
        # if form.is_valid():
        #     search = form.cleaned_data['search']
        #     if search:
        #         data = data.filter(Q(title__icontains=search) | Q(author__icontains=search))

        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['form'] = BasketForm
        return context

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


class QuizUpdateView(UpdateView):
    template_name = 'quiz/quiz_update.html'
    form_class = QuizForm
    model = Quiz

    def get_success_url(self):
        return reverse('quiz_view', kwargs={'pk': self.object.pk})


class QuizDeleteView(DeleteView):
    template_name = 'quiz/quiz_delete.html'
    model = Quiz
    success_url = reverse_lazy('index')
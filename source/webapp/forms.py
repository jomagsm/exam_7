from django import forms
from webapp.models import  Answer, Quiz


class QuizForm(forms.ModelForm):

    class Meta:
        model = Quiz
        fields = ['question']


class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ['answer']
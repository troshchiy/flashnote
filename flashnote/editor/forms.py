from django import forms
from .models import Note, Question


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['text']
        labels = {'text': ''}


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']
        labels = {'text': ''}

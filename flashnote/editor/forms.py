from django import forms
from .models import Note, Question


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['text']
        widgets = {'text': forms.Textarea(attrs={
            'rows': 1,
            'oninput': 'auto_grow(this)',
        })}
        labels = {'text': ''}


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']
        widgets = {'text': forms.Textarea(attrs={
            'rows': 1,
            'oninput': 'auto_grow(this)',
        })}
        labels = {'text': ''}

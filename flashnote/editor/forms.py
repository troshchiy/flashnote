from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['text']
        widgets = {'text': forms.Textarea(attrs={
            'rows': 1,
            'oninput': 'auto_grow(this)',
        })}
        labels = {'text': ''}

NoteFormSet = forms.modelformset_factory(Note, form=NoteForm, fields=['text'], extra=0)

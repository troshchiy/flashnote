from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['text', 'question']
        widgets = {
            'text': forms.Textarea(attrs={
                'rows': 1,
                'oninput': 'auto_grow(this)'}),
            'question': forms.Textarea(attrs={
                'rows': 1,
                'oninput': 'auto_grow(this)'})
        }
        labels = {'text': '',
                  'question': ''}


NoteFormSet = forms.modelformset_factory(Note, form=NoteForm, extra=0)

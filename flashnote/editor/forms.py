from django import forms
from .models import Notebook, Page, Note


class NotebookForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = Notebook
        fields = ['title']


class PageForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = Page
        fields = ['title']


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
                'oninput': 'auto_grow(this);set_parent_value(this);'})
        }
        labels = {'text': '',
                  'question': ''}


NotebookFormSet = forms.modelformset_factory(Notebook, form=NotebookForm, extra=0)
PageFormSet = forms.modelformset_factory(Page, form=PageForm, extra=0)
NoteFormSet = forms.modelformset_factory(Note, form=NoteForm, extra=0)

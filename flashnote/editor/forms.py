from django import forms
from .models import Notebook, Page, Note


class BaseNoteFormSet(forms.BaseModelFormSet):
    ordering_widget = forms.HiddenInput(attrs={'class': 'order'})
    deletion_widget = forms.CheckboxInput(attrs={'class': 'deletion'})


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
                'oninput': 'autoGrow(this)'}),
            'question': forms.Textarea(attrs={
                'rows': 1,
                'oninput': 'autoGrow(this);setParentValue(this);'})
        }
        labels = {'text': '',
                  'question': ''}


NotebookFormSet = forms.modelformset_factory(Notebook, form=NotebookForm, formset=BaseNoteFormSet, extra=0,
                                             can_delete=True)
PageFormSet = forms.modelformset_factory(Page, form=PageForm, formset=BaseNoteFormSet, extra=0,
                                         can_delete=True)
NoteFormSet = forms.modelformset_factory(Note, form=NoteForm, formset=BaseNoteFormSet, extra=0, can_order=True,
                                         can_delete=True)

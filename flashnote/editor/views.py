from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Notebook, Page, Note
from .forms import NoteFormSet


@login_required
def notebooks_list(request):
    notebooks = Notebook.objects.filter(author=request.user).order_by('title')
    return render(request, 'editor/notebooks/list.html', {'notebooks': notebooks,
                                                                                'section': 'notebooks'})


@login_required
def notes_list(request):
    notes_formset = NoteFormSet(queryset=Note.objects.all().order_by('created'))
    if request.method == 'POST':
        notes_formset = NoteFormSet(request.POST)
        if notes_formset.is_valid():
            for note in notes_formset:
                note.instance.author = request.user
            notes_formset.save()
    return render(request, 'editor/notes/list.html', {'notes_formset': notes_formset})

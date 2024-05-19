from django.shortcuts import render
from .models import Note
from .forms import NoteFormSet


def notes_list(request):
    notes_formset = NoteFormSet(queryset=Note.objects.all().order_by('created'))
    if request.method == 'POST':
        notes_formset = NoteFormSet(request.POST)
        if notes_formset.is_valid():
            for note in notes_formset:
                note.instance.author = request.user
            notes_formset.save()
    return render(request, 'editor/notes/list.html', {'notes_formset': notes_formset})

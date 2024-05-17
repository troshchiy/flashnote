from django.shortcuts import render
from .models import Note
from .forms import NoteForm, NoteFormSet


def notes_questions_list(request):
    notes_formset = NoteFormSet(queryset=Note.objects.all().order_by('created'))
    for note in notes_formset:
        print(note)
    if request.method == 'POST':
        #print(request.POST)
        new_notes_formset = NoteFormSet(request.POST)
        for note in new_notes_formset:
            print(note.instance.__class__)
            print(note.instance.id)
            print(note.instance.text)
            print(note.instance.created)
    return render(request, 'editor/notes/list.html', {'notes_formset': notes_formset})

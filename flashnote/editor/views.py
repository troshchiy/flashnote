from django.shortcuts import render
from .models import Note, Question


def notes_questions_list(request):
    notes = Note.objects.all()
    notes_questions = []
    for note in notes:
        try:
            question = Question.objects.get(note=note)
        except Question.DoesNotExist:
            question = None
        notes_questions.append((note, question))

    return render(request, 'editor/notes/list.html', {'notes_questions': notes_questions})

from django.shortcuts import render
from .models import Note, Question
from .forms import NoteForm, QuestionForm


def notes_questions_list(request):
    notes = Note.objects.all()
    notes_questions_forms = []
    for note in notes:
        note_form = NoteForm(instance=note)
        try:
            question = Question.objects.get(note=note)
            question_form = QuestionForm(instance=question)
        except Question.DoesNotExist:
            question_form = None
        notes_questions_forms.append((note_form, question_form))

    return render(request, 'editor/notes/list.html', {'notes_questions_forms': notes_questions_forms})

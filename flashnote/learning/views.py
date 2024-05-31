import decimal
from django.utils import timezone
from django.shortcuts import render
from django.http import Http404
from django.views import View
from editor.models import Page, Note
from editor.forms import NoteForm


class LearnView(View):
    template_name = 'learning/flashcard.html'

    def get(self, request, page_id):
        try:
            page = Page.objects.user(request.user).get(id=page_id)
        except Page.DoesNotExist:
            raise Http404

        flashcards = Note.objects.filter(page=page).exclude(question='').order_by('next_review')
        flashcard_form = NoteForm(instance=flashcards[0])
        return render(request, self.template_name, {'flashcard_form': flashcard_form})

    def post(self, request, page_id):
        try:
            flashcard = Note.objects.get(id=request.POST['note_id'])
        except Note.DoesNotExist:
            raise Http404

        user_grade = int(request.POST['user_grade'])

        # SM-2 algorithm
        # https://en.wikipedia.org/wiki/SuperMemo
        if user_grade >= 3:
            if flashcard.repetition_number == 0:
                interval = 1
            elif flashcard.repetition_number == 1:
                interval = 6
            else:
                interval = round(flashcard.inter_repetition_interval.days * flashcard.easiness_factor)
            flashcard.repetition_number += 1
        else:
            flashcard.repetition_number = 0
            interval = 1

        flashcard.inter_repetition_interval = timezone.timedelta(days=interval)
        flashcard.last_review = timezone.now()
        flashcard.next_review = flashcard.last_review + flashcard.inter_repetition_interval
        flashcard.easiness_factor = (flashcard.easiness_factor
                                     + decimal.Decimal(0.1 - (5 - user_grade) * (0.08 + (5 - user_grade) * 0.02)))
        if flashcard.easiness_factor < 1.3:
            flashcard.easiness_factor = 1.3

        flashcard.save()
        return self.get(request, page_id)


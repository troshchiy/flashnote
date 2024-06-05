import decimal
from django.utils import timezone
from django.shortcuts import render
from django.http import Http404
from django.views import View
from editor.models import Notebook, Page, Note
from editor.forms import NoteForm


class LearnView(View):
    template_name = 'learning/flashcard.html'
    no_cards_for_review_template = 'learning/no_cards_for_review.html'

    def get(self, request, notebook_or_page, notebook_or_page_id):
        if notebook_or_page == 'notebook':
            try:
                notebook = Notebook.objects.user(request.user).get(id=notebook_or_page_id)
            except Notebook.DoesNotExist:
                raise Http404

            pages = Page.objects.filter(notebook=notebook)
            cards = Note.objects.filter(page__in=pages).exclude(question='')
            notebook_or_page_title = notebook.title
        elif notebook_or_page == 'page':
            try:
                page = Page.objects.user(request.user).get(id=notebook_or_page_id)
            except Page.DoesNotExist:
                raise Http404
            cards = Note.objects.filter(page=page).exclude(question='')
            notebook_or_page_title = page.title
        else:
            raise Http404

        new_cards = cards.filter(last_review__isnull=True).order_by('order')
        due_cards = cards.filter(last_review__isnull=False).order_by('next_review')
        if new_cards:
            flashcard_form = NoteForm(instance=new_cards[0])
        elif due_cards and due_cards[0].next_review <= timezone.now():
            flashcard_form = NoteForm(instance=due_cards[0])
        else:
            return render(request, self.no_cards_for_review_template)
        return render(request, self.template_name, {'notebook_or_page': notebook_or_page,
                                                    'notebook_or_page_id': notebook_or_page_id,
                                                    'notebook_or_page_title': notebook_or_page_title,
                                                    'flashcard_form': flashcard_form})

    def post(self, request, notebook_or_page, notebook_or_page_id):
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
        return self.get(request, notebook_or_page, notebook_or_page_id)

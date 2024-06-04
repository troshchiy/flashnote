from django import template
from django.utils import timezone
from editor.models import Notebook, Page, Note

register = template.Library()


@register.simple_tag
def total_notes(notebook_or_page):
    if isinstance(notebook_or_page, Notebook):
        pages = Page.objects.filter(notebook=notebook_or_page)
        return Note.objects.filter(page__in=pages).count()

    return Note.objects.filter(page=notebook_or_page).count()


@register.simple_tag
def total_cards(notebook_or_page):
    if isinstance(notebook_or_page, Notebook):
        pages = Page.objects.filter(notebook=notebook_or_page)
        return Note.objects.filter(page__in=pages).exclude(question="").count()

    return Note.objects.filter(page=notebook_or_page).exclude(question="").count()


@register.simple_tag
def new_cards(notebook_or_page):
    if isinstance(notebook_or_page, Notebook):
        pages = Page.objects.filter(notebook=notebook_or_page)
        return Note.objects.filter(page__in=pages).exclude(question="").filter(last_review__isnull=True).count()

    return Note.objects.filter(page=notebook_or_page).exclude(question="").filter(last_review__isnull=True).count()


@register.simple_tag
def due_cards(notebook_or_page):
    if isinstance(notebook_or_page, Notebook):
        pages = Page.objects.filter(notebook=notebook_or_page)
        return Note.objects.filter(page__in=pages).exclude(question="").filter(next_review__lte=timezone.now()).count()

    return Note.objects.filter(page=notebook_or_page).exclude(question="").filter(next_review__lte=timezone.now()).count()

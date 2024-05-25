from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Notebook, Page, Note
from .forms import NoteFormSet


@login_required
def notebooks_list(request):
    notebooks = Notebook.objects.filter(author=request.user).order_by('title')
    return render(request, 'editor/notebooks/list.html', {'notebooks': notebooks,
                                                          'section': 'notebooks'})


@login_required
def notebook_content(request, notebook_slug):
    user_notebooks = Notebook.objects.filter(author=request.user)
    try:
        notebook = user_notebooks.get(slug=notebook_slug)
    except Notebook.DoesNotExist:
        raise Http404("No Notebook found.")
    pages = Page.objects.filter(notebook=notebook)
    return render(request, 'editor/notebooks/content.html', {'notebook': notebook,
                                                             'pages': pages})


@login_required
def page_content(request, page_slug):
    user_notebooks = Notebook.objects.filter(author=request.user)
    users_pages = Page.objects.filter(notebook__in=user_notebooks)
    try:
        page = users_pages.get(slug=page_slug)
    except Page.DoesNotExist:
        raise Http404("No Page found.")
    notes_formset = NoteFormSet(queryset=Note.objects.filter(page=page))
    if request.method == 'POST':
        notes_formset = NoteFormSet(request.POST)
        if notes_formset.is_valid():
            for note_form in notes_formset:
                note_form.instance.page = page
            notes_formset.save()
    return render(request, 'editor/pages/content.html', {'page': page,
                                                         'notes_formset': notes_formset})

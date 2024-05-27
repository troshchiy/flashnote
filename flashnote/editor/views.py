from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Notebook, Page, Note
from .forms import NotebookFormSet, PageFormSet, NoteFormSet


@login_required
def notebooks_list(request):
    notebooks = Notebook.objects.filter(author=request.user).order_by('title')
    notebooks_formset = NotebookFormSet(queryset=notebooks)
    if request.method == 'POST':
        notebooks_formset = NotebookFormSet(request.POST)
        if notebooks_formset.is_valid():
            for form in notebooks_formset:
                form.instance.author = request.user
            notebooks_formset.save()
    return render(request, 'editor/notebooks/list.html', {'notebooks_formset': notebooks_formset,
                                                          'section': 'notebooks'})


@login_required
def notebook_content(request, notebook_id):
    user_notebooks = Notebook.objects.filter(author=request.user)
    try:
        notebook = user_notebooks.get(id=notebook_id)
    except Notebook.DoesNotExist:
        raise Http404('No Notebook found.')

    if request.method == 'POST':
        pages_formset = PageFormSet(request.POST)
        if pages_formset.is_valid():
            for form in pages_formset:
                form.instance.notebook = notebook
            pages_formset.save()
    else:
        pages = Page.objects.filter(notebook=notebook)

        if not pages:
            new_page = Page(title='Untitled', notebook=notebook)
            new_page.save()
            pages |= Page.objects.filter(id=new_page.id)

        pages_formset = PageFormSet(queryset=pages)
    return render(request, 'editor/notebooks/content.html', {'notebook': notebook,
                                                             'pages_formset': pages_formset})


@login_required
def page_content(request, page_id):
    user_notebooks = Notebook.objects.filter(author=request.user)
    users_pages = Page.objects.filter(notebook__in=user_notebooks)
    try:
        page = users_pages.get(id=page_id)
    except Page.DoesNotExist:
        raise Http404("No Page found.")

    if request.method == 'POST':
        notes_formset = NoteFormSet(request.POST)
        if notes_formset.is_valid():
            for order, note_form in enumerate(notes_formset.ordered_forms):
                note_form.instance.page = page
                note_form.instance.order = order
                note_form.save()
    else:
        notes = Note.objects.filter(page=page)

        if not notes:
            new_note = Note(page=page, order=1)
            new_note.save()
            notes |= Note.objects.filter(id=new_note.id)

        notes_formset = NoteFormSet(queryset=notes)
    return render(request, 'editor/pages/content.html', {'page': page,
                                                         'notes_formset': notes_formset})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Notebook, Page, Note
from .forms import NotebookFormSet, PageFormSet, NoteFormSet


@login_required
def notebooks_list(request):
    if request.method == 'POST':
        notebooks_formset = NotebookFormSet(request.POST)
        if notebooks_formset.is_valid():
            for form in notebooks_formset:
                form.instance.author = request.user
            notebooks_formset.save()
            return redirect('/editor/notebooks')

    notebooks = Notebook.objects.user(request.user).order_by('title')
    notebooks_formset = NotebookFormSet(queryset=notebooks)
    return render(request, 'editor/notebooks/list.html', {'notebooks_formset': notebooks_formset,
                                                          'section': 'notebooks'})


@login_required
def notebook_content(request, notebook_id):
    try:
        notebook = Notebook.objects.user(request.user).get(id=notebook_id)
    except Notebook.DoesNotExist:
        raise Http404

    if request.method == 'POST':
        pages_formset = PageFormSet(request.POST)
        if pages_formset.is_valid():
            for form in pages_formset:
                form.instance.notebook = notebook
            pages_formset.save()
            return redirect(f'/editor/notebook/{notebook_id}')

    pages = Page.objects.filter(notebook=notebook)
    pages_formset = PageFormSet(queryset=pages)
    return render(request, 'editor/notebooks/content.html', {'notebook': notebook,
                                                             'pages_formset': pages_formset})


@login_required
def page_content(request, page_id):
    try:
        page = Page.objects.user(request.user).get(id=page_id)
    except Page.DoesNotExist:
        raise Http404

    if request.method == 'POST':
        notes_formset = NoteFormSet(request.POST)
        if notes_formset.is_valid():
            for order, note_form in enumerate(notes_formset.ordered_forms):
                note_form.instance.page = page
                note_form.instance.order = order
                note_form.instance.save(update_fields=['order'])
            notes_formset.save()
            return redirect(f'/editor/page/{page_id}')

    notes = Note.objects.filter(page=page)
    notes_formset = NoteFormSet(queryset=notes)
    return render(request, 'editor/pages/content.html', {'page': page,
                                                         'notes_formset': notes_formset})

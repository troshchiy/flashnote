from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4


class Notebook(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notebooks')

    def __str__(self):
        return f'Notebook {self.title}'


class Page(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    notebook = models.ForeignKey(Notebook, related_name='pages', on_delete=models.CASCADE)

    def __str__(self):
        return f'Page {self.title}'


class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    text = models.TextField(null=True, blank=True)
    question = models.TextField(null=True, blank=True)
    page = models.ForeignKey(Page, related_name='notes', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    order = models.IntegerField()

    class Meta:
        ordering = ['order']
        indexes = [
            models.Index(fields=['order']),
        ]

    def __str__(self):
        return f'Note id:{self.id}\nQuestion: "{self.question}"\nText: "{self.text}"'

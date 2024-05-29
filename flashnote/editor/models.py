from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
from datetime import timedelta


class UserNotebooksQuerySet(models.query.QuerySet):
    def user(self, user):
        return self.filter(author=user)


class UserPagesQuerySet(models.query.QuerySet):
    def user(self, user):
        user_notebooks = Notebook.objects.user(user=user)
        return self.filter(notebook__in=user_notebooks)


class Notebook(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notebooks')

    objects = UserNotebooksQuerySet.as_manager()

    def __str__(self):
        return self.title


class Page(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    notebook = models.ForeignKey(Notebook, related_name='pages', on_delete=models.CASCADE)

    objects = UserPagesQuerySet.as_manager()

    def __str__(self):
        return self.title


class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    text = models.TextField(blank=True)
    question = models.TextField(blank=True)
    page = models.ForeignKey(Page, related_name='notes', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    order = models.IntegerField()

    repetition_number = models.IntegerField(default=0)
    easiness_factor = models.DecimalField(default=2.5, max_digits=5, decimal_places=2)
    inter_repetition_interval = models.DurationField(default=timedelta(days=0))
    last_review = models.DateTimeField(null=True)
    next_review = models.DateTimeField(null=True)

    class Meta:
        ordering = ['order']
        indexes = [
            models.Index(fields=['order']),
        ]

    def __str__(self):
        return f'Note id:{self.id}\nQuestion: "{self.question}"\nText: "{self.text}"'

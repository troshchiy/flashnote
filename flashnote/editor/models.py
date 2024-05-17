from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4


class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    text = models.TextField()
    question = models.TextField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Note id:{self.id}\nText: "{self.text}"'

from django.contrib import admin
from .models import Notebook, Page, Note


admin.site.register(Notebook)
admin.site.register(Page)
admin.site.register(Note)

from django.contrib import admin
from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    fields = ('message', 'created_date', 'unique_words',)
    readonly_fields = ('created_date', 'unique_words',)
    list_filter = ('unique_words',)

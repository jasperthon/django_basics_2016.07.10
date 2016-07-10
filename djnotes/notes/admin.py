from django.contrib import admin

# Register your models here.

from notes.models import Note

class NoteAdmin(admin.ModelAdmin):
	list_display = (
		'id',
		'title',
		'note',
	)
	search_field = (
		'title',
		'note',
	)

admin.site.register(Note, NoteAdmin)
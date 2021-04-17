from django.contrib import admin

from .models import Notes, Authors, States
# Register your models here.
class NotesAdmin(admin.ModelAdmin):
    pass
admin.site.register([Notes, Authors, States], NotesAdmin)
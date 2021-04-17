from django.contrib import admin

from .models import Notes


# Register your models here.
class NotesAdmin(admin.ModelAdmin):
    pass


admin.site.register([Notes], NotesAdmin)

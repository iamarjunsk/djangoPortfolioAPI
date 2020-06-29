from django.contrib import admin
from .models import works

class notesAdmin(admin.ModelAdmin):
    list_display = ('title' , 'tech')
    search_fields = ('title' , 'tech')

    filter_horizontal = ()
    list_filter = ()

# Register your models here.
admin.site.register(works)
from django.contrib import admin
from .models import Notes
# Register your models here.
class notesAdmin(admin.ModelAdmin):
    list_display = ('title' , 'tech')
    search_fields = ('title' , 'tech')

    filter_horizontal = ()
    list_filter = ()

admin.site.register(Notes,notesAdmin)
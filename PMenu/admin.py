from django.contrib import admin
from .models import Book

# Register your models here.


class BookAdmin(admin.ModelAdmin): # kullandığımız class parametresine dikkat edelim!

    list_display=("id","name","created_date","isPublished")
    list_display_links=("id","name")
    list_filter=("created_date",)
    list_editable=("isPublished",)
    search_fields=("name","description")

admin.site.register(Book,BookAdmin)
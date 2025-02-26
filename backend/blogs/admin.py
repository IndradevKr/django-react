from django.contrib import admin
from .models import Author, Blogs

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    fields = ["first_name", "last_name", "email", 'is_active']
    list_display = ["first_name", "last_name", "email", "is_active"]
    search_fields = ["first_name", "email"]

admin.site.register(Author, AuthorAdmin)
        
admin.site.register(Blogs)
from django.contrib import admin
from .models import Author
from .forms import AuthorForm


class AuthorAdmin(admin.ModelAdmin):
	form = AuthorForm


admin.site.register(Author, AuthorAdmin)

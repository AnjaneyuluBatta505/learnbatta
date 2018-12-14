from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from .models import *


# Register your models here.

admin.site.register(Book)

# my dummy model

class DummyModel(models.Model):

	class Meta:
		verbose_name_plural = 'Dummy Model'
		app_label = 'sample'


def my_custom_view(request):
	return HttpResponse('Admin Custom View')


class DummyModelAdmin(admin.ModelAdmin):
    model = DummyModel

    def get_urls(self):
        view_name = '{}_{}_changelist'.format(
            self.model._meta.app_label, self.model._meta.model_name)
        return [
            path('settings/', my_custom_view, name=view_name),
        ]


admin.site.register(DummyModel, DummyModelAdmin)
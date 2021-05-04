from django.contrib import admin
from .models import Job, Application, Category



class ApplicationInline(admin.TabularInline):

    model = Application
    extra = 0

class JobAdmin(admin.ModelAdmin):

    inlines = [ApplicationInline]

admin.site.register(Job, JobAdmin)
admin.site.register(Application)
admin.site.register(Category)
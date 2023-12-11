from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ['name', 'lst_university']

    def lst_university(self, obj):
        return "\n".join([p.name for p in obj.university.all()])

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Level)
admin.site.register(Subject)

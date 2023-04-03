from django.contrib import admin

from todo.models import Tag, Task

admin.site.register(Tag)


@admin.register(Task)
class CarAdmin(admin.ModelAdmin):
    search_fields = ("content",)



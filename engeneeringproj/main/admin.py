from django.contrib import admin
from .models import News, Jobs, Documents, Blog, Articles, Questions, Answers
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget


class NewsResource(resources.ModelResource):
    class Meta:
        model = News


class NewsAdmin(ImportExportModelAdmin):
    resource_class = NewsResource

class DocumentsAdmin(admin.ModelAdmin):
    ordering = ('title',)
    list_display = ('title', 'url')
    search_fields = ('title',)

admin.site.register(News, NewsAdmin)
admin.site.register(Jobs)
admin.site.register(Documents, DocumentsAdmin)
admin.site.register(Blog)
admin.site.register(Articles)
admin.site.register(Questions)
admin.site.register(Answers)
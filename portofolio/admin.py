from django.contrib import admin

from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'category_slug', 'publish_date')
    prepopulated_fields = {'category_slug': ('category_name',)}

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'article_slug', 'publish_date', 'article_author')
    prepopulated_fields = {'article_slug': ('article_title',)}

class SettingAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'setting_value')
    fieldsets = [
        (None,               {'fields': ['setting_name']}),
        ('Value', {'fields': ['setting_value'], 'classes': ['collapse']}),
    ]

# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Project)
admin.site.register(Setting, SettingAdmin)

from django.contrib import admin
from .models import News, recruitment, Comment


# Register your models here.

class RecruitmentAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'pub_date']
    search_fields = ['title']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['content_list', 'content', 'author', 'create_date', 'modify_date']
    search_fields = ['author']


admin.site.register(News)
admin.site.register(recruitment, RecruitmentAdmin)
admin.site.register(Comment, CommentAdmin)

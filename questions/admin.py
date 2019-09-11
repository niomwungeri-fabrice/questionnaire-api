from django.contrib import admin

from .models import Question, Comment


class CommentInLine(admin.TabularInline):
    model = Comment


class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine,
    ]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Comment)

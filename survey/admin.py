from django.contrib import admin
from .models import Question,Choice


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra=3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['question_t']}),
        ('Date information', {'fields':['q_date'],'classes':['collapse']}),
    ]
    inlines = [ChoiceInLine]
    list_display = ('question_t','q_date','was_published_recently')

    list_filter = ['q_date']
    search_fields = ['question_t']
# Register your models here.
admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)

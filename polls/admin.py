from django.contrib import admin
from .models import Choice, Question

from .models import Question


class ChoiceInline(admin.ModelAdmin):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']
    #serch_files = ('question_text', 'pub_date',)
    list_filter = ('question_text',)


admin.site.register(Choice, ChoiceInline)
admin.site.register(Question, QuestionAdmin)

# Register your models here.

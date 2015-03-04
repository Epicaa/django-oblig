from django.contrib import admin

from django.contrib import admin
from polls.models import Choice, Question

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
	list_display = ('question_text', 'pub_date')

admin.site.register(Question, QuestionAdmin)

# Register your models here.


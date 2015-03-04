from django.contrib import admin

from django.contrib import admin
from polls.models import Question

admin.site.register(Question, QuestionAdmin)

# Register your models here.


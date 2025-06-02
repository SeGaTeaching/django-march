from django.contrib import admin
from .models import Example, Question, Choice

# Register your models here.
admin.site.register(Example)
admin.site.register(Question)
admin.site.register(Choice)
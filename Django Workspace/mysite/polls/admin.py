from django.contrib import admin
from .models import testModel, Question, Choice


# Register your models here.
admin.site.register(testModel)
admin.site.register(Question)
admin.site.register(Choice)

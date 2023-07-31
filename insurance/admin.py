from django.contrib import admin
from insurance.models import Category,Policy,PolicyRecord, Question
# Register your models here.
admin.site.register(Category)
admin.site.register(Policy)
admin.site.register(PolicyRecord)
admin.site.register(Question)
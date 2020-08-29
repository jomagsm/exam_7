from django.contrib import admin

from webapp.models import Answer, Quiz

admin.site.register(Quiz)
admin.site.register(Answer)
from django.contrib import admin
from .models import Работник, Посещаемость, Бонус, Задача

admin.site.register(Работник)
admin.site.register(Посещаемость)
admin.site.register(Бонус)
admin.site.register(Задача)

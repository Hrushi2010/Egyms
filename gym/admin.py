from django.contrib import admin

from .models import Category, Program, Trainer, Member

admin.site.register(Category)
admin.site.register(Program)
admin.site.register(Trainer)
admin.site.register(Member)

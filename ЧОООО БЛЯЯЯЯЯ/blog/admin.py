from django.contrib import admin
from .models import Category, Article, CustomUser, Comment
# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username','name','last_name','phone','job')
    list_editable = ('name','last_name','phone','job')

admin.site.register(Category)
admin.site.register(Article)
admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Comment)

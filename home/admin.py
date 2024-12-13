from django.contrib import admin
from .models import *
# from .models import Author, Editor, Reader

# Register your models here.


class PostAdmin(admin.ModelAdmin):
	list_display = ('title','content','created_date','updated_date','status')

admin.site.register(Post, PostAdmin)
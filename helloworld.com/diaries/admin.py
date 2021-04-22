from django.contrib import admin
from .models import Diary
from .models import Category
from .models import CreatedAt
# Register your models here.

admin.site.register(Diary)
admin.site.register(Category)
admin.site.register(CreatedAt)

from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Good)
admin.site.register(Category)
admin.site.register(GoodImages)
admin.site.register(User)
admin.site.register(Order)
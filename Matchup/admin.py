from django.contrib import admin
from .models import User, Language, Interest

# Register your models here.
admin.site.register(User)
admin.site.register(Language)
admin.site.register(Interest)
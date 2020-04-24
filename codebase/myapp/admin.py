from django.contrib import admin

from .models import SignupUser,PostData

# Register your models here.

admin.site.register(SignupUser)
admin.site.register(PostData)
from django.contrib import admin
from .models import Review, ReviewUser
# Register your models here.

admin.site.register(ReviewUser)
admin.site.register(Review)
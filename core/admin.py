from django.contrib import admin

from .models import CustomUser , ActivityPeriod
# Register your models here.
admin.site.register(CustomUser)

admin.site.register(ActivityPeriod)
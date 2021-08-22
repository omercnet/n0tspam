from django.contrib import admin

from .models import RequestLog, Email


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    pass


@admin.register(RequestLog)
class RequestLogAdmin(admin.ModelAdmin):
    pass

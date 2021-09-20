from django.contrib import admin

from .models import RequestLog, Email


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'from_email', 'to_email', "subject")
    list_display_links = ('id', 'created_at', 'to_email',)
    list_filter = ('to_email', 'from_email', 'created_at')
    search_fields = ('to_email', 'from_email', 'subject')


@admin.register(RequestLog)
class RequestLogAdmin(admin.ModelAdmin):
    pass

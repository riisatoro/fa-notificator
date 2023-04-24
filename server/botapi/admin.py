from django.contrib import admin

from botapi.models import UserFANotifications


@admin.register(UserFANotifications)
class UserFANotificationsAdmin(admin.ModelAdmin):
    list_display = (
        'chat_id', 'update_interval', 'previous_notifications', 'updated_at',
    )
    list_filter = ('update_interval',)

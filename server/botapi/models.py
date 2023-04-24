from datetime import timedelta

from django.conf import settings
from django.db.models import (
    CharField,
    DateTimeField,
    DurationField,
    JSONField,
    IntegerField,
    Model,
)


class UserFANotifications(Model):
    chat_id = IntegerField(unique=True, null=False, blank=False)
    cookie_a = CharField(max_length=255, null=False, blank=False)
    cookie_b = CharField(max_length=255, null=False, blank=False)
    update_interval = DurationField(
        default=timedelta(minutes=settings.UPDATE_NOTIFICATION_INTERVAL_MINUTES)
    )
    previous_notifications = JSONField(null=True, blank=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

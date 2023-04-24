from django.contrib import admin
from django.core.management.utils import get_random_secret_key

from authorization.forms import InternalAccessTokenForm
from authorization.models import InternalAccessToken


@admin.register(InternalAccessToken)
class InternalAccessTokenAdmin(admin.ModelAdmin):
    list_display = ('service', 'token', )
    actions = ('update_token', )
    form = InternalAccessTokenForm

    def update_token(modeladmin, request, queryset):
        for model in queryset:
            model.token = get_random_secret_key()
            model.save()

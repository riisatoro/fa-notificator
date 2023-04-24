from django import forms
from django.core.management.utils import get_random_secret_key

from authorization.models import InternalAccessToken


class InternalAccessTokenForm(forms.ModelForm):

    def save(self, commit=True):
        instance = super(InternalAccessTokenForm, self).save(commit=False)
        instance.token = get_random_secret_key()
        instance.save()
        return instance

    class Meta:
        model = InternalAccessToken
        fields = ('service', )
        readonly_fields = ('token', )

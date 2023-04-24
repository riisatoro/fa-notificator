from rest_framework.serializers import ModelSerializer

from botapi.models import UserFANotifications


class UserCookiesSerializer(ModelSerializer):
    class Meta:
        model = UserFANotifications
        fields = (
            'chat_id', 'cookie_a', 'cookie_b',
        )

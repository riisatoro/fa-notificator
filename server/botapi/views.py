from rest_framework import status
from rest_framework.views import APIView, Response

from botapi.models import UserFANotifications
from botapi.serializers import UserCookiesSerializer


class UserProfileView(APIView):

    def put(self, request):
        cookies = UserFANotifications.objects.filter(
            chat_id=request.POST.get('chat_id')
        ).first()

        instance = UserCookiesSerializer(instance=cookies, data=request.POST)
        if instance.is_valid():
            instance.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)

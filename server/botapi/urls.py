from django.urls import path

from botapi.views import UserProfileView


urlpatterns = [
    path('user/', UserProfileView.as_view(), name='add-user'),
    # path('notifications/'),
]

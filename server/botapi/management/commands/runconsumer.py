import json

from django.core.management.base import BaseCommand
import pika

from botapi.models import UserFANotifications
from botapi.serializers import UserCookiesSerializer


class Command(BaseCommand):
    help = 'Run the Django backend consumer to receive messages from bots.'

    def handle(self, *args, **options):
        channel_name = 'botpusher'
        
        connection = pika.BlockingConnection(
            pika.URLParameters('amqp://guest:guest@consumer/')
        )
        channel = connection.channel()
        channel.queue_declare(queue=channel_name)
        
        channel.basic_consume(
            queue=channel_name,
            on_message_callback=self.bot_notification_callback,
        )
        channel.start_consuming()
    
    @staticmethod
    def bot_notification_callback(ch, method, properties, body):
        data = json.loads(body)
        action = data.pop('__action')

        user_info = UserFANotifications.objects.filter(chat_id=data.get('chat_id')).first()
        if action == 'create-user':
            user_info = UserCookiesSerializer(instance=user_info, data=data)
            if user_info.is_valid():
                user_info.save()
        elif action == 'set-interval':
            if user_info:
                user_info.update(interval=int(data.get('interval')))
        elif action == 'delete-user':
            if user_info:
                user_info.delete()

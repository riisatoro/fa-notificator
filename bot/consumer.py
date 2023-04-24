import json

import pika


class RabbitMQConsumer():
    def __init__(self):
        self.channel_name = 'botpusher'
    
        connection = pika.BlockingConnection(
            pika.URLParameters('amqp://guest:guest@consumer/')
        )
        self.channel = connection.channel()
    
    def send_new_user(self, chat_id, cookie_a, cookie_b):
        data = json.dumps({
            '__action': 'create-user',
            'chat_id': chat_id,
            'cookie_a': cookie_a,
            'cookie_b': cookie_b,
        })
        self.channel.basic_publish(
            exchange='',
            routing_key=self.channel_name,
            body=data,
        )

    def set_new_interval(self, chat_id, interval):
        data = json.dumps({
            '__action': 'set-interval',
            'chat_it': chat_id,
            'interval': interval,
        })
        self.channel.basic_publish(
            exchange='',
            routing_key=self.channel_name,
            body=data,
        )

    def delete_user(self, chat_id):
        data = json.dumps({
            '__action': 'delete-user',
            'chat_id': chat_id,
        })
        self.channel.basic_publish(
            exchange='',
            routing_key=self.channel_name,
            body=data,
        )

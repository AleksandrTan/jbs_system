import pika

import config


class RabbitWorker:
    def __init__(self):
        super().__init__()
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=config.RABBIT_HOST))
        self.channel = self.connection.channel()

    def sender(self, data):
        self.channel.queue_declare(queue="target")
        self.channel.basic_publish(exchange='', routing_key='target', body=data)
        print(" [x] Sent 'Hello World!'")
        self.channel.close()
        self.connection.close()


if __name__ == "__main__":
    worker = RabbitWorker()
    worker.sender("Hello Alex 3500!!!")

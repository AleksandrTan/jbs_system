import json
import pika

import config


class RabbitWorker:
    def __init__(self):
        super().__init__()
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=config.RABBIT_HOST,
                                                                            port=config.RABBIT_PORT))
        self.channel = self.connection.channel()

    def sender(self, data):
        self.channel.queue_declare(queue=config.QUEUE_NAME)
        self.channel.basic_publish(exchange='', routing_key='target', body=data)
        print(" [x] Sent 'Hello World 1!'")
        self.channel.close()
        self.connection.close()


if __name__ == "__main__":
    worker = RabbitWorker()
    message = json.dumps(
        {
            "status": True,
            "link": "http://127.0.0.1:8000/mspanel/testpage/",
            "order_id": 3500,
            "file_path": "http://127.0.0.1:8000/filedownload/",
            "name": "Alex",
            "last_name": "Tan",
            "email": "test@gmail.com",
            "proxy": {
                "proxy_id": 1,
                "host": "138.219.173.58",
                "port": 8000,
                "protocol": "http",
                "username": '2DxLL0',
                "password": 'fwcZsa'
            }
        }
    )
    worker.sender(message)

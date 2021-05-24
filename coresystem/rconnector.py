import json

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
        print(" [x] Sent 'Hello World 1!'")
        self.channel.close()
        self.connection.close()


if __name__ == "__main__":
    worker = RabbitWorker()
    # message = json.dumps(
    #     {
    #         "status": True,
    #         "link": "https://www.careerbuilder.com/job/JD68096636KLHPD352T",
    #         "order_id": 3500
    #     }
    # )

    message = json.dumps(
        {
            "status": True,
            "link": "http://127.0.0.1:8000/mspanel/testpage/",
            "order_id": 3500,
            "file_path": "http://127.0.0.1:8000/filedownload/",
            "name": "Alex",
            "last_name": "Tan",
            "email": "test@gmail.com"
        }
    )
    worker.sender(message)

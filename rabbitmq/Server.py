import pika
from pika.spec import Exchange

class RabbitMqConfig:
    def __init__(self,queue:str ="flask" ,host:str ="localhost",routing_key:str ="flask") -> None:
        self.queue = queue
        self.host = host
        self.routing_key = routing_key

class ServerMq:
    def __init__(self,config: RabbitMqConfig) -> None:
        self.config = config
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(self.config.host))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.config.queue)

    def publish(self,message:str):
        self.channel.basic_publish(exchange='',
            routing_key = self.config.routing_key,
            body = message)
        print(f"Message Sent to RabbitMq with routing key {self.config.routing_key}")
        #self.connection.close()
        #print("Connection Closed")
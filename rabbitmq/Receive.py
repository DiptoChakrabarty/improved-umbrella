import pika

class RabbitMqConfig:
    def __init__(self,queue:str ="flask" ,host:str ="localhost",routing_key:str ="flask") -> None:
        self.queue = queue
        self.host = host
        self.routing = routing

class ReceiveMq:
    def __init__(self,config: RabbitMqConfig) -> None:
        self.config = config
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            host = self.config.host
        ))
        self.channel = self.connection.channel
        self.channel.queue_declare(queue=self.config.queue)
    
    def consume(self):
        self.channel.basic_consume(queue=self.config.routing,
        on_message_callback=ReceiveMq.callback,
        auto_ack = True)
        print("Waiting for messages\n")
        self.channel.start_consuming()

    @staticmethod
    def callback(ch,method,properties,body):
        print("Message Received",body)


        
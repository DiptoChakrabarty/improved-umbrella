import pika
from rabbitmq.Rabbitmq import RabbitMqConfig,ReceiveMq

config = RabbitMqConfig()
connection = pika.BlockingConnection(pika.ConnectionParameters(
            host = config.host
        ))
channel = connection.channel()
channel.queue_declare(queue=config.queue)

def mail_func(ch,method,properties,body):
    print("This is Message Received\n")
    print(body,"\n")

if __name__=="__main__":
    channel.basic_consume(on_message_callback=mail_func,queue=config.queue)
    channel.start_consuming()
    #receiver.start_consuming()



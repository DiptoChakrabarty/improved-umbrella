from rabbitmq.Rabbitmq import RabbitMqConfig,ReceiveMq

config = RabbitMqConfig()
receiver = ReceiveMq(config)

def mail_func(ch,method,properties,body):
    print("This is Message Received\n")
    print(body,"\n")

if __name__=="__main__":
    try:
        receiver.consume(mail_func)
    except KeyboardInterrupt:
        print("Program Terminated")
    #receiver.start_consuming()



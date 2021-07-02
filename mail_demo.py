import os
import json
import smtplib
from itsdangerous import URLSafeTimedSerializer, serializer
from rabbitmq.Rabbitmq import RabbitMqConfig,ReceiveMq
from dotenv import load_dotenv
load_dotenv()

config = RabbitMqConfig()
receiver = ReceiveMq(config)

USERNAME = os.environ.get("USEREMAIL")
PASSWORD = os.environ.get("PASSWORD")
print(USERNAME,PASSWORD)
mail_server = smtplib.SMTP("smtp.gmail.com",587)
mail_server.starttls()
mail_server.login(USERNAME,PASSWORD)
print("Logged into Mail Server")

def mail_func(ch,method,properties,body):
    print("This is Message Received\n")
    print(body,"\n")
    data = json.loads(body)
    print(data,data["email"])
    subject = "Sample Email"
    token = generate_token(data["email"])
    URL = "http://localhost:5000/confirm/" + token
    message = f"Subject: {subject}\n\nHello User with Email for confirmation {URL} "
    mail_server.sendmail(USERNAME,data["email"],message)

def generate_token(email: str):
    serializer = URLSafeTimedSerializer(os.environ.get("SECRET_KEY"))
    return serializer.dumps(email,salt=os.environ.get("SALT_KEY"))

if __name__=="__main__":
    try:
        receiver.consume(mail_func)
    except KeyboardInterrupt:
        print("Program Terminated")
    #receiver.start_consuming()



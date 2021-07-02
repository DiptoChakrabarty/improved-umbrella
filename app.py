import json
from flask import Flask, json,request,jsonify,make_response
from itsdangerous import URLSafeTimedSerializer, exc, serializer
from rabbitmq.Rabbitmq import RabbitMqConfig,ServerMq

app = Flask(__name__)
config = RabbitMqConfig()
server = ServerMq(config)
#server.publish("Hello")

@app.get("/")
def home():
    return "Server Up and Running"

@app.post("/")
def add():
    data = request.get_json()
    message = json.dumps(data)
    print(message)
    print("Sending to RabbitMq")
    server.publish(message)
    return make_response(jsonify(
        {
            "Msg": "msg received",
            "Status": 200
        }
    ),200)

@app.get("/confirm/<str:token>")
def verify(token:str):
    serializer = URLSafeTimedSerializer(os.environ.get("SECRET_KEY"))
    try:
        email = serializer.loads(
            token,
            salt = os.environ.get("SALT_KEY")
        )
    except:
        return False
    
    return email







if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0")
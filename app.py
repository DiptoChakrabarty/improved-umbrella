import json
from flask import Flask, json,request,jsonify,make_response
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






if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0")
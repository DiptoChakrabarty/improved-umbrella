from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return "Server Up and Running"


if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0")
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api()
db = SQLAlchemy()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://user.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


@app.before_first_request
def create_tables():
    db.create_all()


if __name__=="__main__":
    api.init_app(app)
    db.init_app(app)
    app.run(debug=True,host="0.0.0.0")
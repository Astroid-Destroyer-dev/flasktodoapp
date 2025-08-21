from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(BASE_DIR, "todo.db")
db = SQLAlchemy(app)


class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    des = db.Column(db.String(300), nullable=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"{self.sno} - {self.title}"


@app.route("/")
def Home():
    todo = Todo(title="sexy_title", des="sexy des")
    db.session.add(todo)
    db.session.commit()
    all_todo = db.Query.all()
    return render_template("index.html", all_todo="all_todo")


if __name__ == "__main__":
    # Ensure database/tables are created
    with app.app_context():
        db.create_all()
    app.run(debug=True)

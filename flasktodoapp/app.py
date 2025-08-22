from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(BASE_DIR, "todo.db")
db = SQLAlchemy(app)


class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    des = db.Column(db.String(300), nullable=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"{self.sno} - {self.title}"


@app.route("/", methods = ['GET','POST'])
def Home():
    if request.method == 'POST':
        title = request.form.get('title')
        des = request.form.get('des')
        todo = Todo(title = title,des = des)
        db.session.add(todo)
        db.session.commit()
        

    all_todo = Todo.query.all()
    return render_template("index.html", all_todo = all_todo)

@app.route("/delete/<int:sno>")
def delete(sno):
    todo = Todo.query.filter_by(sno = sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")

@app.route("/update/<int:sno>", methods = ['POST','GET'])
def update(sno):
    todo = Todo.query.filter_by(sno = sno).first()
    if request.method == 'POST':
        title = request.form.get('title')
        des = request.form.get("des")
        todo = Todo.query.filter_by(sno = sno).first()
        todo.title = title
        todo.des = des
        db.session.add(todo)
        db.session.commit()
        return redirect("/")
    return render_template("update.html", todo = todo)

if __name__ == "__main__":
    app.run(debug=True)

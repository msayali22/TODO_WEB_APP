from flask import Flask,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class Todo(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	title=db.Column(db.String(100))
	complete=db.Column(db.Boolean)
	
@app.route('/home')
def show_homepage():
	todo_list=Todo.query.all()
	page=render_template("home.html",todo_list=todo_list)
	return page
	
@app.route("/")
def home():
	return redirect(url_for('show_homepage'))
    
@app.route("/add_task",methods=["POST"])
def add_task():
	title=request.form.get("title")
	new_todo=Todo(title=title,complete=False)
	db.session.add(new_todo)
	db.session.commit()
	return redirect(url_for("home"))
	
@app.route("/update/<int:todo_id>")
def update(todo_id):
	todo=Todo.query.filter_by(id=todo_id).first()
	todo.complete=not todo.complete
	db.session.commit()
	return redirect(url_for("home"))
	
@app.route("/delete/<int:todo_id>")
def delete(todo_id):
	todo=Todo.query.filter_by(id=todo_id).first()
	db.session.delete(todo)
	db.session.commit()
	return redirect(url_for("home"))
#base--home.html		
@app.route('/logout')
def logout():
	session.pop('username',None)
	return redirect(url_for('show_homepage'))

if __name__=='__main__':
	app.run(host="0.0.0.0",port=50000)
	
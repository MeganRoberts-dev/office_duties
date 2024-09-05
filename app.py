import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from bson.objectid import ObjectId

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)
bcrypt = Bcrypt(app)

@app.route('/test-data')
def test_data():
    tasks = mongo.db.tasks.find()
    return render_template('test_data.html', tasks=tasks)


@app.route('/')
def home():
    if 'user' in session:
        tasks = mongo.db.tasks.find({"user": session["user"]})
        return render_template('home.html', tasks=tasks)
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if mongo.db.users.find_one({"username": username}):
            flash('Username already exists. Please log in.', 'danger')
            return redirect(url_for('login'))

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        mongo.db.users.insert_one({"username": username, "password": hashed_password})
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = mongo.db.users.find_one({"username": username})

        if user and bcrypt.check_password_hash(user["password"], password):
            session['user'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login failed. Check your username and/or password.', 'danger')

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user')
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))


@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.form.get('task')
    mongo.db.tasks.insert_one({"task": task, "user": session["user"]})
    flash('Task added!', 'success')
    return redirect(url_for('home'))


@app.route('/delete_task/<task_id>')
def delete_task(task_id):
    mongo.db.tasks.delete_one({"_id": ObjectId(task_id)})
    flash('Task deleted!', 'info')
    return redirect(url_for('home'))


@app.route('/complete_task/<task_id>')
def complete_task(task_id):
    task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    if task:
        mongo.db.tasks.update_one({"_id": ObjectId(task_id)}, {"$set": {"completed": not task.get("completed", False)}})
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(host=os.environ.get("IP"), port=int(os.environ.get("PORT")))

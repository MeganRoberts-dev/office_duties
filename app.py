import os
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from flask import (
    Flask, render_template,
    Flask, render_template,
    request, redirect, url_for, session, flash
)

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route('/')
def home():
    if 'user' in session:
        user = mongo.db.users.find_one({"username": session["user"]})["_id"]
        duties = list(mongo.db.duties.find({"owner": user}))
        return render_template('home.html', duties=duties)
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {'username': request.form.get('username').lower()})

        if existing_user:
            flash('Username already exists', 'danger')
            return redirect(url_for('register'))

        new_user = {
            'username': request.form.get('username').lower(),
            'password': generate_password_hash(request.form.get('password'))
        }
        mongo.db.users.insert_one(new_user)

        # put the new user into 'session' cookie
        session['user'] = request.form.get('username').lower()
        flash('Registration Successful!')
        return redirect(url_for('profile', username=session['user']))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username').lower()
        password = request.form.get('password')

        existing_user = mongo.db.users.find_one({'username': username})

        if existing_user:

            if check_password_hash(existing_user['password'], password):
                session['user'] = username
                return redirect(url_for('home'))
            else:
                flash('Incorrect Username and/or Password', 'danger')
        else:
            flash('Incorrect Username and/or Password', 'danger')

        return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/profile/<username>', methods=['GET', 'POST'])
def profile(username):
    username = mongo.db.users.find_one(
        {'username': session['user']})['username']

    if 'user' in session:
        return render_template('profile.html', username=username)

    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('user')
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))


@app.route('/add_duty', methods=['GET', 'POST'])
def add_duty():
    if request.method == 'POST':
        user_id = mongo.db.users.find_one({'username': session['user']})['_id']
        completed = True if request.form.get('completed') else False
        duty = {
            'title': request.form.get('title'),
            'description': request.form.get('description'),
            'completed': completed,
            'owner': ObjectId(user_id)
        }
        mongo.db.duties.insert_one(duty)
        flash('Duty Successfully Added', 'info')
        return redirect(url_for('home'))

    return render_template('add_duty.html')


@app.route('/edit/<duty_id>', methods=['GET', 'POST'])
def edit_duty(duty_id):
    duty = mongo.db.duties.find_one({"_id": ObjectId(duty_id)})
    if not duty:
        flash("Duty not found.", "danger")
        return redirect(url_for('home'))

    owner = mongo.db.users.find_one({"_id": ObjectId(duty["owner"])})

    if owner and session.get("user") == owner["username"]:
        if request.method == 'POST':
            completed = True if request.form.get('completed') else False
            update_data = {
                'title': request.form.get('title'),
                'description': request.form.get('description'),
                'completed': completed
            }
            mongo.db.duties.update_one(
                {"_id": ObjectId(duty_id)},
                {"$set": update_data})
            flash('Duty Updated Successfully', 'success')
            return redirect(url_for('home'))

        return render_template('edit_duty.html', duty=duty)

    flash('Access Denied - Invalid User', 'danger')
    return redirect(url_for('home'))


@app.route('/delete_duty/<duty_id>', methods=['POST'])
def delete_duty(duty_id):
    duty = mongo.db.duties.find_one({"_id": ObjectId(duty_id)})
    owner = mongo.db.users.find_one(
        {"_id": ObjectId(duty["owner"])})["username"]

    if session["user"] == owner:
        mongo.db.duties.delete_one({"_id": ObjectId(duty_id)})
        flash('Duty deleted successfully!', 'success')
    else:
        flash('Access Denied - Invalid User', 'danger')

    return redirect(url_for('home'))


@app.route('/complete_duty/<duty_id>', methods=['POST'])
def complete_duty(duty_id):
    duty = mongo.db.duties.find_one({"_id": ObjectId(duty_id)})
    owner = mongo.db.users.find_one(
        {"_id": ObjectId(duty["owner"])})["username"]

    if session["user"] == owner:
        mongo.db.duties.update_one(
            {'_id': ObjectId(duty_id)},
            {'$set': {'completed': True}}
        )
        flash('Duty marked as completed!', 'success')
        return redirect(url_for('home'))

    flash('Access Denied - Invalid User', 'danger')
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG", True)
    )

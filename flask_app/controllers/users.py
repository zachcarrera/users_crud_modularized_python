from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import User


# page to show all user in a table
@app.route("/")
@app.route("/users")
def show_all():
    
    # query the db to get all users
    users = User.get_all()
    return render_template("all_users.html", users = users)


# page with a form to create a new user
@app.route("/users/new")
def new_user():
    return render_template("create_user.html")


# form submission to create user and redirect
@app.route("/create_user", methods=["POST"])
def create_user():
    user_id = User.save(request.form)
    return redirect(f"/users/{user_id}")


# page with form to update user info
@app.route("/users/edit/<int:user_id>")
def edit_user(user_id):

    # query to get info of a user
    user = User.get_one(user_id)
    return render_template("edit_user.html", user = user)


# form submission to update user info
@app.route("/update_user", methods=["POST"])
def update_user():
    # update query to db 
    User.update(request.form)
    return redirect(f"/users/{request.form['id']}")


# page to display info on a given user
@app.route("/users/<int:user_id>")
def show_user(user_id):

    # query the db to get info on one user
    user = User.get_one(user_id)
    return render_template("show_one.html", user = user)


# delete user path
@app.route("/users/destroy/<int:user_id>")
def destroy(user_id):

    # query db to delete a specific user
    User.delete(user_id)
    return redirect("/users")

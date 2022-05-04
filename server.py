from flask import Flask, redirect, render_template, request, session
from users import User
app = Flask(__name__)

app.secret_key = "Justw0rk!"

@app.route("/")
def index():
    users = User.get_all_users()
    print(users)
    return render_template("index.html", all_users = users)

@app.route("/add_user")
def add_user_page():
    return render_template("add_user.html")

@app.route("/create_user", methods=['post'])
def create_user():
    user = User.create(request.form)
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)
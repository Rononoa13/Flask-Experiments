from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5432/login"
app.config["SECRET_KEY"] = "thisissecret"

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)

@login_manager.user_loader
def  load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
   user = User.query.filter_by(username="Sumit").first()
   login_user(user)
   return "You are now logged in"


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return "Yout are now logged out"

@app.route('/home')
@login_required
def home():
   return "The current usename is " + current_user.username


if __name__ == "__main__":
    app.run(debug=True)
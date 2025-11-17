from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, login_required,current_user
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'
login_manager.login_message = "Veuillez vous connecter pour accéder à cette page."

from models.user import User
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)
from routes.auth import auth_bp
from routes.profil import profil_bp
from routes.notes import notes_bp
from routes.contacts import contacts_bp

app.register_blueprint(auth_bp)
app.register_blueprint(profil_bp)
app.register_blueprint(notes_bp)
app.register_blueprint(contacts_bp)
@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('profil.dashboard'))
    return redirect(url_for('auth.login'))
if __name__ == '__main__':
    app.run(debug=True)

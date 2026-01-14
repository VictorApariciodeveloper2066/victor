from flask import Blueprint, render_template, session, redirect, url_for

front_bp = Blueprint('front', __name__)

@front_bp.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('front.dashboard'))
    return render_template('index.html')

@front_bp.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('front.index'))
    return render_template('dashboard.html', username=session['username'])

@front_bp.route('/login')
def login_page():
    return render_template('login.html')

@front_bp.route('/register')
def register_page():
    return render_template('register.html')

@front_bp.route('/predashboard')
def predashboard():
    return render_template('predashboard.html')

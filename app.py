from backend.extensions import db, cors, migrate
from backend.routes.auth import auth_bp
from flask import Flask
from backend.routes.auth import auth_bp
from backend.routes.front import front_bp
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()
APP_DIR = Path(__file__).resolve().parent

def create_app():
    app = Flask(
        __name__,
        template_folder=str(APP_DIR / 'frontend' / 'templates'),
        static_folder=str(APP_DIR / 'frontend' / 'static' / 'assets'),
        static_url_path='/static'
    )

    app.secret_key = os.getenv('FLASK_SECRET_KEY', 'supersecretkey')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    cors.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(front_bp)
    app.register_blueprint(auth_bp)


    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

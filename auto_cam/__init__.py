from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM 초기화
    db.init_app(app)
    migrate.init_app(app, db)
    from auto_cam.model import models

    with app.app_context():
        db.create_all()

    # 블루프린트 등록
    from auto_cam.views import main_views
    app.register_blueprint(main_views.views_blueprint)

    return app
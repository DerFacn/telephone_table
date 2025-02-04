from flask import Flask, render_template
from app.config import Config
from flask_basicauth import BasicAuth
from alchemical.flask import Alchemical

basic_auth = BasicAuth()
db = Alchemical()


def create_app(config_obj=Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_obj)

    basic_auth.init_app(app)
    db.init_app(app)


    @app.route('/')
    def index():
        return render_template('index.html')
    
    from app.cli import data
    from app import models

    app.cli.add_command(data)

    with app.app_context():
        db.create_all()

        for city_name in app.config.get('CITIES'):
            city = db.session.scalar(
                models.City.select().filter_by(name=city_name)
            )

            if not city:
                new_city = models.City(name=city_name)
                db.session.add(new_city)
        
        db.session.commit()

    return app

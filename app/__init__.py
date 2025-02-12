from flask import Flask, render_template
from app.config import Config
from flask_basicauth import BasicAuth
from alchemical.flask import Alchemical
from flask_babel import Babel

from flask_admin import Admin

basic_auth = BasicAuth()
db = Alchemical()
babel = Babel()


def create_app(config_obj=Config) -> Flask:
    # Creating Flask instance
    app = Flask(__name__)
    app.config.from_object(config_obj)

    # Initialisation
    basic_auth.init_app(app)
    db.init_app(app)
    babel.init_app(app, default_locale='de')
    
    # Importing important modules
    from app.cli import data
    from app import models
    from app.routes import index, import_excel
    from app.panel import ProtectedAdminIndexView, register_views

    # Registering cli commands and some routes
    app.add_url_rule('/', 'index', index, methods=['GET'])
    app.add_url_rule('/import-excel', 'import_excel', import_excel, methods=['POST'])
    app.cli.add_command(data)
    
    admin = Admin(
        app=app,
        name='BBZ Telefon Tabelle',
        url='/panel',
        index_view=ProtectedAdminIndexView(name='Home', template='home.html', url='/panel'),
        template_mode='bootstrap4',
    )

    with app.app_context():
        db.create_all()
        register_views(admin, db.session) # Registering all admin model views

        for city_name in app.config.get('CITIES'):
            city = db.session.scalar(
                models.City.select().filter_by(name=city_name)
            )

            if not city:
                new_city = models.City(name=city_name)
                db.session.add(new_city)
        
        db.session.commit()

    return app

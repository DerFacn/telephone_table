from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from app.models import City, Entrie, Building
from app import basic_auth
from app.utils import get_all


class ProtectedAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        all_cities = list(get_all(
          City.select()
        ))

        cities = [city.name for city in all_cities]
        
        return self.render('home.html', cities=cities)
    
    def is_accessible(self):
        if not basic_auth.authenticate():
            return False
        else:
            return True
        
    def inaccessible_callback(self, name, **kwargs):
        return basic_auth.challenge()
    

class ProtectedModelView(ModelView):
    def is_accessible(self):
        if not basic_auth.authenticate():
            return False
        else:
            return True
        
    def inaccessible_callback(self, name, **kwargs):
        return basic_auth.challenge()

from .views import CitiesModelView, EntriesModelView, BuildingsModelView

def register_views(admin: Admin, session):
    admin.add_view(
        CitiesModelView(
            City,
            session,
            'Städte',
            url='cities',
        )
    )
    admin.add_view(
        BuildingsModelView(
            Building,
            session,
            'Gebäude',
            url='buildings'
        )
    )
    admin.add_view(
        EntriesModelView(
            Entrie,
            session,
            'Einträge',
            url='entries'
        )
    )

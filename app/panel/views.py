from . import ProtectedModelView
from app.utils import get_all, get_first
from app.models import City, Building
from wtforms.fields import SelectField
from wtforms.validators import DataRequired
from markupsafe import Markup


def _display_city(view, context, model, name):
    return model.city.name if model.city else '—'


def _display_building(view, context, model, name):
    return model.gebaeude.name if model.gebaeude else '—'


def _copyable_number(view, context, model, name):
    return Markup(
        f'''
        <p 
        onclick="
            navigator.clipboard.writeText(this.innerText);
            alert('Copied the text: ' + this.innerText);" 
        onMouseOver="this.style.color='#565656'" 
        onMouseOut="this.style.color='#000'"
        style="cursor: pointer; display: inline-block;" title="Click to copy">{ model.nummer }</p>
        '''
    )


class CitiesModelView(ProtectedModelView):
    page_size = 50
    column_list = ('name',)
    column_searchable_list = ['name']

    column_labels = {
        "name": "Stadt"
    }


class BuildingsModelView(ProtectedModelView):
    page_size = 50
    column_list = ('name',)
    column_searchable_list = ['name']


class EntriesModelView(ProtectedModelView):
    page_size = 75
    column_list = ('name', 'nummer', 'funktion', 'raumnummer', 'city', 'gebaeude')
    column_searchable_list = ['name', 'nummer', 'funktion', 'raumnummer']

    form_columns = ['name', 'nummer', 'funktion', 'raumnummer', 'city', 'gebaeude']

    column_labels = {
        "name": "Name/Bezeichnung",
        "nummer": "Nummer",
        "funktion": "Funktion",
        "gebaeude": "Gebäude",
        "raumnummer": "Raumnummer"
    }

    column_formatters = {
        "nummer": _copyable_number,
        "city": _display_city,
        "gebaeude": _display_building
    }

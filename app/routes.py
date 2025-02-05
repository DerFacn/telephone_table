from app import db
from app.models import Entrie, City
from app.utils import get_all
from flask import render_template


def index():
    all_entries = list(get_all(
        Entrie.select()
    ))

    entries = [{
        'city': entry.city.name,
        'name': entry.name if entry.name else '—',
        'nummer': entry.nummer if entry.nummer else '—',
        'funktion': entry.funktion if entry.funktion else '—',
        'gebaeude': entry.gebaeude if entry.gebaeude else '—',
        'raumnummer': entry.raumnummer if entry.raumnummer else '—'
    } for entry in all_entries]

    return render_template('index.html', entries=entries)

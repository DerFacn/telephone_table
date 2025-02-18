import pandas
from app import db, basic_auth
from app.models import Entrie, City, Building
from app.utils import get_all, get_first
from flask import render_template, request, redirect, url_for, flash, make_response


def index():
    all_entries = list(get_all(
        Entrie.select()
    ))

    entries = [{
        'city': entry.city.name if entry.city else '—',
        'name': entry.name if entry.name else '—',
        'nummer': entry.nummer if entry.nummer else '—',
        'personal_nummer': entry.personal_nummer if entry.personal_nummer else '—',
        'funktion': entry.funktion if entry.funktion else '—',
        'gebaeude': entry.gebaeude.name if entry.gebaeude else '—',
        'raumnummer': entry.raumnummer if entry.raumnummer else '—'
    } for entry in all_entries]

    return render_template('index.html', entries=entries)


@basic_auth.required
def import_excel():
    file = request.files.get('excel')
    city_name = request.form.get('city')

    if not file or file.filename == "":
        return redirect(url_for('admin.index'))

    filename = file.filename
    filetype = filename.rsplit('.', 1)[1]

    if filetype != 'xlsx':
        flash('File must be in .xlsx format!', 'danger')
        return redirect(url_for('admin.index'))
    
    columns = {
        'name': 'Name/Bezeichnung',
        'nummer': 'Nummer',
        'funktion': 'Funktion',
        'gebaeude': 'Gebäude',
        'raumnummer': 'Raumnummer'
    }
    
    # Choosing the city
    city = get_first(
        City.select().filter_by(name=city_name)
    )

    if not city:
        flash('Choosed city does not exist!', 'danger')
        return redirect(url_for('admin.index'))

    # Opening the table
    df = pandas.read_excel(file.stream)

    values = df[columns.values()].values

    # Parsing data
    for row in values.tolist():
        item = dict(zip(columns.keys(), row))

        new_entrie = Entrie(city_id=city.id)

        for column, value in item.items():
            if column == 'gebaeude':
                if type(value) != float:
                    building = get_first(
                        Building.select().filter_by(name=value.strip())
                    )    

                    if not building:
                        building = Building(name=value.strip())
                        db.session.add(building)
                        db.session.flush()

                    setattr(new_entrie, 'gebaeude_id', building.id)
                continue

            # Handle NaN or missing values, ensure the value is a string
            if value is None or (isinstance(value, float) and pandas.isna(value)):
                value = ""  # Default to an empty string if NaN or None
            
            # Ensure the value is treated as a string
            value = str(value).strip()

            setattr(new_entrie, column, value)

        db.session.add(new_entrie)
    
    db.session.commit()

    flash('Table successfully imported!', 'success')

    return redirect(url_for('admin.index'))


import click
import pandas
from app import db
from app.models import Entrie, City
from app.utils import get_all, get_first


@click.group(help='Manage data')
def data():
    pass


@data.command('erase-all', help='Clean entries table')
def erase_all():
    results = get_all(
        Entrie.select()
    )

    for entry in results:
        db.session.delete(entry)

    db.session.commit()

    click.echo('Entry table completely erased!')


@data.command('import-from-excel', help='Import data from excel.')
def import_from_excel():
    path_to_excel = click.prompt('Enter path to excel file')
    columns = {
        'name': 'Name/Bezeichnung',
        'nummer': 'Nummer',
        'funktion': 'Funktion',
        'gebaeude': 'Gebäude',
        'raumnummer': 'Raumnummer'
    }
    
    # Choosing the city
    cities_results = list(get_all(
        City.select()
    ))

    city = None

    while not city:
        city_name = click.prompt(f'Choose the city {[city_.name for city_ in cities_results]}')

        for city_ in cities_results:
            if city_.name == city_name:
                city = city_
                break

    # Opening the table
    df = pandas.read_excel(path_to_excel)

    values = df[columns.values()].values

    for row in values.tolist():
        item = dict(zip(columns.keys(), row))

        new_entrie = Entrie(city_id=city.id)

        for column, value in item.items():
            setattr(new_entrie, column, value)

        db.session.add(new_entrie)
    
    db.session.commit()

    click.echo('Successfully imported!')

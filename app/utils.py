from app import db


def get_all(query): return db.session.scalars(query)


def get_first(query):
    result = db.session.scalar(query)
    return result if result else False

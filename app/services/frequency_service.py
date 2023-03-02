from app import db
from app.models import Frequency


def create_frequency(frequency):
    db.session.add(frequency)
    db.session.commit()


def get_frequencies():
    return Frequency.query.all()


def get_frequency_id(frequency_id):
    return Frequency.query.get(frequency_id)


def update_frequency(old_frequency, new_frequency):
    old_frequency.description = new_frequency.description
    db.session.commit()


def delete_frequency(frequency):
    db.session.delete(frequency)
    db.session.commit()

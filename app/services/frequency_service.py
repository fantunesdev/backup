from app.models import Frequency


def get_frequencies():
    return Frequency.query.all()


def get_frequency_id(frequency_id):
    return Frequency.query.get(frequency_id)

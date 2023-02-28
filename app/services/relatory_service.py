from datetime import date

from sqlalchemy import cast, Date

from app.models import Relatory


def get_relatories():
    return Relatory.query.all()


def get_relatory_by_day(day):
    return Relatory.query \
        .filter(cast(Relatory.date, Date) == day) \
        .all()


def get_relatory_by_week(week):
    return Relatory.query.all()


def get_relatory_id(relatory_id):
    return Relatory.query.get(relatory_id)

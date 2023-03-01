from datetime import date

from sqlalchemy import cast, Date, extract

from app.models import Relatory


def get_relatories():
    return Relatory.query.all()


def get_relatory_by_day(day):
    return Relatory.query \
        .filter(cast(Relatory.date, Date) == day) \
        .join(Relatory.backup_obj) \
        .filter_by(frequency=1) \
        .all()


def get_relatory_by_week(year, week):
    return Relatory.query \
        .filter(
            extract('week', Relatory.date) == week,
            extract('year', Relatory.date) == year
        ) \
        .join(Relatory.backup_obj) \
        .filter_by(frequency=3) \
        .all()


def get_relatory_id(relatory_id):
    return Relatory.query.get(relatory_id)

from datetime import date, datetime, timedelta

from flask import render_template

from app import app
from app.repositories import relatory_repository
from app.services import relatory_service


@app.route('/relatorios')
def get_relatories():
    relatories = relatory_service.get_relatories()
    return render_template('relatory/get_relatories.html', relatories=relatories)


@app.route('/sincronizacao')
@app.route('/diario')
@app.route('/')
def get_relatory_today():
    today = date.today()
    relatories = relatory_service.get_relatory_by_day(today)
    matrix = relatory_repository.templatetags_assembler(relatories)
    success_fails = relatory_repository.get_success_fail_number(relatories)
    next_day = today + timedelta(days=1)
    last_day = today - timedelta(days=1)
    return render_template(
        'relatory/get_relatories_dayly.html',
        relatories=relatories,
        matrix=matrix,
        success=success_fails['success'],
        fails=success_fails['fails'],
        date=today.strftime('%d/%m/%Y'),
        day=today.day,
        next_day=next_day,
        last_day=last_day
    )


@app.route('/diario/<string:day>')
def get_relatory_by_day(day):
    relatories = relatory_service.get_relatory_by_day(day)
    matrix = relatory_repository.templatetags_assembler(relatories)
    success_fails = relatory_repository.get_success_fail_number(relatories)
    next_day = datetime.strptime(day, '%Y-%m-%d').date() + timedelta(days=1)
    last_day = datetime.strptime(day, '%Y-%m-%d').date() - timedelta(days=1)
    return render_template(
        'relatory/get_relatories_dayly.html',
        relatories=relatories,
        matrix=matrix,
        success=success_fails['success'],
        fails=success_fails['fails'],
        date=day,
        next_day=next_day,
        last_day=last_day
    )


@app.route('/semana', defaults={'year': None, 'week': None})
@app.route('/ano/<int:year>/semana/<int:week>')
@app.route('/semanal')
def get_week(year, week):
    if not week:
        week = date.today().isocalendar()[1]
    if not year:
        year = date.today().year
    print(year, week)
    relatories = relatory_service.get_relatory_by_week(year, week)
    success_fails = relatory_repository.get_success_fail_number(relatories)
    last_week = date.fromisocalendar(year, week, 1) - timedelta(weeks=1)
    next_week = date.fromisocalendar(year, week, 1) + timedelta(weeks=1)
    print(last_week, next_week)
    return render_template(
        'relatory/get_relatories.html',
        relatories=relatories,
        success=success_fails['success'],
        fails=success_fails['fails'],
        year=year,
        week=week,
        last_week=last_week.isocalendar()[1],
        next_week=next_week.isocalendar()[1],
        last_week_year=last_week.year,
        next_week_year=next_week.year
    )


@app.route('/relatorios/<int:relatory_id>')
def get_relatory_id(relatory_id):
    relatory = relatory_service.get_relatory_id(relatory_id)
    return render_template('relatory/detail_relatory.html', relatory=relatory)

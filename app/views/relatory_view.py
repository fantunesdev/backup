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


@app.route('/semanal', defaults={'week': None})
@app.route('/semanal/<int:week>')
def get_week(week):
    if not week:
        week = date.today().isocalendar()[1]
    relatories = relatory_service.get_relatory_by_week(week)
    success_fails = relatory_repository.get_success_fail_number(relatories)
    return render_template(
        'relatory/get_relatories.html',
        relatories=relatories,
        success=success_fails['success'],
        fails=success_fails['fails'],
        week=week
    )


@app.route('/relatorios/<int:relatory_id>')
def get_relatory_id(relatory_id):
    relatory = relatory_service.get_relatory_id(relatory_id)
    return render_template('relatory/detail_relatory.html', relatory=relatory)

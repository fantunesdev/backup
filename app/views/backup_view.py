import datetime

from flask import render_template, redirect, url_for, request

from app import app
from app.forms import backup_form
from app.models import Backup
from app.services import backup_service


@app.route('/backups/create', methods=['GET', 'POST'])
def create_backup():
    form_backup = backup_form.BackupForm()
    if form_backup.validate_on_submit():
        new_backup = Backup(
            description=form_backup.description.data,
            source=form_backup.source.data,
            target=form_backup.target.data,
            program=form_backup.program.data,
            options=form_backup.options.data,
            frequency=form_backup.frequency.data,
        )
        backup_service.create_backup(new_backup)
        return redirect(url_for('configure_settings'))
    return render_template('backup/form_backup.html', form_backup=form_backup)


@app.route('/backups')
def get_backups():
    backups = backup_service.get_backups()
    return render_template('backup/get_backups.html', backups=backups)


@app.route('/backups/<int:backup_id>')
def get_backup_id(backup_id):
    backup = backup_service.get_backup_id(backup_id)
    return render_template('backup/detail_backup.html', backup=backup)


@app.route('/backups/update/<int:backup_id>', methods=['GET', 'POST'])
def update_backup(backup_id):
    old_backup = backup_service.get_backup_id(backup_id)
    form_backup = backup_form.BackupForm(obj=old_backup)
    if form_backup.validate_on_submit():
        new_backup = Backup(
            description=form_backup.description.data,
            source=form_backup.source.data,
            target=form_backup.target.data,
            program=form_backup.program.data,
            options=form_backup.options.data,
            frequency=form_backup.frequency.data,
        )
        backup_service.update_backup(old_backup, new_backup)
        return redirect(url_for('configure_settings'))

    return render_template('backup/form_backup.html', form_backup=form_backup)


@app.route('/backups/delete/<int:backup_id>', methods=['GET', 'POST'])
def delete_backup(backup_id):
    backup = backup_service.get_backup_id(backup_id)
    if request.method == 'POST':
        backup_service.delete_backup(backup)
        return redirect(url_for('configure_settings'))
    return render_template('backup/detail_backup.html', backup=backup)

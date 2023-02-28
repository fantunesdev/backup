import datetime

from flask import render_template

from app import app
from app.services import backup_service


@app.route('/backups')
def get_backups():
    backups = backup_service.get_backups()
    return render_template('backup/get_backups.html', backups=backups)


@app.route('/backups/<int:backup_id>')
def get_backup_id(backup_id):
    backup = backup_service.get_backup_id(backup_id)
    return render_template('backup/detail_backup.html', backup=backup)

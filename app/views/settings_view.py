from flask import render_template

from app import app
from app.services import backup_service, frequency_service


@app.route('/settings')
def configure_settings():
    backups = backup_service.get_backups()
    frequencies = frequency_service.get_frequencies()
    return render_template('settings.html', backups=backups, frequencies=frequencies)

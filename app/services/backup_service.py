from app.models import Backup


def get_backups():
    return Backup.query.all()


def get_backup_id(backup_id):
    return Backup.query.get(backup_id)

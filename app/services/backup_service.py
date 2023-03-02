from app import db
from app.models import Backup


def create_backup(new_backup):
    db.session.add(new_backup)
    db.session.commit()


def get_backups():
    return Backup.query.all()


def get_backup_id(backup_id):
    return Backup.query.get(backup_id)


def update_backup(old_backup, new_backup):
    old_backup.description = new_backup.description
    old_backup.source = new_backup.source
    old_backup.target = new_backup.target
    old_backup.program = new_backup.program
    old_backup.options = new_backup.options
    old_backup.frequency = new_backup.frequency
    db.session.commit()


def delete_backup(backup):
    db.session.delete(backup)
    db.session.commit()

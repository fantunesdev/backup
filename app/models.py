from sqlalchemy.orm import relationship

from app import db


class Frequency(db.Model):
    __tablename__ = 'frequency'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(50), nullable=False)

    def __str__(self):
        return self.description


class Backup(db.Model):
    __tablename__ = 'backup'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    description = db.Column(db.String(50))
    source = db.Column(db.String(255))
    target = db.Column(db.String(255), nullable=False)
    program = db.Column(db.String(25), nullable=False)
    options = db.Column(db.String(255))
    frequency = db.Column(db.ForeignKey('frequency.id'), nullable=False)

    frequency_obj = relationship('Frequency')

    def __str__(self):
        return self.description


class Relatory(db.Model):
    __tablename__ = 'relatory'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime, nullable=False)
    backup = db.Column(db.ForeignKey('backup.id'), nullable=False)
    log = db.Column(db.Text)

    backup_obj = relationship('Backup')

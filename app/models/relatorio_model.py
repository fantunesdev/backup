from sqlalchemy.orm import relationship

from app import db


class Acao(db.Model):
    __tablename__ = 'acao'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descricao = db.Column(db.String(50), nullable=False)


class Frequencia(db.Model):
    __tablename__ = 'frequencia'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descricao = db.Column(db.String(50), nullable=False)


class Relatorio(db.Model):
    __tablename__ = 'relatorio'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    acao_id = db.Column(db.ForeignKey('acao.id'), nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    frequencia_id = db.Column(db.ForeignKey('frequencia.id'), nullable=False)
    data = db.Column(db.DateTime, nullable=False)
    detalhamento = db.Column(db.Text, nullable=True)

    acao = relationship('Acao')
    frequencia = relationship('Frequencia')

    @property
    def estatus(self):
        if self.status:
            return 'Ok'
        else:
            return 'Falhou'

    @property
    def data_pt_br(self):
        return self.data.strftime('%d/%m/%Y às %H:%M:%S')

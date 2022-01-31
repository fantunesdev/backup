from sqlalchemy import extract

from app.models import relatorio_model
from app.models.relatorio_model import Relatorio


def listar_relatorios():
    return relatorio_model.Relatorio.query.all()


def listar_dia(dia):
    return Relatorio.query\
        .filter(Relatorio.data.like(f'{dia}%'))\
        .filter(Relatorio.frequencia_id == 1)\
        .order_by(Relatorio.id.desc())


def listar_semana(semana):
    return Relatorio.query\
        .filter_by(frequencia_id=3)\
        .filter(extract('week', Relatorio.data) == semana)\
        .order_by(Relatorio.acao_id)


def listar_relatorio_id(relatorio_id):
    return Relatorio.query.filter_by(id=relatorio_id).first()

from app.models import relatorio_model
from app.models.relatorio_model import Relatorio


def listar_relatorios():
    return relatorio_model.Relatorio.query.all()


def listar_dia(dia):
    return Relatorio.query.filter(Relatorio.data.like(f'{dia}%')).order_by(Relatorio.id.desc())

import datetime
from app import app
from flask import render_template
from app.repositorios import relatorio_repositorio
from app.services import relatorio_service


@app.route('/sincronizacao')
def listar_hoje():
    hoje = datetime.date.today()
    data = hoje.strftime('%d/%m/%Y')
    relatorios = relatorio_service.listar_dia(hoje)
    matriz = relatorio_repositorio.montar_templatetags(relatorios)
    total = len(matriz) * (len(matriz[0]) - 1)
    return render_template('relatorio/sincronizacao.html', matriz=matriz, total=total, data=data)


@app.route('/sincronizacao/<string:dia>')
def listar_dia(dia):
    dia = datetime.datetime.strptime(dia, '%Y-%m-%d').date()
    data = dia.strftime('%d/%m/%Y')
    relatorios = relatorio_service.listar_dia(dia)
    matriz = relatorio_repositorio.montar_templatetags(relatorios)
    total = len(matriz) * (len(matriz[0]) - 1)
    return render_template('relatorio/sincronizacao.html', matriz=matriz, total=total, data=data)

@app.route('/relatorios/<int:relatorio_id>')
def listar_relatorio_id(relatorio_id):
    relatorio = relatorio_service.listar_relatorio_id(relatorio_id)
    return render_template('relatorio/expandir.html', relatorio=relatorio)

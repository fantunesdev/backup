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
    sucessos_falhas = relatorio_repositorio.retorna_numero_sucessos_falhas(relatorios)
    return render_template('relatorio/sincronizacao.html', matriz=matriz,
                                                           sucessos=sucessos_falhas['sucessos'],
                                                           falhas=sucessos_falhas['falhas'],
                                                           data=data)


@app.route('/sincronizacao/<string:dia>')
def listar_dia(dia):
    dia = datetime.datetime.strptime(dia, '%Y-%m-%d').date()
    data = dia.strftime('%d/%m/%Y')
    relatorios = relatorio_service.listar_dia(dia)
    matriz = relatorio_repositorio.montar_templatetags(relatorios)
    sucessos_falhas = relatorio_repositorio.retorna_numero_sucessos_falhas(relatorios)
    return render_template('relatorio/sincronizacao.html', matriz=matriz,
                                                           sucessos=sucessos_falhas['sucessos'],
                                                           falhas=sucessos_falhas['falhas'],
                                                           data=data)


@app.route('/semana', defaults={'semana': None})
@app.route('/semana/<int:semana>')
def listar_semana(semana):
    if not semana:
        semana = datetime.date.today().isocalendar()[1]
    relatorios = relatorio_service.listar_semana(semana)
    sucessos_falhas = relatorio_repositorio.retorna_numero_sucessos_falhas(relatorios)
    return render_template('relatorio/semana.html', relatorios=relatorios,
                                                    sucessos=sucessos_falhas['sucessos'],
                                                    falhas=sucessos_falhas['falhas'],
                                                    semana=semana)


@app.route('/relatorios/<int:relatorio_id>')
def listar_relatorio_id(relatorio_id):
    relatorio = relatorio_service.listar_relatorio_id(relatorio_id)
    return render_template('relatorio/expandir.html', relatorio=relatorio)

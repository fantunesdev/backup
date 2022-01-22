from unidecode import unidecode


def montar_templatetags(relatorios):

    linhas = []
    colunas = []
    matriz = [[]]
    contador = 1

    for relatorio in relatorios:
        if relatorio.acao.descricao not in linhas:
            linhas.append(relatorio.acao.descricao)
        if relatorio.data.strftime('%H') not in colunas:
            colunas.append(relatorio.data.strftime('%H'))

    matriz[0].append('Ação')
    for j in colunas:
        if j not in matriz[0]:
            matriz[0].append(j)

    for i in linhas:
        matriz.append([])
        matriz[contador].append(i)
        contador += 1

    for relatorio in relatorios:
        for linha in matriz:
            i = matriz.index(linha)
            if i == 0:
                continue
            acao = relatorio.acao.descricao
            if acao in linha:
                matriz[i].append(relatorio.status)

    return matriz


def retornar_horas(relatorios):
    horas = []
    for relatorio in relatorios:
        hora = relatorio.data.strftime('%H')
        if hora not in horas:
            horas.append(hora)
    horas.sort(reverse=True)
    return horas


def retornar_distintos(relatorios):
    distintos = []
    for relatorio in relatorios:
        if relatorio.acao.descricao not in distintos:
            distintos.append(relatorio.acao.descricao)
    return distintos


def retornar_datas(relatorios):
    datas = []
    for relatorio in relatorios:
        if relatorio.data not in datas:
            datas.append(relatorio.data)
    return datas


def slugify(string):
    evitar = '^~/'
    lower = string.lower()
    unicode = unidecode(lower)
    underscore = unicode.replace(' ', '_')
    for letra in underscore:
        if letra in evitar:
            underscore = underscore.replace(letra, '')
    return underscore

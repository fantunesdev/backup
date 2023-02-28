from unidecode import unidecode


def templatetags_assembler(relatories):

    rows = []
    columns = []
    matrix = [[]]
    counter = 1

    for relatory in relatories:
        if relatory.backup_obj.description not in rows:
            rows.append(relatory.backup_obj.description)
        if relatory.date.strftime('%H') not in columns:
            columns.append(relatory.date.strftime('%H'))

    matrix[0].append('Backup')
    for j in columns:
        if j not in matrix[0]:
            matrix[0].append(j)

    for i in rows:
        matrix.append([])
        matrix[counter].append(i)
        counter += 1

    for relatory in relatories:
        for row in matrix:
            i = matrix.index(row)
            if i == 0:
                continue
            backup = relatory.backup_obj.description
            if backup in row:
                matrix[i].append(relatory)

    return matrix


def get_hours(relatories):
    hours = []
    for relatory in relatories:
        hour = relatory.data.strftime('%H')
        if hour not in hours:
            hours.append(hour)
    hours.sort(reverse=True)
    return hours


def get_distinct(relatories):
    distinct = []
    for relatory in distinct:
        if relatory.backup_obj.description not in distinct:
            distinct.append(relatory.backup_obj.description)
    return distinct


def get_dates(relatories):
    dates = []
    for relatory in relatories:
        if relatory.date not in dates:
            dates.append(relatory.date)
    return dates


def get_success_fail_number(relatories):
    success_counter = 0
    fail_counter = 0
    for relatory in relatories:
        if relatory.status:
            success_counter += 1
        else:
            fail_counter += 1
    return {'success': success_counter,
            'fails': fail_counter}


def slugify(string):
    avoid = '^~/'
    lower = string.lower()
    unicode = unidecode(lower)
    underscore = unicode.replace(' ', '_')
    for letter in underscore:
        if letter in avoid:
            underscore = underscore.replace(letter, '')
    return underscore

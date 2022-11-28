from datetime import datetime

def get_table_from_html(soup):
    table = soup.find('table', {'class': 'edit-delete', 'id': 'ref_games'})
    table = str(table)
    table = table.split('<table class="edit-delete" id="ref_games">')[1]
    table = table.split('</table>')[0]

    return table

def clean_table(games):
    clean_games = {}
    for game in games:
        date = get_datetime(games[game]['td'][0]['_value'])
        start_time = get_start_time(date, games[game]['td'][1]['_value'])
        end_time = get_end_time(date, games[game]['td'][1]['_value'])
        summary = get_summary(games[game]['td'])

        clean_games[game] = {'start': {'dateTime': start_time}}
        clean_games[game]['end'] = {'dateTime': end_time}
        clean_games[game].update({'summary': games[game]['td'][3]['_value']})
        clean_games[game].update({'location': games[game]['td'][2]['a'][0]['_value']})
        clean_games[game].update({'description': summary})

    return clean_games

def get_datetime(date):
    date = date.split(' ', 1)[1]
    date = datetime.strptime(date, '%b-%d-%y').strftime('%Y-%m-%d')

    return date

def get_start_time(date, time):
    start_time = time.split(' - ', 1)[0]
    start_time = datetime.strptime(start_time, '%I:%M %p').strftime('%H:%M')
    start_time = date + 'T' + start_time + ':00-07:00'
    start_time = datetime.strptime(start_time, '%Y-%m-%dT%H:%M:%S%z').isoformat('T')

    return start_time

def get_end_time(date, time):
    end_time = time.split(' - ', 1)[1]
    end_time = datetime.strptime(end_time, '%I:%M %p').strftime('%H:%M')
    end_time = date + 'T' + end_time + ':00-07:00'
    end_time = datetime.strptime(end_time, '%Y-%m-%dT%H:%M:%S%z').isoformat('T')

    return end_time

def get_summary(game):
    summary = 'Game Type: ' + game[4]['_value'] + '\n' + 'Visiting Team: ' + game[5]['_value'] + '\n' + 'Home Team: ' + game[6]['_value'] + '\n'
    ref1, ref2, lines1, lines2, house1, house2, supervisor = '', '', '', '', '', '', ''

    try:
        ref1 = game[7]['_value']
        summary += 'Referee: ' + ref1 + '\n'
    except:
        pass
    try:
        ref2 = game[8]['_value']
        summary += 'Referee: ' + ref2 + '\n'
    except:
        pass
    try:
        lines1 = game[9]['_value']
        summary += 'Linesman: ' + lines1 + '\n'
    except:
        pass
    try:
        lines2 = game[10]['_value']
        summary += 'Linesman: ' + lines2 + '\n'
    except:
        pass
    try:
        house1 = game[11]['_value']
        summary += 'Linesman: ' + house1 + '\n'
    except:
        pass
    try:
        house2 = game[12]['_value']
        summary += 'Linesman: ' + house2 + '\n'
    except:
        pass
    try:
        supervisor = game[13]['_value']
        summary += 'Supervisor: ' + supervisor + '\n'
    except:
        pass

    return summary
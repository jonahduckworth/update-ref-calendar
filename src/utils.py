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

        print('start_time: ', start_time)
        print('end_time:   ', end_time)

        clean_games[game] = {'date': date}
        clean_games[game].update({'time': games[game]['td'][1]['_value']})
        clean_games[game].update({'location': games[game]['td'][2]['a'][0]['_value']})
        clean_games[game].update({'category': games[game]['td'][3]['_value']})
        clean_games[game].update({'type': games[game]['td'][4]['_value']})
        clean_games[game].update({'visiting_team': games[game]['td'][5]['_value']})
        clean_games[game].update({'home_team': games[game]['td'][6]['_value']})
        try:
            clean_games[game].update({'ref1': games[game]['td'][7]['_value']})
        except:
            clean_games[game].update({'ref1': None})
        try:
            clean_games[game].update({'ref2': games[game]['td'][8]['_value']})
        except:
            clean_games[game].update({'ref2': None})
        try:
            clean_games[game].update({'lines1': games[game]['td'][9]['_value']})
        except:
            clean_games[game].update({'lines1': None})
        try:
            clean_games[game].update({'lines2': games[game]['td'][10]['_value']})
        except:
            clean_games[game].update({'lines2': None})
        try:
            clean_games[game].update({'house1': games[game]['td'][11]['_value']})
        except:
            clean_games[game].update({'house1': None})
        try:
            clean_games[game].update({'house2': games[game]['td'][12]['_value']})
        except:
            clean_games[game].update({'house2': None})
        try:
            clean_games[game].update({'supervisor': games[game]['td'][13]['_value']})
        except:
            clean_games[game].update({'supervisor': None})

    return clean_games

def get_datetime(date):
    date = date.split(' ', 1)[1]
    date = datetime.strptime(date, '%b-%d-%y').strftime('%Y-%m-%d')

    return date

def get_start_time(date, time):
    start_time = time.split(' - ', 1)[0]
    start_time = datetime.strptime(start_time, '%I:%M %p').strftime('%H:%M')
    start_time = date + 'T' + start_time + ':00-07:00'

    return start_time

def get_end_time(date, time):
    end_time = time.split(' - ', 1)[1]
    end_time = datetime.strptime(end_time, '%I:%M %p').strftime('%H:%M')
    end_time = date + 'T' + end_time + ':00-07:00'

    return end_time
from bs4 import BeautifulSoup as bs4
import requests
import json
import time
import html_to_json
import pandas as pd

def update():

    cookies = {
        'locale': 'en_CA',
        '__utmc': '1',
        '__utmv': "1.|1=Org%20ID=682=1^2=Ads%20Displayed=false=1^3=Org%20Name=Central%20Region%20Referees'%20Committee=1",
        '_ga': 'GA1.3.67814177.1668442561',
        '__qca': 'P0-1750481069-1668442561773',
        '_gcl_au': '1.1.755741071.1668442986',
        '__gtm_referrer': 'https%3A%2F%2Fczrc.goalline.ca%2F',
        '_ga': 'GA1.1.272533617.1668442986',
        '_ga_060C46HJ6P': 'GS1.1.1668442986.1.0.1668442993.0.0.0',
        '_ga_401S33L4PF': 'GS1.1.1668442986.1.0.1668442996.0.0.0',
        'gl_ref_email': 'jonahduck%40gmail.com',
        'intercom-id-v9yzaleo': '7383aec8-a8bf-45ba-85c0-e3a6af8c05ff',
        'intercom-session-v9yzaleo': '',
        '_hjSessionUser_291201': 'eyJpZCI6IjFmNDZmNGI0LWUwMDEtNWU1Ny04ZGFiLTQyNjU5OWExNGQzOCIsImNyZWF0ZWQiOjE2Njg3OTQzODg3MTksImV4aXN0aW5nIjp0cnVlfQ==',
        'gl_ref_pass': 'vqy_yqz_qra1ZYX7tkm',
        '_gid': 'GA1.3.1939218577.1669071096',
        '__utmz': '1.1669139202.6.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
        '__utma': '1.67814177.1668442561.1669139202.1669144954.7',
        '__utmb': '1.2.10.1669144954',
        'mp_4ad8a04b18d5ec30a5d65ececa08a630_mixpanel': '%7B%22distinct_id%22%3A%20%221848be5908e64c-0eadef996dd309-18525635-1aeaa0-1848be5908fe5b%22%2C%22%24device_id%22%3A%20%221848be5908e64c-0eadef996dd309-18525635-1aeaa0-1848be5908fe5b%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fczrc.goalline.ca%2Flogin_ref.php%22%2C%22%24initial_referring_domain%22%3A%20%22czrc.goalline.ca%22%7D',
        '_hjIncludedInSessionSample': '0',
        '_hjSession_291201': 'eyJpZCI6IjUyMGEwMGJkLTk5Y2QtNDMzOS04Zjg2LTExNDlmMTg1ZTc0YSIsImNyZWF0ZWQiOjE2NjkxNDQ5NTQ1NzgsImluU2FtcGxlIjpmYWxzZX0=',
        '_hjIncludedInPageviewSample': '1',
        '_hjAbsoluteSessionInProgress': '0',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': "locale=en_CA; __utmc=1; __utmv=1.|1=Org%20ID=682=1^2=Ads%20Displayed=false=1^3=Org%20Name=Central%20Region%20Referees'%20Committee=1; _ga=GA1.3.67814177.1668442561; __qca=P0-1750481069-1668442561773; _gcl_au=1.1.755741071.1668442986; __gtm_referrer=https%3A%2F%2Fczrc.goalline.ca%2F; _ga=GA1.1.272533617.1668442986; _ga_060C46HJ6P=GS1.1.1668442986.1.0.1668442993.0.0.0; _ga_401S33L4PF=GS1.1.1668442986.1.0.1668442996.0.0.0; gl_ref_email=jonahduck%40gmail.com; intercom-id-v9yzaleo=7383aec8-a8bf-45ba-85c0-e3a6af8c05ff; intercom-session-v9yzaleo=; _hjSessionUser_291201=eyJpZCI6IjFmNDZmNGI0LWUwMDEtNWU1Ny04ZGFiLTQyNjU5OWExNGQzOCIsImNyZWF0ZWQiOjE2Njg3OTQzODg3MTksImV4aXN0aW5nIjp0cnVlfQ==; gl_ref_pass=vqy_yqz_qra1ZYX7tkm; _gid=GA1.3.1939218577.1669071096; __utmz=1.1669139202.6.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utma=1.67814177.1668442561.1669139202.1669144954.7; __utmb=1.2.10.1669144954; mp_4ad8a04b18d5ec30a5d65ececa08a630_mixpanel=%7B%22distinct_id%22%3A%20%221848be5908e64c-0eadef996dd309-18525635-1aeaa0-1848be5908fe5b%22%2C%22%24device_id%22%3A%20%221848be5908e64c-0eadef996dd309-18525635-1aeaa0-1848be5908fe5b%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fczrc.goalline.ca%2Flogin_ref.php%22%2C%22%24initial_referring_domain%22%3A%20%22czrc.goalline.ca%22%7D; _hjIncludedInSessionSample=0; _hjSession_291201=eyJpZCI6IjUyMGEwMGJkLTk5Y2QtNDMzOS04Zjg2LTExNDlmMTg1ZTc0YSIsImNyZWF0ZWQiOjE2NjkxNDQ5NTQ1NzgsImluU2FtcGxlIjpmYWxzZX0=; _hjIncludedInPageviewSample=1; _hjAbsoluteSessionInProgress=0",
        'Origin': 'https://czrc.goalline.ca',
        'Referer': 'https://czrc.goalline.ca/show_referee_assignments.php',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }

    data = {
        'the_d': '1',
        'from_month': '11',
        'from_day': '22',
        'from_year': '2022',
        'to_month': '12',
        'to_day': '25',
        'to_year': '2022',
        'the_league[]': '0',
        'venue_id[]': '0',
        'the_ref': '93275',
    }

    response = requests.post('https://czrc.goalline.ca/show_referee_assignments.php', cookies=cookies, headers=headers, data=data)

    soup = bs4(response.text, 'html.parser')

    table = soup.find('table', {'class': 'edit-delete', 'id': 'ref_games'})
    table = str(table)
    table = table.split('<table class="edit-delete" id="ref_games">')[1]
    table = table.split('</table>')[0]

    json2 = html_to_json.convert(table)

    games = {}
    count = 0

    for game in json2['tr']:
        games[count] = game
        count += 1

    games.pop(0)

    clean_games = {}
    
    for game in games:
        # pretty = json.dumps(games[game]['td'], indent=4, sort_keys=True)
        # print(pretty)

        clean_games[game] = {'date': games[game]['td'][0]['_value']}
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

    pretty = json.dumps(clean_games, indent=4, sort_keys=False)
    print(pretty)


    return ("", 204)
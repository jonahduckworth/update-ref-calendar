from bs4 import BeautifulSoup as bs4
import requests
import json
import html_to_json
import config
import utils

def update():
    url = config.GAMES_URL
    cookies = config.getCookies
    headers = config.getHeaders
    data = config.getData

    response = requests.post(url, cookies=cookies, headers=headers, data=data)
    soup = bs4(response.text, 'html.parser')

    table = utils.get_table_from_html(soup)
    table_json = html_to_json.convert(table)

    games = {}
    count = 0

    for game in table_json['tr']:
        games[count] = game
        count += 1

    # don't need item at first index
    games.pop(0)

    clean_games = utils.clean_table(games)

    pretty = json.dumps(clean_games, indent=4, sort_keys=False)
    print(pretty)

    return ("", 204)
from multiprocessing import Pool
from urllib.request import Request, urlopen

from fake_useragent import UserAgent
from bs4 import BeautifulSoup

ACCESSORIES_URLS = [
    'http://pathofexile.gamepedia.com/List_of_unique_amulets',
    'http://pathofexile.gamepedia.com/List_of_unique_belts',
    'http://pathofexile.gamepedia.com/List_of_unique_rings',
    'http://pathofexile.gamepedia.com/List_of_unique_quivers'
]

ARMOUR_URLS = [
    'http://pathofexile.gamepedia.com/List_of_unique_body_armours',
    'http://pathofexile.gamepedia.com/List_of_unique_boots',
    'http://pathofexile.gamepedia.com/List_of_unique_gloves',
    'http://pathofexile.gamepedia.com/List_of_unique_helmets',
    'http://pathofexile.gamepedia.com/List_of_unique_shields'
]

WEAPON_URLS = [
    'http://pathofexile.gamepedia.com/List_of_unique_axes',
    'http://pathofexile.gamepedia.com/List_of_unique_bows',
    'http://pathofexile.gamepedia.com/List_of_unique_claws',
    'http://pathofexile.gamepedia.com/List_of_unique_daggers',
    'http://pathofexile.gamepedia.com/List_of_unique_fishing_rods',
    'http://pathofexile.gamepedia.com/List_of_unique_maces',
    'http://pathofexile.gamepedia.com/List_of_unique_staves',
    'http://pathofexile.gamepedia.com/List_of_unique_swords',
    'http://pathofexile.gamepedia.com/List_of_unique_wands'
]

FLASK_URLS = [
    'http://pathofexile.gamepedia.com/List_of_unique_life_flasks',
    'http://pathofexile.gamepedia.com/List_of_unique_mana_flasks',
    'http://pathofexile.gamepedia.com/List_of_unique_hybrid_flasks',
    'http://pathofexile.gamepedia.com/List_of_unique_utility_flasks'
]

JEWEL_URLS = [
    'http://pathofexile.gamepedia.com/List_of_unique_jewels',
]

MAP_URLS = [
    'http://pathofexile.gamepedia.com/List_of_unique_maps',
]

ALL_URLS = [ACCESSORIES_URLS, ARMOUR_URLS, WEAPON_URLS, FLASK_URLS, JEWEL_URLS, MAP_URLS]


def fetch_all():
    items = []

    for urls in ALL_URLS:
        items.append(fetch_group(urls))

    return items


def fetch_group(urls):
    return Pool().map(fetch, urls)


def fetch(url):
    items = []

    req = Request(url)
    req.add_header('User-Agent', UserAgent().random)

    conn = urlopen(req).read()
    document = BeautifulSoup(conn, 'html.parser')
    conn.close()

    for table in document.findAll('table', {'class': 'wikitable'}):
        for row in table.findAll('tr', {'id': True}):
            columns = row.findAll('td')

            item = {}

            item['name'] = columns[0]['data-sort-value']
            item['type'] = columns[1]['data-sort-value']
            item['level'] = columns[2].text

            try:

                description = []

                for modifier in columns[len(columns) - 1].div.findAll('span'):
                    for text_line in modifier.stripped_strings:
                        description.append(text_line)

                item['description'] = description

            except AttributeError:
                print('ERROR parsing item', item)
                item['description'] = []

            finally:
                items.append(item)

    document.decompose()

    return items

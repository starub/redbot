import json

import os

DB_PATH = os.getcwd() + '/db/items.json'


def save(items):
    try:
        os.remove(DB_PATH)
    except:
        pass

    file = open(DB_PATH, 'w+')

    json.dump(items, file, indent=4, sort_keys=True)

    file.close()


def load():
    file = open(DB_PATH, 'r')

    items = json.load(file)

    file.close()

    return items

import json

import os
import fetch

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
    return json.load(open(DB_PATH, 'r'))


save(fetch.fetch_all())

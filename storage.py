import json

import os
import fetcher

DB_PATH = os.getcwd() + '/storage/items.db'


def save(items):
    try:
        os.remove(DB_PATH)
    except:
        pass

    file = open(DB_PATH, 'rw')

    json.dump(items, file)

    file.close()

items = fetcher.fetch_group(fetcher.MAP_URLS)
print(items)

save(items)

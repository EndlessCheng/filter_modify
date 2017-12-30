from datetime import datetime
from multiprocessing.pool import Pool
import time

import requests

_now = datetime.now()
_type_list = ['normal', 'cruel', 'merciless', 'uber'][:3]


def fetch_image(type_):
    url = "http://www.poelab.com/wp-content/uploads/{year}/{month}/{year}-{month}-{day}_{type}.jpg".format(
        year=_now.year, month=_now.month, day=_now.day, type=type_)
    print(url)
    r = requests.get(url)
    with open('{}.jpg'.format(type_), 'wb') as img:
        img.write(r.content)


def main():
    with Pool(len(_type_list)) as p:
        p.map(fetch_image, _type_list)


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("Fetch success, time cost: {:.0f}ms".format(1000 * (time.time() - start_time)))

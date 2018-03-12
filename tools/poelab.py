from datetime import datetime
from multiprocessing.pool import Pool
import time

import requests

_now = datetime.now()
_type_list = ['normal', 'cruel', 'merciless', 'uber'][:3]


def fetch_image(type_):
    url = "http://www.poelab.com/wp-content/uploads/{year}/{month:02}/{year}-{month:02}-{day:02}_{type}.jpg".format(
        year=_now.year, month=_now.month, day=_now.day, type=type_)
    print(url)
    r = requests.get(url)
    with open('{}.jpg'.format(_type_list.index(type_) + 1), 'wb') as img:
        img.write(r.content)


def main():
    pool_size = [len(_type_list), 1][1]
    with Pool(pool_size) as p:
        p.map(fetch_image, _type_list)


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("Fetch success, time cost: {:.0f}ms".format(1000 * (time.time() - start_time)))

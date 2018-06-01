from datetime import datetime, timedelta
from multiprocessing.pool import Pool
import time

import requests

TYPE_LIST = ['normal', 'cruel', 'merciless', 'uber']

_type_list = ['normal', 'cruel', 'merciless', 'uber'][:1]


def gen_url(dt, type_):
    return "http://www.poelab.com/wp-content/uploads/{year}/{month:02}/{year}-{month:02}-{day:02}_{type}.jpg".format(
        year=dt.year, month=dt.month, day=dt.day, type=type_)


def fetch_image(dt, type_):
    url = gen_url(dt, type_)
    print(url)
    r = requests.get(url)
    return r


def fetch_image_file(type_):
    now = datetime.now()
    r = fetch_image(now, type_)
    if r.status_code == 404:
        print(f'{type_} 404')
        now -= timedelta(days=1)
        r = fetch_image(now, type_)
    with open('{}.jpg'.format(TYPE_LIST.index(type_) + 1), 'wb') as img:
        img.write(r.content)


def main():
    pool_size = [len(_type_list), 1][1]
    with Pool(pool_size) as p:
        p.map(fetch_image_file, _type_list)


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("Fetch success, time cost: {:.0f}ms".format(1000 * (time.time() - start_time)))

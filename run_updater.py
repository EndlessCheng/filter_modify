import os

from utils.parser import NSParser
from utils.updater import NSUpdater

if __name__ == '__main__':
    filter_path = 'res' + os.sep + 'NeverSink\'s filter - 1-REGULAR.filter'
    block_indexes = NSParser(filter_path).extract_block_indexes()
    NSUpdater('modify.py', block_indexes).update()

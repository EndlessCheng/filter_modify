import os

from utils.parser import NSParser
from utils.updater import NSUpdater

if __name__ == '__main__':
    filter_path = 'res' + os.sep + 'NeverSink\'s filter - 1-REGULAR.filter'
    ns_block_indexes = NSParser(filter_path, '0100').extract_block_indexes()
    assert ns_block_indexes
    NSUpdater('modify.py', ns_block_indexes).update()

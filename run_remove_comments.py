import os

from utils.parser import NSParser

if __name__ == '__main__':
    filter_name = 'NeverSink\'s filter - 0-SOFT.filter'
    filter_path = 'res' + os.sep + filter_name
    NSParser(filter_path).remove_comments()

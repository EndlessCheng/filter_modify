import os

from utils.parser import NSParser

if __name__ == '__main__':
    filter_path = 'res' + os.sep + 'NeverSink\'s filter - 1-REGULAR.filter'
    NSParser(filter_path).remove_comments()

import copy

from filter_modify import *

if __name__ == '__main__':
    with open("NeverSink's filter - 1-REGULAR.filter") as f:
        filter_manager = FilterManager(f.readlines())

    for i in range(100, 2501):
        filter_manager.extend_blocks(block_number=i)

    with open("SIMPLE.filter", 'w') as f:
        f.writelines(filter_manager.new_text)

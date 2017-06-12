# -*- coding:utf-8 -*-

import copy


class FilterBlock:
    # See http://pathofexile.gamepedia.com/Item_filter
    # See https://dd.reddit.com/r/pathofexile/comments/5ftpbg/lootfilter_performance_tips_thanks_to_the/
    _FILTER_ORDER = [
        # Conditions
        'LinkedSockets',
        'Sockets',
        'Quality',
        'Corrupted',
        'Identified',
        'SocketGroup',
        'Height',
        'Width',
        'DropLevel',
        'Class',
        'BaseType',
        'Rarity',
        'ItemLevel',

        # Actions(Styles)
        'SetFontSize',
        'SetTextColor',
        'SetBorderColor',
        'SetBackgroundColor',
        'PlayAlertSound',
    ]

    def __init__(self, raw_text=None, status='Show', **kwargs):
        self.SetFontSize = 33  # default
        if raw_text is None:
            self.status = status
        else:
            text = [line.split('#')[0].strip() for line in raw_text]
            self.status = text[0]
            for line in text[1:]:
                if line == '':
                    continue
                pos = line.find(' ')  # 第一个空格分割属性和属性值
                if line[:pos] == 'ItemLevel' and getattr(self, 'Class', None) == 'Flasks':
                    if hasattr(self, 'ItemLevel'):
                        continue  # FIXME: 影响？
                setattr(self, line[:pos], line[pos + 1:])
        self.modify(**kwargs)

    def modify(self, **kwargs):
        for k, v in kwargs.iteritems():
            setattr(self, k, v)

    def copy_modify(self, **kwargs):
        block = copy.copy(self)
        for k, v in kwargs.iteritems():
            setattr(block, k, v)
        return block

    def generate(self):
        new_text = [self.status + '\n']
        for attr in self._FILTER_ORDER:
            if hasattr(self, attr):
                new_text.append(" {} {}\n".format(attr, str(getattr(self, attr))))
        assert len(new_text) > 1
        return new_text


class FilterManager:
    new_text = []

    def __init__(self, raw_text):
        self.raw_text = raw_text

    def _get_small_block(self, start_index):
        block = []
        for line in self.raw_text[start_index:]:
            if line.strip() == '':
                break
            block.append(line)
        return FilterBlock(block)

    def _get_small_blocks(self, start_index):
        blocks = []
        while True:
            line = self.raw_text[start_index]
            if line.strip() == '':
                start_index += 1
                continue
            if line[:2] == '#=' or line[:4] == '#   ':  # 小心未来文件结构上的变化
                return blocks
            if line[:4] == 'Show' or line[:4] == 'Hide':
                blocks.append(self._get_small_block(start_index))
            start_index += 1

    def _get_big_block(self, block_number):
        for i in range(len(self.raw_text)):
            if self.raw_text[i][:2] == '#=' and self.raw_text[i + 1][6:8] == '00':
                if block_number == int(self.raw_text[i + 1][4:8]):
                    return self._get_small_blocks(i + 3)

    def _get_middle_block(self, block_number):
        for i in range(len(self.raw_text)):
            if self.raw_text[i][:2] == '#-' and self.raw_text[i + 1][:4] == '#   ':
                if block_number == int(self.raw_text[i + 1][5:9]):
                    return self._get_small_blocks(i + 3)

    def get_block(self, block_number):
        if block_number % 100 == 0:
            return self._get_big_block(block_number)
        return self._get_middle_block(block_number)

    def append_block(self, filter_block):
        self.new_text.extend(filter_block.generate())

    def extend_blocks(self, filter_blocks=None, block_number=-1):
        if block_number != -1:
            filter_blocks = self.get_block(block_number)
        if filter_blocks is not None:
            for block in filter_blocks:
                self.append_block(block)

    def add_comment(self, block_number, comment):
        self.new_text.append("\n# {:0>4} {}\n".format(block_number, comment))

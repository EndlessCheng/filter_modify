# -*- coding:utf-8 -*-

RARITY_NORMAL = 'Normal'
RARITY_MAGIC = 'Magic'
RARITY_RARE = 'Rare'
RARITY_UNIQUE = 'Unique'
RARITY_GEM = 'Gem'
RARITY_CURRENCY = 'Currency'


class ItemInfoParser:
    _SPLIT = '--------'

    rarity = ''
    name = ''
    item_class = ''

    sockets = ''

    affix_ms = ''

    def __init__(self, raw_info):
        self.info = raw_info.split('\n')

    def parse(self):
        if len(self.info) <= 1:
            return
        self.rarity = self.info[0].split(':')[1].strip()
        if self.rarity == RARITY_GEM:
            self.name = self.info[1]
        elif self.rarity == RARITY_CURRENCY:
            self.name = self.info[1]
        else:
            self.sockets = self.parse_sockets()
            self.affix_ms = self.parse_ms()

    def parse_sockets(self):
        for line in self.info:
            splits = line.split(':')
            if len(splits) == 2 and splits[0] == 'Sockets':
                return splits[1].strip()

    def parse_ms(self):
        for line in self.info[::-1]:
            if line == self._SPLIT:
                return 0
            splits = line.split('%')
            if len(splits) == 2 and splits[1].strip() == 'increased Movement Speed':
                self.item_class = 'Boots'
                return int(splits[0])

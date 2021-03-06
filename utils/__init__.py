import copy


class FilterBlock:
    """
    http://pathofexile.gamepedia.com/Item_filter
    https://dd.reddit.com/r/pathofexile/comments/5ftpbg/lootfilter_performance_tips_thanks_to_the/

    `... over 96% of all drops in the endgame are normal and magic items or very low orbs.`
    """
    _FILTER_ORDER = [
        # Conditions
        'LinkedSockets',
        'Sockets',
        'Quality',
        'ElderItem', 'ShaperItem',
        'ElderMap', 'ShapedMap',
        'MapTier',
        'Corrupted',
        'Identified',
        'SocketGroup',
        'Height', 'Width',
        'ItemLevel',
        'DropLevel',
        'Rarity',
        'Class',
        'BaseType',
        'HasExplicitMod',
        'StackSize',
        'GemLevel',

        # Actions(Styles)
        'SetFontSize', 'SetTextColor', 'SetBorderColor', 'SetBackgroundColor',
        'MinimapIcon',
        'PlayEffect',
        'PlayAlertSound', 'CustomAlertSound',
        'DisableDropSound',
    ]

    def __init__(self, raw_text=None, status='Show', **kwargs):
        # self.SetFontSize = 33  # default
        if not raw_text:
            self.status = status
        else:
            if isinstance(raw_text, str):
                raw_text = raw_text.split('\n')
            # self.remove_comments()
            text = [line.split('#')[0].strip() for line in raw_text]
            self.status = text[0]
            for line in text[1:]:
                if line == '':
                    continue
                attr_name, attr_value = line.split(' ', 1)
                assert attr_name in FilterBlock._FILTER_ORDER, attr_name

                attr = getattr(self, attr_name, None)
                if attr is not None:
                    if not isinstance(attr, list):  # str
                        attr = [attr]
                    attr.append(attr_value)
                    setattr(self, attr_name, attr)
                else:
                    setattr(self, attr_name, attr_value)
        self.modify(**kwargs)

    def modify(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def copy_modify(self, **kwargs):
        block = copy.copy(self)
        for k, v in kwargs.items():
            setattr(block, k, v)
        return block

    def generate(self):
        new_text = [self.status + '\n']
        for attr_name in FilterBlock._FILTER_ORDER:
            if getattr(self, attr_name, None) is not None:
                attr = getattr(self, attr_name)
                if attr_name == 'MinimapIcon':
                    attr = attr.replace('2', '0').replace('1', '0').replace('White', 'Yellow')

                if isinstance(attr, list):
                    for v in attr:
                        new_text.append(f" {attr_name} {v}\n")
                else:
                    new_text.append(f" {attr_name} {attr}\n")
        assert len(new_text) > 1
        return new_text


class FilterManager:
    def __init__(self, raw_text):
        self.raw_text = raw_text

        self.new_text = []

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
                break
            if line[:4] == 'Show' or line[:4] == 'Hide':
                blocks.append(self._get_small_block(start_index))
            start_index += 1
        return blocks

    def _get_big_block(self, block_number):
        for i in range(len(self.raw_text)):
            if self.raw_text[i][:2] == '#=' and self.raw_text[i + 1][6:8] == '00':
                if block_number == int(self.raw_text[i + 1][4:8]):
                    return self._get_small_blocks(i + 3)
        assert False
        # return []

    def _get_middle_block(self, block_number):
        for i in range(len(self.raw_text)):
            if self.raw_text[i][:2] == '#-' and self.raw_text[i + 1][:4] == '#   ':
                if block_number == int(self.raw_text[i + 1][5:9]):
                    return self._get_small_blocks(i + 3)
        assert False
        # return []

    def get_blocks(self, block_number):
        if block_number % 100 == 0:
            return self._get_big_block(block_number)
        return self._get_middle_block(block_number)

    def append_block(self, filter_block):
        self.new_text.extend(filter_block.generate())

    def extend_blocks(self, filter_blocks):
        for block in filter_blocks:
            self.append_block(block)

    def add_comment(self, block_number, comment, ignored=False):
        self.new_text.append("\n# {:0>4} {}\n".format(block_number, comment))
        return self.get_blocks(block_number) if not ignored else []

    def clear(self):
        self.new_text = []

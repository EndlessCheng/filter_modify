import os
import re


class BasicParser:
    def __init__(self, filter_path, first_index='0100'):
        self.filter_path = filter_path
        self.raw_text = self._read()

        self.first_index = first_index

    def _read(self):
        with open(self.filter_path) as f:
            return f.readlines()

    def remove_comments(self):
        new_text = [line for line in list(self.raw_text)
                    # if not line.startswith(('\tMinimapIcon', '\tPlayEffect'))
                    ]
        for no, line in enumerate(new_text, 1):
            if line and line[0] != '#':
                new_text[no - 1] = line.split('#')[0].rstrip() + '\n'

        new_file_path, ext = os.path.splitext(self.filter_path)
        new_file_path += '-no-comments' + ext
        with open(new_file_path, 'w') as f:
            return f.write(''.join(new_text))

    # TODO
    def gen_template(self):
        ...


class NSParser(BasicParser):
    def _extract_block_indexes(self):
        for no, l in enumerate(self.raw_text):
            if self.first_index in l:
                start_no = no
                for line in self.raw_text[start_no:]:
                    m = re.search(r'\[?\[[0-9]{4}\]\]?', line)
                    if m:
                        index_s = m.group()
                        index = int(index_s[1:-1] if len(index_s) == 6 else index_s[2:-2])
                        desc = line[m.end():].strip()
                        yield index, desc
                    else:
                        return

    def extract_block_indexes(self):
        return {index: desc for index, desc in self._extract_block_indexes()}

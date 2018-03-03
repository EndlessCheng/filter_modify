import re


class BasicParser:
    def __init__(self, filter_path):
        self.filter_path = filter_path
        self.raw_text = self._read()

    def _read(self):
        with open(self.filter_path) as f:
            return f.readlines()

    # TODO
    def gen_template(self):
        ...


class NSParser(BasicParser):
    def _extract_block_indexes(self):
        for no, l in enumerate(self.raw_text):
            if '0100' in l:
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

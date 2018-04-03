class BasicUpdater:
    pass


class NSUpdater(BasicUpdater):
    def __init__(self, script_path, ns_block_indexes=None):
        self.script_path = script_path
        with open(self.script_path, encoding='utf-8') as f:
            self.raw_text = f.readlines()
        self.ns_block_indexes = ns_block_indexes

    # TODO: ast
    def _parse_add_comment(self):
        for no, line in enumerate(self.raw_text, 1):
            if 'add_comment' in line:
                splits = line.split("'")
                assert len(splits) == 3, f"Line {no}: {line}"
                index_s = splits[0].split('(')[1].strip()[:-1]
                desc = splits[1].strip()
                yield no, index_s, desc

    # TODO: 提醒双方各缺/多的部分
    def _modify_indexes(self):
        cnt, width = 0, 10
        errors = []

        new_text = list(self.raw_text)

        for no, index_s, desc in self._parse_add_comment():
            cnt += 1
            end = '' if cnt % width else '\n'

            line = self.raw_text[no - 1]

            if not index_s.isdigit():
                print('W', end=end)  # Words
                # errors.append(('non-index', no, line))
                continue

            sub_times = sum(desc == v for _, v in self.ns_block_indexes.items())
            if sub_times > 1:
                print(min(sub_times, 9), end=end)
                errors.append(('multi-desc', no, line))
                continue

            for k, v in self.ns_block_indexes.items():
                if desc == v:
                    new_text[no - 1] = line.replace(index_s, str(k))
                    print('.', end=end)
                    break
            else:
                print('M', end=end)
                errors.append((f'miss', no, line))

        print()

        for error, no, line in errors:
            print(line.strip())
            print(f'WARNING: {error} at line {no}\n')

        return new_text

    def update(self):
        new_text = self._modify_indexes()
        with open(self.script_path, 'w', encoding='utf-8') as f:
            f.write(''.join(new_text))

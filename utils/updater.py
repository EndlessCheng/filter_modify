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

    def _modify_indexes(self):
        cnt, width = 0, 10
        errors = []

        new_text = list(self.raw_text)

        for no, index_s, desc in self._parse_add_comment():
            cnt += 1
            end = '' if cnt % width else '\n'

            line = self.raw_text[no - 1]

            if not index_s.isdigit():
                # 检测到常量字段，需要手动修改
                print('W', end=end)
                # errors.append(('non-index', no, line))
                continue

            ns_indexes = [k for k, v in self.ns_block_indexes.items() if desc == v]

            if len(ns_indexes) > 1:
                # 检测到该 desc 在 NS 中出现了多次，需要手动修改
                print(len(ns_indexes), end=end)
                errors.append(('multi-desc', no, line))
                continue

            if len(ns_indexes) == 0:
                # 未在 NS 中找到，请检查代码
                print('M', end=end)
                errors.append((f'miss', no, line))
                continue

            ns_index = ns_indexes[0]

            if int(index_s) == ns_index:
                # 无需修改（忽略）
                print('.', end=end)
            else:
                # 更新 desc 唯一相同但 index 不同的代码
                new_text[no - 1] = line.replace(index_s, str(ns_index))
                print('U', end=end)

        print()

        for error, no, line in errors:
            print(line.strip())
            print(f'WARNING: {error} at line {no}\n')

        return new_text

    def update(self):
        new_text = self._modify_indexes()
        with open(self.script_path, 'w', encoding='utf-8') as f:
            f.write(''.join(new_text))

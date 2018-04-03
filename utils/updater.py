import ast


class BasicUpdater:
    pass


class NSUpdater(BasicUpdater):
    TARGET_FUNC_NAME = 'add_comment'

    def __init__(self, script_path, ns_block_indexes=None):
        self.script_path = script_path
        with open(self.script_path, encoding='utf-8') as f:
            self.raw_text = f.readlines()
        self.ns_block_indexes = ns_block_indexes

    def _parse_add_comment(self):
        """
        已废弃。
        """
        for no, line in enumerate(self.raw_text, 1):
            if NSUpdater.TARGET_FUNC_NAME in line:
                splits = line.split("'")
                assert len(splits) == 3, f"Line {no}: {line}"
                index_s = splits[0].split('(')[1].strip()[:-1]
                desc = splits[1].strip()
                yield no, index_s, desc

    def _parse_add_comment_ast(self):
        py_module = ast.parse(''.join(self.raw_text))
        for py_ast in py_module.body:
            if isinstance(py_ast, ast.FunctionDef):
                # print(f"修改 {py_ast.name}() ...")
                for stmt in py_ast.body:
                    if isinstance(stmt, (ast.Expr, ast.Assign)) \
                            and isinstance(stmt.value, ast.Call) \
                            and isinstance(stmt.value.func, ast.Attribute) \
                            and stmt.value.func.attr == NSUpdater.TARGET_FUNC_NAME:
                        index_expr, desc_expr = stmt.value.args
                        assert isinstance(index_expr, (ast.Num, ast.Name))
                        assert isinstance(desc_expr, ast.Str)
                        index_s = str(index_expr.n) if isinstance(index_expr, ast.Num) else index_expr.id
                        desc = desc_expr.s
                        yield stmt.lineno, index_s, desc

    def _modify_indexes(self):
        cnt, width = 0, 10
        cnt_updated = 0
        errors = []

        new_text = list(self.raw_text)

        for lineno, index_s, desc in self._parse_add_comment_ast():
            cnt += 1
            end = '' if cnt % width else '\n'

            line = self.raw_text[lineno - 1]

            if not index_s.isdigit():
                # 检测到常量字段，需要手动修改
                print('W', end=end)
                # errors.append(('non-index', no, line))
                continue

            ns_indexes = [k for k, v in self.ns_block_indexes.items() if desc == v]

            if len(ns_indexes) > 1:
                # 检测到该 desc 在 NS 中出现了多次，需要手动修改
                print(len(ns_indexes), end=end)
                errors.append(('multi-desc', lineno, line))
                continue

            if len(ns_indexes) == 0:
                # 未在 NS 中找到，请检查代码
                print('M', end=end)
                errors.append((f'miss', lineno, line))
                continue

            ns_index = ns_indexes[0]

            if int(index_s) == ns_index:
                # 无需修改（忽略）
                print('.', end=end)
            else:
                # 更新 desc 唯一相同但 index 不同的代码
                new_text[lineno - 1] = line.replace(index_s, str(ns_index))
                cnt_updated += 1
                print('U', end=end)

        print(f"\n\n查找到 {cnt} 个，修改了 {cnt_updated} 个\n")

        for error, lineno, line in errors:
            print(line.strip())
            print(f'WARNING: {error} at line {lineno}\n')

        return new_text

    def update(self):
        new_text = self._modify_indexes()
        with open(self.script_path, 'w', encoding='utf-8') as f:
            f.write(''.join(new_text))

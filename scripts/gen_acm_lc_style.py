# -*- coding: utf-8 -*-
"""
按「个人模板风格」生成 ACM 单组输入解题文件。

与 acm-solutions/（多组测试）的区别：
    - 单组输入，直接用 input() 读取，适合本地手动调试与单例对拍。
    - 文件结构与 ACM-lc/HOT100 下已写的题解保持一致的风格。

模板风格:
    def 函数名(参数):
        \"\"\"
        :type 参数: 类型
        :rtype: 返回类型
        \"\"\"
        # 在这里写你的代码
        ...

    def main():
        <读入>
        print(函数名(...))

    if __name__ == "__main__":
        main()

    # 题面 / 示例 / 思路 / 输入格式 / 样例（以 # 注释放在文件末尾）

用法:
    python scripts/gen_acm_lc_style.py

产出:
    acm-solutions-lc-style/01-哈希/0001-两数之和.py
"""

import importlib.util
import os
import textwrap

ROOT_DIR = 'acm-solutions-lc-style'

MODULES = [
    's01_hash', 's02_two_pointers', 's03_sliding_window', 's04_substring',
    's05_array', 's06_matrix', 's07_linked_list', 's08_binary_tree',
    's09_graph', 's10_backtracking', 's11_binary_search', 's12_stack',
    's13_heap', 's14_greedy', 's15_dp', 's16_dp2', 's17_tricks',
]

HERE = os.path.dirname(os.path.abspath(__file__))

HEADER = '''# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: {num}    标题: {title}    难度: {difficulty}    分类: {category}
# 链接: https://leetcode.cn/problems/{slug}/
# 运行: python3 "{file_name}"   （按提示输入，或重定向样例输入）
'''


def _load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def load_meta():
    """从 gen_hot100_templates.py 复用题面元信息（描述 / 示例 / 思路提示）。"""
    mod = _load(os.path.join(HERE, 'gen_hot100_templates.py'), '_hot100_tpl')
    meta = {}
    for p in mod.PROBLEMS:
        # (num, slug, title, difficulty, category, func, params, ret, desc, example, hint)
        meta[p[0]] = {
            'slug': p[1], 'title': p[2], 'difficulty': p[3], 'category': p[4],
            'desc': p[8], 'example': p[9], 'hint': p[10],
        }
    return meta


def build_function_block(p):
    """按个人模板风格组装函数定义块（可按需前置 prelude：节点类 / 辅助函数）。"""
    parts = []
    if p.get('prelude'):
        parts.append(p['prelude'].strip('\n'))
    if p.get('code'):
        parts.append(p['code'].strip('\n'))
        return '\n\n\n'.join(parts)

    typedoc = ''.join('    :type %s: %s\n' % (n, t) for n, t in p['params'])
    sig = ', '.join(n for n, _ in p['params'])
    parts.append((
        'def {func}({sig}):\n'
        '    """\n'
        '{typedoc}'
        '    :rtype: {ret}\n'
        '    """\n'
        '{body}'
    ).format(func=p['func'], sig=sig, typedoc=typedoc, ret=p['ret'], body=p['body'].rstrip('\n')))
    return '\n\n\n'.join(parts)


def build_doc(num, meta, p):
    """题面等说明以 # 注释放在文件末尾。"""
    out = []
    out.append('# %d. %s  %s' % (num, meta['title'], meta['difficulty']))
    out.append('#')
    out.append('# 【题目描述】')
    for ln in textwrap.wrap(meta['desc'], width=72) or ['']:
        out.append('# ' + ln)
    out.append('#')
    out.append('# 【示例】')
    for ln in meta['example'].split('\n'):
        out.append('# ' + ln)
    out.append('#')
    out.append('# 【思路提示】')
    for ln in textwrap.wrap(meta['hint'], width=72) or ['']:
        out.append('# ' + ln)
    out.append('#')
    out.append('# 【输入格式】')
    for ln in p['inp'].split('\n'):
        out.append('# ' + ln)
    out.append('#')
    out.append('# 【样例输入】')
    sample_in = p['sample_in'].rstrip('\n')
    if sample_in:
        for ln in sample_in.split('\n'):
            out.append('# ' + ln)
    else:
        out.append('# (无)')
    out.append('# 【样例输出】')
    for ln in p['sample_out'].rstrip('\n').split('\n'):
        out.append('# ' + ln)
    return '\n'.join(out)


def main():
    base = os.path.dirname(HERE)
    root = os.path.join(base, ROOT_DIR)
    meta_all = load_meta()

    problems = []
    for name in MODULES:
        problems.extend(_load(os.path.join(HERE, 'acm_lc_data', name + '.py'), name).PROBLEMS)

    if len(problems) != 100:
        raise SystemExit('题目数量应为 100，当前为 %d' % len(problems))

    nums = [p['num'] for p in problems]
    if len(set(nums)) != len(nums):
        dup = sorted({n for n in nums if nums.count(n) > 1})
        raise SystemExit('存在重复题号: %s' % dup)

    missing = [n for n in nums if n not in meta_all]
    if missing:
        raise SystemExit('以下题号缺少题面元信息: %s' % sorted(missing))

    cats = []
    for p in problems:
        c = meta_all[p['num']]['category']
        if c not in cats:
            cats.append(c)
    order = {c: i for i, c in enumerate(cats)}
    problems.sort(key=lambda p: (order[meta_all[p['num']]['category']], p['num']))

    written = []
    for idx, p in enumerate(problems, 1):
        num = p['num']
        meta = meta_all[num]
        dir_name = '%02d-%s' % (order[meta['category']] + 1, meta['category'])
        target_dir = os.path.join(root, dir_name)
        os.makedirs(target_dir, exist_ok=True)

        file_name = '%04d-%s.py' % (num, meta['title'])
        content = HEADER.format(
            num=num, title=meta['title'], difficulty=meta['difficulty'],
            category=meta['category'], slug=meta['slug'], file_name=file_name,
        )
        content += '\n' + build_function_block(p) + '\n\n\n'
        content += 'def main():\n' + p['main'].rstrip('\n') + '\n\n\n'
        content += 'if __name__ == "__main__":\n    main()\n\n\n'
        content += build_doc(num, meta, p) + '\n'

        with open(os.path.join(target_dir, file_name), 'w', encoding='utf-8') as f:
            f.write(content)
        written.append((idx, num, meta, dir_name, file_name))

    write_readme(root, written, cats, order)
    print('生成完成: %d 个单组输入解题' % len(written))
    for c in cats:
        d = '%02d-%s' % (order[c] + 1, c)
        n = sum(1 for w in written if w[2]['category'] == c)
        print('  %-16s %d 题' % (d, n))
    print('目录: %s' % os.path.relpath(root, base))


def write_readme(root, written, cats, order):
    total = len(written)
    lines = []
    lines.append('# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）')
    lines.append('')
    lines.append('> 本目录按「个人模板风格」编写，与 `acm-solutions/`（多组测试格式）并存，两者互不影响。')
    lines.append('> `ACM-lc/` 为你自己手写的题解，保持原样不动。')
    lines.append('')
    lines.append('## 文件结构')
    lines.append('')
    lines.append('```python')
    lines.append('def 函数名(参数):')
    lines.append('    """')
    lines.append('    :type 参数: 类型')
    lines.append('    :rtype: 返回类型')
    lines.append('    """')
    lines.append('    # 在这里写你的代码')
    lines.append('    ...')
    lines.append('')
    lines.append('')
    lines.append('def main():')
    lines.append('    <读入>')
    lines.append('    print(函数名(...))')
    lines.append('')
    lines.append('')
    lines.append('if __name__ == "__main__":')
    lines.append('    main()')
    lines.append('')
    lines.append('')
    lines.append('# 题面 / 示例 / 思路 / 输入格式 / 样例（以 # 注释放在文件末尾）')
    lines.append('```')
    lines.append('')
    lines.append('## 输入输出约定')
    lines.append('')
    lines.append('- **单组输入**，直接 `input()` 读取，适合本地调试与单例对拍。')
    lines.append('- 数组用 `eval(input())` 读取（如 `[1,2,3]`）；标量用 `int(input())`；字符串用 `input()`。')
    lines.append('- 输出直接 `print(...)`，即 Python 原生格式（如 `[0, 1]`、`True`、`6`）。')
    lines.append('- 每个文件末尾的注释里写明了「输入格式」与「样例输入 / 样例输出」，可直接照着输入。')
    lines.append('')
    lines.append('## 运行方式')
    lines.append('')
    lines.append('```bash')
    lines.append("cd acm-solutions-lc-style")
    lines.append('echo "4;2 7 11 15;9" | tr ";" "\\n" | python3 "01-哈希/0001-两数之和.py"')
    lines.append('```')
    lines.append('')
    lines.append('## 题型分布')
    lines.append('')
    lines.append('| 分类 | 题量 | 目录 |')
    lines.append('| --- | --- | --- |')
    for c in cats:
        n = sum(1 for w in written if w[2]['category'] == c)
        lines.append('| %s | %d | `%02d-%s/` |' % (c, n, order[c] + 1, c))
    lines.append('| **合计** | **%d** | |' % total)
    lines.append('')
    lines.append('## 题目清单')
    lines.append('')
    lines.append('| # | 题号 | 标题 | 难度 | 分类 | 文件 |')
    lines.append('| --- | --- | --- | --- | --- | --- |')
    for idx, num, meta, dir_name, file_name in written:
        lines.append('| %d | %d | %s | %s | %s | `%s/%s` |' % (
            idx, num, meta['title'], meta['difficulty'], meta['category'], dir_name, file_name))
    lines.append('')
    lines.append('## 维护方式')
    lines.append('')
    lines.append('函数体与 main 存放在 `scripts/acm_lc_data/` 各模块中，题面元信息复用 `scripts/gen_hot100_templates.py`。')
    lines.append('修改后重新生成：')
    lines.append('')
    lines.append('```bash')
    lines.append('python scripts/gen_acm_lc_style.py')
    lines.append('python scripts/check_acm_lc_style.py')
    lines.append('```')
    lines.append('')

    with open(os.path.join(root, 'README.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))


if __name__ == '__main__':
    main()

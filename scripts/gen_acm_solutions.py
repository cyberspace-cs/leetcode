# -*- coding: utf-8 -*-
"""
生成 LeetCode 热题 HOT 100 的「ACM 模式完整解题」文件。

用法:
    python scripts/gen_acm_solutions.py

产出:
    acm-solutions/
      README.md
      01-哈希/0001-两数之和.py
      ...

约定:
    - 每组测试数据由各题自己的 solve(it) 负责读入，it 为 token 迭代器。
    - 统一外层框架：先读 T，再循环 T 次调用 solve(it)，逐组输出。
    - 每个解题数据模块位于 scripts/acm_data/ 下，暴露 PROBLEMS 列表。
"""

import importlib.util
import os

ROOT_DIR = 'acm-solutions'

# 解题数据模块（顺序即分类顺序）
MODULES = [
    'c01_hash',
    'c02_two_pointers',
    'c03_sliding_window',
    'c04_substring',
    'c05_array',
    'c06_matrix',
    'c07_linked_list',
    'c08_binary_tree',
    'c09_graph',
    'c10_backtracking',
    'c11_binary_search',
    'c12_stack',
    'c13_heap',
    'c14_greedy',
    'c15_dp',
    'c16_dp2',
    'c17_tricks',
]

CATEGORY_ORDER = []

TEMPLATE = '''# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
{sep}
题号 : {num}
标题 : {title}
难度 : {difficulty}
分类 : {category}
链接 : https://leetcode.cn/problems/{slug}/
{sep}

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
{inp}

【输出格式】
{outp}

【样例输入】
{sample_in}
【样例输出】
{sample_out}
"""

import sys


{code}

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    t = int(next(it))
    out = []
    for _ in range(t):
        out.append(str(solve(it)))
    sys.stdout.write("\\n".join(out) + "\\n")


if __name__ == "__main__":
    main()
'''


def load_problems(module_name):
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, 'acm_data', module_name + '.py')
    spec = importlib.util.spec_from_file_location(module_name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.PROBLEMS


def main():
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    root = os.path.join(base, ROOT_DIR)

    problems = []
    for name in MODULES:
        problems.extend(load_problems(name))

    cats = []
    for p in problems:
        if p['category'] not in cats:
            cats.append(p['category'])

    order = {c: i for i, c in enumerate(cats)}
    problems.sort(key=lambda p: (order[p['category']], p['num']))

    if len(problems) != 100:
        raise SystemExit('题目数量应为 100，当前为 %d' % len(problems))

    nums = [p['num'] for p in problems]
    if len(set(nums)) != len(nums):
        dup = sorted({n for n in nums if nums.count(n) > 1})
        raise SystemExit('存在重复题号: %s' % dup)

    written = []
    for idx, p in enumerate(problems, 1):
        dir_name = '%02d-%s' % (order[p['category']] + 1, p['category'])
        target_dir = os.path.join(root, dir_name)
        os.makedirs(target_dir, exist_ok=True)

        content = TEMPLATE.format(
            sep='=' * 64,
            num=p['num'], title=p['title'], difficulty=p['difficulty'],
            category=p['category'], slug=p['slug'],
            inp=p['inp'], outp=p['outp'],
            sample_in=p['sample_in'], sample_out=p['sample_out'],
            code=p['code'].strip('\n'),
        )
        file_name = '%04d-%s.py' % (p['num'], p['title'])
        with open(os.path.join(target_dir, file_name), 'w', encoding='utf-8') as f:
            f.write(content)
        written.append((idx, p, dir_name, file_name))

    write_readme(root, written, cats)
    print('生成完成: %d 个 ACM 完整解题' % len(written))
    for c in cats:
        d = '%02d-%s' % (order[c] + 1, c)
        n = sum(1 for w in written if w[1]['category'] == c)
        print('  %-16s %d 题' % (d, n))
    print('目录: %s' % os.path.relpath(root, base))


def write_readme(root, written, cats):
    order = {c: i for i, c in enumerate(cats)}
    total = len(written)

    lines = []
    lines.append('# LeetCode 热题 HOT 100 · ACM 模式完整解题')
    lines.append('')
    lines.append('> 本目录提供 **完整、可直接运行** 的 ACM 式解题代码（标准输入 / 标准输出），')
    lines.append('> 与 `hot100/` 的题面模板、`ACM-lc/` 的个人练习互不影响。')
    lines.append('')
    lines.append('## 输入输出约定')
    lines.append('')
    lines.append('- 第 1 行为 `T`，表示测试数据组数，之后紧跟 T 组数据。')
    lines.append('- 每组数据的输入格式见各文件头部的「输入格式」说明。')
    lines.append('- 每组数据的输出占若干行，组与组之间按顺序依次输出。')
    lines.append('- 布尔值统一输出 `true` / `false`；空结果统一输出 `EMPTY`。')
    lines.append('')
    lines.append('## 命名规范')
    lines.append('')
    lines.append('- 分类目录：`NN-题型/`（两位顺序号，固定排序）')
    lines.append('- 题目文件：`题号4位补零-中文标题.py`，例如 `0001-两数之和.py`')
    lines.append('')
    lines.append('## 运行方式')
    lines.append('')
    lines.append('```bash')
    lines.append('# 用文件头部的样例数据自测')
    lines.append('printf \'2\\n4 9\\n2 7 11 15\\n3 6\\n3 2 4\\n\' | python3 "acm-solutions/01-哈希/0001-两数之和.py"')
    lines.append('```')
    lines.append('')
    lines.append('## 题型分布')
    lines.append('')
    lines.append('| 分类 | 题量 | 目录 |')
    lines.append('| --- | --- | --- |')
    for c in cats:
        n = sum(1 for w in written if w[1]['category'] == c)
        lines.append('| %s | %d | `%02d-%s/` |' % (c, n, order[c] + 1, c))
    lines.append('| **合计** | **%d** | |' % total)
    lines.append('')
    lines.append('## 题目清单')
    lines.append('')
    lines.append('| # | 题号 | 标题 | 难度 | 分类 | 文件 |')
    lines.append('| --- | --- | --- | --- | --- | --- |')
    for idx, p, dir_name, file_name in written:
        lines.append('| %d | %d | %s | %s | %s | `%s/%s` |' % (
            idx, p['num'], p['title'], p['difficulty'], p['category'], dir_name, file_name))
    lines.append('')
    lines.append('## 维护方式')
    lines.append('')
    lines.append('解题代码存放在 `scripts/acm_data/` 各模块中，修改后重新生成即可：')
    lines.append('')
    lines.append('```bash')
    lines.append('python scripts/gen_acm_solutions.py')
    lines.append('```')
    lines.append('')

    with open(os.path.join(root, 'README.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))


if __name__ == '__main__':
    main()

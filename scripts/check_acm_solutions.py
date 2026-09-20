# -*- coding: utf-8 -*-
"""
校验 acm-solutions/ 下所有解题文件：用文件自带的样例输入运行，比对样例输出。

用法:
    python scripts/check_acm_solutions.py
"""

import importlib.util
import os
import subprocess
import sys

MODULES = [
    'c01_hash', 'c02_two_pointers', 'c03_sliding_window', 'c04_substring',
    'c05_array', 'c06_matrix', 'c07_linked_list', 'c08_binary_tree',
    'c09_graph', 'c10_backtracking', 'c11_binary_search', 'c12_stack',
    'c13_heap', 'c14_greedy', 'c15_dp', 'c16_dp2', 'c17_tricks',
]

IGNORE = []


def norm(text):
    lines = [ln.rstrip() for ln in text.strip('\n').split('\n')]
    while lines and lines[-1] == '':
        lines.pop()
    return '\n'.join(lines)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    base = os.path.dirname(here)
    data_dir = os.path.join(here, 'acm_data')

    problems = []
    for name in MODULES:
        spec = importlib.util.spec_from_file_location(name, os.path.join(data_dir, name + '.py'))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        problems.extend(mod.PROBLEMS)

    passed, failed = 0, []
    for p in problems:
        # 在 acm-solutions 下按题号前缀查找生成文件
        target = None
        for root, _dirs, files in os.walk(os.path.join(base, 'acm-solutions')):
            for fn in files:
                if fn.startswith('%04d-' % p['num']) and fn.endswith('.py'):
                    target = os.path.join(root, fn)
                    break
            if target:
                break
        if not target:
            failed.append((p['num'], p['title'], '未找到生成文件'))
            continue

        proc = subprocess.run(
            [sys.executable, target],
            input=p['sample_in'].encode('utf-8'),
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        )
        got = norm(proc.stdout.decode('utf-8', 'replace'))
        want = norm(p['sample_out'])
        if proc.returncode != 0:
            failed.append((p['num'], p['title'], '运行报错: %s' % proc.stderr.decode('utf-8', 'replace').strip().split('\n')[-1]))
        elif got != want:
            failed.append((p['num'], p['title'], '输出不一致\n  期望:\n%s\n  实际:\n%s' % (
                '\n'.join('    ' + x for x in want.split('\n')),
                '\n'.join('    ' + x for x in got.split('\n')))))
        else:
            passed += 1

    print('通过: %d / %d' % (passed, len(problems)))
    if failed:
        print('\n失败用例:')
        for num, title, msg in failed:
            print('  LC%s %s -> %s' % (num, title, msg))
        return 1
    print('全部样例通过 ✅')
    return 0


if __name__ == '__main__':
    sys.exit(main())

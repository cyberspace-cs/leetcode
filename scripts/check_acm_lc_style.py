# -*- coding: utf-8 -*-
"""
校验 acm-solutions-lc-style/ 下所有解题文件：
用文件自带的样例输入运行，比对样例输出。

用法:
    python scripts/check_acm_lc_style.py
"""

import importlib.util
import os
import subprocess
import sys

MODULES = [
    's01_hash', 's02_two_pointers', 's03_sliding_window', 's04_substring',
    's05_array', 's06_matrix', 's07_linked_list', 's08_binary_tree',
    's09_graph', 's10_backtracking', 's11_binary_search', 's12_stack',
    's13_heap', 's14_greedy', 's15_dp', 's16_dp2', 's17_tricks',
]

HERE = os.path.dirname(os.path.abspath(__file__))


def norm(text):
    lines = [ln.rstrip() for ln in text.strip('\n').split('\n')]
    while lines and lines[-1] == '':
        lines.pop()
    return '\n'.join(lines)


def main():
    base = os.path.dirname(HERE)
    root = os.path.join(base, 'acm-solutions-lc-style')

    problems = []
    for name in MODULES:
        spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, 'acm_lc_data', name + '.py'))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        problems.extend(mod.PROBLEMS)

    passed, failed = 0, []
    for p in problems:
        target = None
        for cur_dir, _dirs, files in os.walk(root):
            for fn in files:
                if fn.startswith('%04d-' % p['num']) and fn.endswith('.py'):
                    target = os.path.join(cur_dir, fn)
                    break
            if target:
                break
        if not target:
            failed.append((p['num'], '未找到生成文件'))
            continue

        proc = subprocess.run(
            [sys.executable, target],
            input=p['sample_in'].encode('utf-8'),
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        )
        got = norm(proc.stdout.decode('utf-8', 'replace'))
        want = norm(p['sample_out'])
        if proc.returncode != 0:
            err = proc.stderr.decode('utf-8', 'replace').strip().split('\n')[-1]
            failed.append((p['num'], '运行报错: %s' % err))
        elif got != want:
            failed.append((p['num'], '输出不一致\n  期望: %s\n  实际: %s' % (
                want.replace('\n', ' | '), got.replace('\n', ' | '))))
        else:
            passed += 1

    print('通过: %d / %d' % (passed, len(problems)))
    if failed:
        print('\n失败用例:')
        for num, msg in failed:
            print('  LC%s -> %s' % (num, msg))
        return 1
    print('全部样例通过 ✅')
    return 0


if __name__ == '__main__':
    sys.exit(main())

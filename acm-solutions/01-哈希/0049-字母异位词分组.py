# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 49
标题 : 字母异位词分组
难度 : 中等
分类 : 哈希
链接 : https://leetcode.cn/problems/group-anagrams/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n；第二行：n 个仅含小写字母的字符串。

【输出格式】
第一行：组数 g；随后 g 行，每行一组，组内字符串按字典序升序、空格分隔；各组之间按行首字符串字典序升序。

【样例输入】
1
6
eat tea tan ate nat bat

【样例输出】
3
ate eat tea
bat
nat tan

"""

import sys


def solve(it):
    n = int(next(it))
    strs = [next(it) for _ in range(n)]
    groups = {}
    for s in strs:
        groups.setdefault("".join(sorted(s)), []).append(s)
    rows = []
    for g in groups.values():
        g.sort()
        rows.append(" ".join(g))
    rows.sort()
    return "\n".join([str(len(rows))] + rows)

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    t = int(next(it))
    out = []
    for _ in range(t):
        out.append(str(solve(it)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

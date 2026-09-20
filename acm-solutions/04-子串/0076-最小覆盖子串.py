# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 76
标题 : 最小覆盖子串
难度 : 困难
分类 : 子串
链接 : https://leetcode.cn/problems/minimum-window-substring/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：字符串 s；第二行：字符串 t（均不含空白字符）。

【输出格式】
一行，s 中涵盖 t 全部字符的最短子串；不存在则输出 -1。

【样例输入】
2
ADOBECODEBANC
ABC
a
aa

【样例输出】
BANC
-1

"""

import sys


def solve(it):
    s = next(it)
    t = next(it)
    need = {}
    for c in t:
        need[c] = need.get(c, 0) + 1
    missing = len(t)
    left = 0
    best = None
    for right, c in enumerate(s):
        if need.get(c, 0) > 0:
            missing -= 1
        need[c] = need.get(c, 0) - 1
        while missing == 0:
            if best is None or right - left + 1 < best[1] - best[0] + 1:
                best = (left, right)
            need[s[left]] = need.get(s[left], 0) + 1
            if need[s[left]] > 0:
                missing += 1
            left += 1
    return s[best[0]:best[1] + 1] if best else "-1"

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

# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 131
标题 : 分割回文串
难度 : 中等
分类 : 回溯
链接 : https://leetcode.cn/problems/palindrome-partitioning/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
一行：字符串 s（仅含小写字母）。

【输出格式】
第一行：方案数 g；随后 g 行，每行若干回文子串（空格分隔）。

【样例输入】
2
aab
a

【样例输出】
2
a a b
aa b
1
a

"""

import sys


def solve(it):
    s = next(it)
    n = len(s)
    res = []
    path = []

    def is_pal(l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def bt(start):
        if start == n:
            res.append(" ".join(path))
            return
        for end in range(start, n):
            if is_pal(start, end):
                path.append(s[start:end + 1])
                bt(end + 1)
                path.pop()

    bt(0)
    return "\n".join([str(len(res))] + res)

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

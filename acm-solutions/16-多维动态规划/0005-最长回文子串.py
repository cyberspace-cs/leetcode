# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 5
标题 : 最长回文子串
难度 : 中等
分类 : 多维动态规划
链接 : https://leetcode.cn/problems/longest-palindromic-substring/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
一行：字符串 s（不含空白字符）。

【输出格式】
一行，最长回文子串（若存在多个等长答案，输出中心扩展过程中最先得到的那个）。

【样例输入】
3
babad
cbbd
a

【样例输出】
bab
bb
a

"""

import sys


def solve(it):
    s = next(it)
    n = len(s)
    if n == 0:
        return "EMPTY"
    start, best = 0, 1
    for i in range(n):
        for l, r in ((i, i), (i, i + 1)):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            length = r - l - 1
            if length > best:
                best = length
                start = l + 1
    return s[start:start + best]

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

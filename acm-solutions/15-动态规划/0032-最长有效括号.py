# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 32
标题 : 最长有效括号
难度 : 困难
分类 : 动态规划
链接 : https://leetcode.cn/problems/longest-valid-parentheses/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
一行：字符串 s（仅含左右括号）。

【输出格式】
一行，最长有效括号子串的长度。

【样例输入】
3
(()
)()())
()(())

【样例输出】
2
4
6

"""

import sys


def solve(it):
    s = next(it)
    n = len(s)
    dp = [0] * n
    best = 0
    for i in range(1, n):
        if s[i] != ")":
            continue
        if s[i - 1] == "(":
            dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
        else:
            j = i - dp[i - 1] - 1
            if j >= 0 and s[j] == "(":
                dp[i] = dp[i - 1] + 2 + (dp[j - 1] if j >= 1 else 0)
        if dp[i] > best:
            best = dp[i]
    return best

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

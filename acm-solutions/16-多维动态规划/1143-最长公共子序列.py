# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 1143
标题 : 最长公共子序列
难度 : 中等
分类 : 多维动态规划
链接 : https://leetcode.cn/problems/longest-common-subsequence/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：字符串 text1；第二行：字符串 text2。

【输出格式】
一行，最长公共子序列的长度。

【样例输入】
3
abcde
ace
abc
abc
aaa
aa

【样例输出】
3
3
2

"""

import sys


def solve(it):
    a = next(it)
    b = next(it)
    n, m = len(a), len(b)
    dp = [0] * (m + 1)
    for i in range(1, n + 1):
        prev = 0
        for j in range(1, m + 1):
            tmp = dp[j]
            if a[i - 1] == b[j - 1]:
                dp[j] = prev + 1
            else:
                dp[j] = max(dp[j], dp[j - 1])
            prev = tmp
    return dp[m]

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

# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 72
标题 : 编辑距离
难度 : 中等
分类 : 多维动态规划
链接 : https://leetcode.cn/problems/edit-distance/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：字符串 word1；第二行：字符串 word2。

【输出格式】
一行，最少操作次数（插入 / 删除 / 替换）。

【样例输入】
3
horse
ros
intention
execution
abc
abc

【样例输出】
3
5
0

"""

import sys


def solve(it):
    a = next(it)
    b = next(it)
    n, m = len(a), len(b)
    dp = list(range(m + 1))
    for i in range(1, n + 1):
        prev = dp[0]
        dp[0] = i
        for j in range(1, m + 1):
            tmp = dp[j]
            if a[i - 1] == b[j - 1]:
                dp[j] = prev
            else:
                dp[j] = 1 + min(prev, dp[j], dp[j - 1])
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

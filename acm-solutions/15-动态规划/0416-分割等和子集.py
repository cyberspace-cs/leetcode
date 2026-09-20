# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 416
标题 : 分割等和子集
难度 : 中等
分类 : 动态规划
链接 : https://leetcode.cn/problems/partition-equal-subset-sum/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n；第二行：n 个正整数。

【输出格式】
一行，true 或 false。

【样例输入】
3
4
1 5 11 5
4
1 2 3 5
1
2

【样例输出】
true
false
false

"""

import sys


def solve(it):
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    total = sum(a)
    if total % 2:
        return "false"
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    for x in a:
        for j in range(target, x - 1, -1):
            if dp[j - x]:
                dp[j] = True
    return "true" if dp[target] else "false"

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

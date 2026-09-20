# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 128
标题 : 最长连续序列
难度 : 中等
分类 : 哈希
链接 : https://leetcode.cn/problems/longest-consecutive-sequence/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n；第二行：n 个整数。

【输出格式】
一行，最长连续数字序列的长度。

【样例输入】
3
6
100 4 200 1 3 2
4
0 0 0 0
5
1 2 3 4 5

【样例输出】
4
1
5

"""

import sys


def solve(it):
    n = int(next(it))
    nums = [int(next(it)) for _ in range(n)]
    pool = set(nums)
    best = 0
    for x in pool:
        if x - 1 in pool:
            continue
        y = x
        while y + 1 in pool:
            y += 1
        if y - x + 1 > best:
            best = y - x + 1
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

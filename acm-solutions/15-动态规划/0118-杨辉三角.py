# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 118
标题 : 杨辉三角
难度 : 简单
分类 : 动态规划
链接 : https://leetcode.cn/problems/pascals-triangle/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
一行：numRows，表示行数。

【输出格式】
numRows 行，每行该行的数字（空格分隔）。

【样例输入】
1
5

【样例输出】
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1

"""

import sys


def solve(it):
    n = int(next(it))
    rows = []
    cur = []
    for _ in range(n):
        cur = [1] + [cur[i] + cur[i + 1] for i in range(len(cur) - 1)] + [1] if cur else [1]
        rows.append(" ".join(map(str, cur)))
    return "\n".join(rows) if rows else "EMPTY"

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

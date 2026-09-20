# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 53
标题 : 最大子数组和
难度 : 中等
分类 : 普通数组
链接 : https://leetcode.cn/problems/maximum-subarray/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n；第二行：n 个整数。

【输出格式】
一行，最大连续子数组和。

【样例输入】
2
9
-2 1 -3 4 -1 2 1 -5 4
1
-1

【样例输出】
6
-1

"""

import sys


def solve(it):
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    cur = best = a[0]
    for x in a[1:]:
        cur = x if cur < 0 else cur + x
        if cur > best:
            best = cur
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

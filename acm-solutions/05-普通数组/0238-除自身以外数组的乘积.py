# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 238
标题 : 除自身以外数组的乘积
难度 : 中等
分类 : 普通数组
链接 : https://leetcode.cn/problems/product-of-array-except-self/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n；第二行：n 个整数。

【输出格式】
一行，answer[i] 为除 nums[i] 外其余元素的乘积。

【样例输入】
2
4
1 2 3 4
5
-1 1 0 -3 3

【样例输出】
24 12 8 6
0 0 9 0 0

"""

import sys


def solve(it):
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    res = [1] * n
    p = 1
    for i in range(n):
        res[i] = p
        p *= a[i]
    p = 1
    for i in range(n - 1, -1, -1):
        res[i] *= p
        p *= a[i]
    return " ".join(map(str, res))

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

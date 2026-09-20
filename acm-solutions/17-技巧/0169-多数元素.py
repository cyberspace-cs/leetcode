# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 169
标题 : 多数元素
难度 : 简单
分类 : 技巧
链接 : https://leetcode.cn/problems/majority-element/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n；第二行：n 个整数（保证存在出现次数 > n/2 的元素）。

【输出格式】
一行，多数元素。

【样例输入】
2
7
2 2 1 1 1 2 2
3
3 2 3

【样例输出】
2
3

"""

import sys


def solve(it):
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    cand = None
    count = 0
    for x in a:
        if count == 0:
            cand = x
            count = 1
        elif x == cand:
            count += 1
        else:
            count -= 1
    return cand

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

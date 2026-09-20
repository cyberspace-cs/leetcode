# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 1
标题 : 两数之和
难度 : 简单
分类 : 哈希
链接 : https://leetcode.cn/problems/two-sum/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n target；第二行：n 个整数。

【输出格式】
一行，两个 0-based 下标（升序，空格分隔），保证有唯一解。

【样例输入】
2
4 9
2 7 11 15
3 6
3 2 4

【样例输出】
0 1
1 2

"""

import sys


def solve(it):
    n = int(next(it)); target = int(next(it))
    nums = [int(next(it)) for _ in range(n)]
    seen = {}
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return "%d %d" % (seen[need], i)
        seen[x] = i
    return "-1 -1"

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

# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 287
标题 : 寻找重复数
难度 : 中等
分类 : 技巧
链接 : https://leetcode.cn/problems/find-the-duplicate-number/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n；第二行：n 个整数（取值在 1..n-1 之间，仅有一个数字重复）。

【输出格式】
一行，重复的数字。

【样例输入】
2
5
1 3 4 2 2
6
3 1 3 4 2 5

【样例输出】
2
3

"""

import sys


def solve(it):
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    slow = fast = a[0]
    while True:
        slow = a[slow]
        fast = a[a[fast]]
        if slow == fast:
            break
    slow = a[0]
    while slow != fast:
        slow = a[slow]
        fast = a[fast]
    return slow

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

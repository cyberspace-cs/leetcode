# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 239
标题 : 滑动窗口最大值
难度 : 困难
分类 : 子串
链接 : https://leetcode.cn/problems/sliding-window-maximum/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n k；第二行：n 个整数。窗口每次右移一位，共 n-k+1 个窗口。

【输出格式】
一行，每个窗口的最大值（空格分隔）。

【样例输入】
2
8 3
1 3 -1 -3 5 3 6 7
1 1
5

【样例输出】
3 3 5 5 6 7
5

"""

import sys


from collections import deque


def solve(it):
    n = int(next(it))
    k = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    dq = deque()
    res = []
    for i, x in enumerate(a):
        while dq and a[dq[-1]] <= x:
            dq.pop()
        dq.append(i)
        if dq[0] <= i - k:
            dq.popleft()
        if i >= k - 1:
            res.append(a[dq[0]])
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

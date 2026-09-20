# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 994
标题 : 腐烂的橘子
难度 : 中等
分类 : 图论
链接 : https://leetcode.cn/problems/rotting-oranges/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：m n；随后 m 行，每行 n 个整数（0 空格子 / 1 新鲜 / 2 腐烂）。

【输出格式】
一行，所有橘子腐烂所需的最少分钟数；不可能则输出 -1。

【样例输入】
3
3 3
2 1 1
1 1 0
0 1 1
3 3
2 1 1
0 1 1
1 0 1
1 1
0

【样例输出】
4
-1
0

"""

import sys


from collections import deque


def solve(it):
    m = int(next(it))
    n = int(next(it))
    g = [[int(next(it)) for _ in range(n)] for _ in range(m)]
    dq = deque()
    fresh = 0
    for i in range(m):
        for j in range(n):
            if g[i][j] == 2:
                dq.append((i, j, 0))
            elif g[i][j] == 1:
                fresh += 1
    minutes = 0
    while dq:
        i, j, t = dq.popleft()
        if t > minutes:
            minutes = t
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            x, y = i + di, j + dj
            if 0 <= x < m and 0 <= y < n and g[x][y] == 1:
                g[x][y] = 2
                fresh -= 1
                dq.append((x, y, t + 1))
    return minutes if fresh == 0 else -1

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

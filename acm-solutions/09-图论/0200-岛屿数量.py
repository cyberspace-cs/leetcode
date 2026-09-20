# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 200
标题 : 岛屿数量
难度 : 中等
分类 : 图论
链接 : https://leetcode.cn/problems/number-of-islands/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：m n；随后 m 行，每行 n 个以空格分隔的字符（0 或 1）。

【输出格式】
一行，岛屿（上下左右相连的 1）数量。

【样例输入】
2
4 5
1 1 1 1 0
1 1 0 1 0
1 1 0 0 0
0 0 0 0 0
3 3
1 1 0
1 0 0
0 0 1

【样例输出】
1
2

"""

import sys


def solve(it):
    m = int(next(it))
    n = int(next(it))
    g = [[next(it) for _ in range(n)] for _ in range(m)]
    seen = [[False] * n for _ in range(m)]
    cnt = 0
    for i in range(m):
        for j in range(n):
            if g[i][j] == "1" and not seen[i][j]:
                cnt += 1
                seen[i][j] = True
                stack = [(i, j)]
                while stack:
                    x, y = stack.pop()
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n and g[nx][ny] == "1" and not seen[nx][ny]:
                            seen[nx][ny] = True
                            stack.append((nx, ny))
    return cnt

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

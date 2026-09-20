# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 51
标题 : N 皇后
难度 : 困难
分类 : 回溯
链接 : https://leetcode.cn/problems/n-queens/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
一行：n，表示棋盘大小。

【输出格式】
第一行：方案数 g；随后依次输出每个方案，每个方案占 n 行（Q 表示皇后，. 表示空位）。

【样例输入】
1
4

【样例输出】
2
.Q..
...Q
Q...
..Q.
..Q.
Q...
...Q
.Q..

"""

import sys


def solve(it):
    n = int(next(it))
    res = []
    cols = set()
    d1 = set()
    d2 = set()
    board = [["."] * n for _ in range(n)]

    def bt(r):
        if r == n:
            res.append("\n".join("".join(row) for row in board))
            return
        for c in range(n):
            if c in cols or (r - c) in d1 or (r + c) in d2:
                continue
            cols.add(c)
            d1.add(r - c)
            d2.add(r + c)
            board[r][c] = "Q"
            bt(r + 1)
            cols.discard(c)
            d1.discard(r - c)
            d2.discard(r + c)
            board[r][c] = "."

    bt(0)
    return "\n".join([str(len(res))] + res)

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

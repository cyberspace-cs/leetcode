# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 79
标题 : 单词搜索
难度 : 中等
分类 : 回溯
链接 : https://leetcode.cn/problems/word-search/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：m n；随后 m 行，每行 n 个字符；最后一行：word。

【输出格式】
一行，true 或 false。

【样例输入】
3
3 4
A B C E
S F C S
A D E E
ABCCED
3 4
A B C E
S F C S
A D E E
ABCB
3 4
A B C E
S F C S
A D E E
SEE

【样例输出】
true
false
true

"""

import sys


def solve(it):
    m = int(next(it))
    n = int(next(it))
    board = [[next(it) for _ in range(n)] for _ in range(m)]
    word = next(it)

    def dfs(i, j, k):
        if board[i][j] != word[k]:
            return False
        if k == len(word) - 1:
            return True
        tmp = board[i][j]
        board[i][j] = "#"
        found = False
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            x, y = i + di, j + dj
            if 0 <= x < m and 0 <= y < n and dfs(x, y, k + 1):
                found = True
                break
        board[i][j] = tmp
        return found

    for i in range(m):
        for j in range(n):
            if dfs(i, j, 0):
                return "true"
    return "false"

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

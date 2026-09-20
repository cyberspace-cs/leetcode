# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 51    标题: N 皇后    难度: 困难    分类: 回溯
# 链接: https://leetcode.cn/problems/n-queens/
# 运行: python3 "0051-N 皇后.py"   （按提示输入，或重定向样例输入）

def solve_n_queens(n):
    """
    :type n: int
    :rtype: List[List[str]]
    """
    # 在这里写你的代码
    res = []
    cols = set()
    diag1 = set()
    diag2 = set()
    board = [["."] * n for _ in range(n)]

    def backtrack(row):
        if row == n:
            res.append(["".join(r) for r in board])
            return
        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            board[row][col] = "Q"
            backtrack(row + 1)
            cols.discard(col)
            diag1.discard(row - col)
            diag2.discard(row + col)
            board[row][col] = "."

    backtrack(0)
    return res


def main():
    n = int(input())
    print(solve_n_queens(n))


if __name__ == "__main__":
    main()


# 51. N 皇后  困难
#
# 【题目描述】
# 在 n×n 棋盘上放置 n 个皇后，使它们互不攻击，返回所有不同的解法。
#
# 【示例】
# n = 4  →  [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
#
# 【思路提示】
# 逐行放置 + 用集合记录已占用的列、主对角线、副对角线来判重。
#
# 【输入格式】
# 一行：n（棋盘大小）。
#
# 【样例输入】
# 4
# 【样例输出】
# [['.Q..', '...Q', 'Q...', '..Q.'], ['..Q.', 'Q...', '...Q', '.Q..']]

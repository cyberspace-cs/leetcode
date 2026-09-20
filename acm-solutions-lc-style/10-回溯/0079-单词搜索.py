# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 79    标题: 单词搜索    难度: 中等    分类: 回溯
# 链接: https://leetcode.cn/problems/word-search/
# 运行: python3 "0079-单词搜索.py"   （按提示输入，或重定向样例输入）

def exist(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    # 在这里写你的代码
    if not board:
        return False
    m, n = len(board), len(board[0])

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
                return True
    return False


def main():
    board = eval(input())
    word = input()
    print(exist(board, word))


if __name__ == "__main__":
    main()


# 79. 单词搜索  中等
#
# 【题目描述】
# 在二维字符网格中判断能否通过上下左右相邻的单元格按顺序拼出给定单词（同一格不可重复使用）。
#
# 【示例】
# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"  →  true
#
# 【思路提示】
# DFS + 剪枝，把访问过的格子临时标记，回溯时恢复。
#
# 【输入格式】
# 第一行：二维字符网格；第二行：单词 word。
#
# 【样例输入】
# [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# ABCCED
# 【样例输出】
# True

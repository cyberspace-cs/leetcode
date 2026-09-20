# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 061 / 100 题
================================================================
题号 : 79
标题 : 单词搜索
难度 : 中等
分类 : 回溯
链接 : https://leetcode.cn/problems/word-search/
================================================================

【题目描述】
在二维字符网格中判断能否通过上下左右相邻的单元格按顺序拼出给定单词（同一格不可重复使用）。

【示例】
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"  →  true

【思路提示】
DFS + 剪枝，把访问过的格子临时标记，回溯时恢复。

【说明】
本文件只提供题面与解题入口，具体实现请在下方 `Solution` 中完成，
并建议在 `if __name__ == "__main__":` 区域补充自测用例。
"""

from typing import List, Optional


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass

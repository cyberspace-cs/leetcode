# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 021 / 100 题
================================================================
题号 : 240
标题 : 搜索二维矩阵 II
难度 : 中等
分类 : 矩阵
链接 : https://leetcode.cn/problems/search-a-2d-matrix-ii/
================================================================

【题目描述】
在每行从左到右、每列从上到下均递增的矩阵中查找目标值是否存在。

【示例】
matrix = [[1,4,7],[2,5,8],[3,6,9]], target = 5  →  true

【思路提示】
从右上角出发：当前值大于目标则左移一列，小于目标则下移一行。

【说明】
本文件只提供题面与解题入口，具体实现请在下方 `Solution` 中完成，
并建议在 `if __name__ == "__main__":` 区域补充自测用例。
"""

from typing import List, Optional


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass

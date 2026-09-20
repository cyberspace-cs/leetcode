# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 067 / 100 题
================================================================
题号 : 74
标题 : 搜索二维矩阵
难度 : 中等
分类 : 二分查找
链接 : https://leetcode.cn/problems/search-a-2d-matrix/
================================================================

【题目描述】
在每行升序、且每行首元素大于上一行末元素的矩阵中查找目标值。

【示例】
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3  →  true

【思路提示】
把二维矩阵视为一维有序数组做二分，通过 divmod 完成下标映射。

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

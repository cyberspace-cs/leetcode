# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 042 / 100 题
================================================================
题号 : 108
标题 : 将有序数组转换为二叉搜索树
难度 : 简单
分类 : 二叉树
链接 : https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/
================================================================

【题目描述】
把升序数组转换为高度平衡的二叉搜索树。

【示例】
nums = [-10,-3,0,5,9]  →  [0,-3,9,-10,null,5]

【思路提示】
每次取区间中点作为根，再递归构造左右子树。

【说明】
本文件只提供题面与解题入口，具体实现请在下方 `Solution` 中完成，
并建议在 `if __name__ == "__main__":` 区域补充自测用例。
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass

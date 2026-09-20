# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 049 / 100 题
================================================================
题号 : 437
标题 : 路径总和 III
难度 : 中等
分类 : 二叉树
链接 : https://leetcode.cn/problems/path-sum-iii/
================================================================

【题目描述】
统计二叉树中节点值之和等于 targetSum 的路径条数（路径方向只能向下，不必从根开始）。

【示例】
root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8  →  3

【思路提示】
前缀和 + 回溯：遍历时统计 (当前前缀和 - targetSum) 在哈希表中的出现次数。

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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass

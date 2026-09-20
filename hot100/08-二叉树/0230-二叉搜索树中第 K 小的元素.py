# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 047 / 100 题
================================================================
题号 : 230
标题 : 二叉搜索树中第 K 小的元素
难度 : 中等
分类 : 二叉树
链接 : https://leetcode.cn/problems/kth-smallest-element-in-a-bst/
================================================================

【题目描述】
返回二叉搜索树中第 k 小的元素值。

【示例】
root = [3,1,4,null,2], k = 1  →  1

【思路提示】
中序遍历，计数到第 k 个即返回（可提前剪枝）。

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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass

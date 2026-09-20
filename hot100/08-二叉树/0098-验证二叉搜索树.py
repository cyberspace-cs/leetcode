# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 037 / 100 题
================================================================
题号 : 98
标题 : 验证二叉搜索树
难度 : 中等
分类 : 二叉树
链接 : https://leetcode.cn/problems/validate-binary-search-tree/
================================================================

【题目描述】
判断二叉树是否为有效的二叉搜索树（左 < 根 < 右，且子树同样满足）。

【示例】
root = [2,1,3]  →  true

【思路提示】
递归时向下传递上下界 (low, high)；或中序遍历检查是否严格递增。

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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass

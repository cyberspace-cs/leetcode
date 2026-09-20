# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 036 / 100 题
================================================================
题号 : 94
标题 : 二叉树的中序遍历
难度 : 简单
分类 : 二叉树
链接 : https://leetcode.cn/problems/binary-tree-inorder-traversal/
================================================================

【题目描述】
返回二叉树的中序遍历（左-根-右）结果。

【示例】
root = [1,null,2,3]  →  [1,3,2]

【思路提示】
递归或显式栈；进阶可用 Morris 遍历做到 O(1) 额外空间。

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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass

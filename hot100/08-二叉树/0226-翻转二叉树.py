# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 046 / 100 题
================================================================
题号 : 226
标题 : 翻转二叉树
难度 : 简单
分类 : 二叉树
链接 : https://leetcode.cn/problems/invert-binary-tree/
================================================================

【题目描述】
翻转二叉树，使每个节点的左右子树互换，返回根节点。

【示例】
root = [4,2,7,1,3,6,9]  →  [4,7,2,9,6,3,1]

【思路提示】
递归交换每个节点的左右子树。

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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
